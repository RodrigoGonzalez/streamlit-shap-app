""" SHAP components for the webapp. """
from collections.abc import Callable
from typing import Any
from typing import TypeVar
from typing import cast

import matplotlib
import numpy as np
import pandas as pd
import shap
import streamlit as st
from streamlit_shap import st_shap

matplotlib.use("Agg")


F = TypeVar("F", bound=Callable[..., Any])


def st_typed_cache_resource(func: F) -> F:
    """
    A decorator for caching resources in Streamlit applications with type
    annotations.

    This function is a wrapper around Streamlit's cache_resource function,
    which allows for caching of resources in Streamlit applications. The
    decorator is designed to work with functions that have type annotations,
    ensuring that the cached resources are of the correct type.

    Parameters
    ----------
    func : Callable[..., Any]
        The function whose output is to be cached. This function should have
        type annotations for all its parameters and its return value.

    Returns
    -------
    Callable[..., Any]
        The same function passed in `func`, but now its output is cached by
        Streamlit.
    """
    from streamlit import cache_resource

    return cast(F, cache_resource(func))


def st_typed_cache_data(func: F) -> F:
    """
    A decorator for caching data in Streamlit applications with type
    annotations.

    This function is a wrapper around Streamlit's cache_data function, which
    allows for caching of data in Streamlit applications. The decorator is
    designed to work with functions that have type annotations, ensuring that
    the cached data are of the correct type.

    Parameters
    ----------
    func : Callable[..., Any]
        The function whose output is to be cached. This function should have
        type annotations for all its parameters and its return value.

    Returns
    -------
    Callable[..., Any]
        The same function passed in `func`, but now its output is cached by
        Streamlit.
    """
    from streamlit import cache_data

    return cast(F, cache_data(func))


def tree_shap_components_loader(
    *,
    model_path: str | None = None,
    model: object | None = None,
    dataset: str | pd.DataFrame = "boston_housing",
) -> tuple[shap.TreeExplainer, shap.Explanation, np.ndarray]:
    """
    Loads the model and data and returns the shap components.

    Parameters
    ----------
    model_path : str | None, optional
        Path to the pickle file, by default None
    model : object | None, optional
        The deserialized model object, by default None
    dataset : str | pd.DataFrame, optional
        The dataset to use, by default "boston_housing"

    Returns
    -------
    tuple[shap.TreeExplainer, shap.Explanation, np.ndarray]
        The shap components.
    """

    if model_path is None and model is None:
        raise ValueError("Either model_path or model must be provided.")
    if model_path is not None and model is not None:
        raise ValueError("Only one of model_path or model must be provided.")

    # Load the model if needed
    if model_path is not None:
        from shap_app.webapp.components.loaders import load_model

        model = load_model(model_path)

    # Load the dataset
    if dataset is None:
        raise ValueError("dataset must be provided.")
    if isinstance(dataset, str):
        from shap_app.webapp.components.loaders import load_data

        dataset = load_data(dataset)

    explainer = shap.TreeExplainer(model)
    shap_explanation = explainer(dataset)
    shap_values = explainer.shap_values(dataset)

    return explainer, shap_explanation, shap_values


def main_shap_plot() -> None:
    """
    Generate the main SHAP plot for the given dataset and SHAP values.

    This function uses the provided SHAP explainer and SHAP values to generate
    a SHAP plot for the given dataset. The SHAP plot visualizes the
    contribution of each feature to the prediction for each sample in the
    dataset.

    Returns
    -------
    None
    """
    st.markdown(
        """
        ### SHAP Library

        The SHAP library is a Python library that allows us to explain
        how a model works. The library is based on the idea of
        [Shapley Values](https://en.wikipedia.org/wiki/Shapley_value) from
        game theory. The library is model agnostic, meaning it can be used
        to explain any model.
        """
    )

    st_shap(
        shap.force_plot(
            base_value=st.session_state["explainer"].expected_value,
            shap_values=st.session_state["shap_values"],
            features=st.session_state["X"],
            feature_names=None,
            out_names=None,
            link="identity",
            plot_cmap="RdBu",
            matplotlib=False,
            show=True,
            figsize=(20, 3),
            ordering_keys=None,
            ordering_keys_time_format=None,
            text_rotation=0,
            contribution_threshold=0.05,
        ),
        height=500,
    )
    st.markdown(
        """
        The interactive graph provided here allows you to select specific Y and X values,
        and dynamically generate plots. This feature aids in understanding the underlying
        model by visualizing the relationships between variables and their impact on the
        model's predictions. By interacting with the graph, you can gain insights into
        how changes in the input variables influence the output, thereby providing a
        deeper understanding of the model's behavior.
        """
    )
