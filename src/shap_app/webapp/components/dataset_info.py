""" Components for displaying dataset information. """
from collections.abc import Callable
from typing import Any
from typing import TypeVar
from typing import cast

import pandas as pd

F = TypeVar("F", bound=Callable[..., Any])


def st_typed_cache_data(func: F) -> F:
    """
    Streamlit cache data decorator for typed functions.

    This decorator is used to cache the results of a function call in
    Streamlit. It is specifically designed for functions with typed arguments,
    ensuring that the cache is correctly invalidated when the types of the
    arguments change.

    Parameters
    ----------
    func : Callable[..., Any]
        The function whose results should be cached.

    Returns
    -------
    Callable[..., Any]
        The decorated function, which will have its results cached.
    """
    from streamlit import cache_data

    return cast(F, cache_data(func))


@st_typed_cache_data
def data_dictionary(dataset: str = "boston_housing") -> str:
    """
    Retrieve the data dictionary for a specified dataset.

    This function fetches the data dictionary associated with a given dataset.
    The data dictionary provides detailed information about the dataset
    including the description of each feature, their data types, and other
    relevant details.

    Parameters
    ----------
    dataset : str, optional
        The name of the dataset for which the data dictionary is to be fetched.
        The default dataset is "boston_housing".

    Returns
    -------
    str
        A string representation of the data dictionary associated with the
        specified dataset.

    Raises
    ------
    ValueError
        If the specified dataset does not have an associated data dictionary.
    """
    if dataset == "boston_housing":
        from shap_app.datasets.boston_housing.data_dictionary import boston_housing_data_dictionary

        return boston_housing_data_dictionary()
    elif dataset == "california_housing":
        from shap_app.datasets.california_housing import california_housing_data_dictionary

        return california_housing_data_dictionary()
    else:
        raise ValueError(f"Dataset {dataset} data dictionary not found.")


@st_typed_cache_data
def summary_statistics(dataset: str = "boston_housing") -> pd.DataFrame:
    """
    Compute and return summary statistics for a specified dataset.

    This function calculates summary statistics for a given dataset. The
    summary statistics include count, mean, standard deviation, minimum, 25th
    percentile, median, 75th percentile, and maximum of each feature in the
    dataset.

    Parameters
    ----------
    dataset : str, optional
        The name of the dataset for which the summary statistics are to be
        computed. The default dataset is "boston_housing".

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the summary statistics of each feature in the
        specified dataset. Each row represents a feature and the columns
        represent the count, mean, standard deviation, minimum, 25th
        percentile, median, 75th percentile, and maximum.

    Raises
    ------
    ValueError
        If the specified dataset does not exist or summary statistics cannot
        be computed.
    """
    if dataset == "boston_housing":
        from shap_app.datasets.boston_housing.loader import raw_boston_housing_summary_statistics

        return raw_boston_housing_summary_statistics()
    elif dataset == "california_housing":
        from shap_app.datasets.california_housing import raw_california_housing_summary_statistics

        return raw_california_housing_summary_statistics()
    else:
        raise ValueError(f"Dataset {dataset} summary statistics not found.")
