""" SHAP components for the webapp. """
from collections.abc import Callable
from typing import Any
from typing import TypeVar
from typing import cast

import numpy as np
import pandas as pd
import shap
import streamlit as st
from streamlit_shap import st_shap

shap.initjs()

F = TypeVar("F", bound=Callable[..., Any])


def st_typed_cache_resource(func: F) -> F:
    """Streamlit cache resource decorator for typed functions."""
    from streamlit import cache_resource

    return cast(F, cache_resource(func))


def st_typed_cache_data(func: F) -> F:
    """Streamlit cache data decorator for typed functions."""
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


def main_shap_plot(
    explainer: shap.TreeExplainer, shap_values: shap.Explanation, dataset: pd.DataFrame
) -> None:
    """
    Main SHAP plot

    Parameters
    ----------
    explainer : shap.TreeExplainer
        The shap explainer
    shap_values : shap.Explanation
        The shap values
    dataset : pd.DataFrame
        The dataset to use for the shap plot
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
        The interactive graph allows you to select your Y and X values,
        and dynamically generate plots to understand the model
        """
    )
