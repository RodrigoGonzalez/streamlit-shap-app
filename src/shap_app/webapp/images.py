""" Helper functions for displaying images in Streamlit. """
import base64
import os
import pickle
from collections.abc import Callable
from typing import Any
from typing import TypeVar
from typing import cast

import pandas as pd
import streamlit as st

F = TypeVar("F", bound=Callable[..., Any])


def st_typed_cache_resource(func: F) -> F:
    """
    This is a decorator for Streamlit cache resource. It is used to cache the
    output of a function that is computationally expensive to recreate each
    time the script is run. The function must be a typed function.

    Implemented to make MyPy happy.

    Parameters
    ----------
    func : Callable[..., Any]
        The function whose output needs to be cached.

    Returns
    -------
    Callable[..., Any]
        The same function with caching enabled.
    """
    from streamlit import cache_resource

    return cast(F, cache_resource(func))


def render_svg(svg: str) -> None:
    """
    Render the given SVG string as an image.

    This function takes an SVG string, encodes it to base64, and then
    renders it as an image using Streamlit's write function. The image
    is embedded directly into the HTML using a data URL.

    Parameters
    ----------
    svg : str
        The SVG string to render.

    Returns
    -------
    None

    References
    ----------
    Borrowed From:
    https://gist.github.com/treuille/8b9cbfec270f7cda44c5fc398361b3b1
    """
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}"/>'
    st.write(html, unsafe_allow_html=True)


# @st_typed_cache_resource
def load_figure(saved_fig_path: str) -> Any:
    """Load the figure from the saved file"""
    with open(saved_fig_path, "rb") as f:
        fig = pickle.load(f)
    return fig


def figure_wrapper(fig_name: str, dataset_name: str = "boston_housing") -> callable:
    """
    A decorator function to handle the generation, saving, and loading of
    figures.

    This function takes a figure name and an optional dataset name (default is
    "boston_housing").
    It returns a decorator that can be used to wrap a function that generates
    a figure.

    The wrapped function should take a Pandas' DataFrame as input and return a
    matplotlib figure.

    The decorator handles the saving and loading of the figure. If the figure
    is already saved, it will be loaded from the saved file. Otherwise, the
    figure will be generated using the provided function and then saved for
    future use.

    Parameters
    ----------
    fig_name : str
        The name of the figure. This will be used as the filename when saving
        the figure.

    dataset_name : str, optional
        The name of the dataset. This is used to organize the saved figures by
        dataset.
        By default, "boston_housing" is used as the default directory.

    Returns
    -------
    callable
        A decorator function that can be used to wrap a function that generates
        a figure.
    """

    def decorator(func: callable) -> callable:
        """
        The actual decorator function.

        This function takes a function that generates a figure and returns a
        wrapped version of that function. The wrapped function takes a Pandas'
        DataFrame as input, generates a figure (or loads it from a saved file),
        and then displays the figure in Streamlit.

        Parameters
        ----------
        func : callable
            The function that generates a figure. It should take a Pandas'
            DataFrame as input and return a matplotlib figure.

        Returns
        -------
        callable
            The wrapped function.
        """

        def wrapper(dataset: pd.DataFrame) -> None:
            """
            The wrapped function.

            This function takes a Pandas' DataFrame as input, generates a
            figure (or loads it from a saved file), and then displays the
            figure in Streamlit.

            Parameters
            ----------
            dataset : pd.DataFrame
                The dataset to use for generating the figure.

            Returns
            -------
            None
            """
            # Define the path to the saved figure
            saved_fig_path = f"assets/{dataset_name}/{fig_name}.pkl"

            # Check if the figure is already saved
            if os.path.exists(saved_fig_path):
                fig = load_figure(saved_fig_path)
            else:
                # Generate the figure using the provided function
                fig = func(dataset)

                # Save the figure
                with open(saved_fig_path, "wb") as f:
                    pickle.dump(fig, f)

            # Display the figure in Streamlit
            if fig is not None:
                st.pyplot(fig, clear_figure=True)
            else:
                st.error("Error: Figure not generated.")

        return wrapper

    return decorator
