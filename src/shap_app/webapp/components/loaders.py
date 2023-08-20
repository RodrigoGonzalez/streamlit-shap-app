""" This module contains functions for loading the model and data. """
import pickle
from collections.abc import Callable
from typing import Any
from typing import TypeVar
from typing import cast

import pandas as pd

from shap_app.io.loaders import load_full_dataset

F = TypeVar("F", bound=Callable[..., Any])


def st_typed_cache_resource(func: F) -> F:
    """Streamlit cache resource decorator for typed functions."""
    from streamlit import cache_resource

    return cast(F, cache_resource(func))


def st_typed_cache_data(func: F) -> F:
    """Streamlit cache data decorator for typed functions."""
    from streamlit import cache_data

    return cast(F, cache_data(func))


@st_typed_cache_resource
def load_model(model_path: str) -> object:
    """

    Parameters
    ----------
    model_path : str
        Path to the pickle file.

    Returns
    -------
    object
        The deserialized model object.
    """
    return pickle.load(open(model_path, "rb"))


@st_typed_cache_data
def load_data(dataset_name: str = "boston_housing") -> pd.DataFrame:
    """
    Loads and returns the Boston dataset using the shap library.

    Returns
    -------
    tuple of numpy arrays
        The Boston dataset.
    """
    # data = load_full_dataset(dataset_name)
    # data.drop("TARGET", axis=1, inplace=True)
    # return data
    return load_full_dataset(dataset_name)
