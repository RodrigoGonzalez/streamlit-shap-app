""" This module contains functions for loading the model and data. """
import os
import pickle
from collections.abc import Callable
from typing import Any
from typing import TypeVar
from typing import cast

import pandas as pd

from shap_app.io.loaders import load_full_dataset

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


def st_typed_cache_data(func: F) -> F:
    """
    This is a decorator for Streamlit cache data. It is used to cache the
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
    from streamlit import cache_data

    return cast(F, cache_data(func))


@st_typed_cache_resource
def load_model(model_path: str) -> object:
    """
    Load a model from a pickle file.

    This function uses the Python pickle module to deserialize a model object
    from a file. The file is expected to be a pickle file, which is a binary
    file format used by Python for serializing and deserializing Python object
    structures.

    The function is decorated with the `st_typed_cache_resource` decorator,
    which caches the output of the function in Streamlit. This is useful for
    computationally expensive operations, such as loading a large model, as it
    allows the result to be stored and reused across multiple runs of the
    script, rather than being recomputed each time.

    Parameters
    ----------
    model_path : str
        The path to the pickle file containing the serialized model. This
        should be a string representing a valid file path on the system where
        the script is being run.

    Returns
    -------
    object
        The deserialized model object. The exact type of this object will
        depend on the type of the model that was serialized into the pickle
        file. It could be any type of Python object that is capable of being
        pickled, but in the context of this function it is expected to be a
        machine learning model object of some kind.
    """
    return pickle.load(open(model_path, "rb"))


@st_typed_cache_data
def load_data(dataset: str = "boston_housing") -> pd.DataFrame:
    """
    Load a dataset using the shap library. By default, the Boston Housing
    dataset is loaded. This function can also load a dataset from a CSV file
    if a valid file path is provided instead of a dataset name.

    This function is decorated with the `st_typed_cache_data` decorator, which
    caches the output of the function in Streamlit. This is useful for
    computationally expensive operations, such as loading a large dataset, as
    it allows the result to be stored and reused across multiple runs of the
    script, rather than being recomputed each time.

    Parameters
    ----------
    dataset : str, optional
        The name of the dataset to load or the path to a CSV file. If not
        provided, the Boston Housing dataset is loaded by default.

    Returns
    -------
    pd.DataFrame
        The loaded dataset as a Panda's DataFrame.
    """
    # Check if the dataset is a file path
    if os.path.isfile(dataset):
        return pd.read_csv(dataset)

    # Check if the dataset is a known dataset name
    known_datasets = ["boston_housing", "california_housing"]
    if dataset in known_datasets:
        return load_full_dataset(dataset)

    raise ValueError(f"Unknown dataset: {dataset}")
