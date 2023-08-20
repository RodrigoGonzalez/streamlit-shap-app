""" Components for displaying dataset information. """
from collections.abc import Callable
from typing import Any
from typing import TypeVar
from typing import cast

import pandas as pd

F = TypeVar("F", bound=Callable[..., Any])


def st_typed_cache_data(func: F) -> F:
    """Streamlit cache data decorator for typed functions."""
    from streamlit import cache_data

    return cast(F, cache_data(func))


@st_typed_cache_data
def data_dictionary(dataset: str = "boston_housing") -> str:
    """
    Display data dictionary for specified dataset.

    Parameters
    ----------
    dataset : str
        Dataset name.

    Returns
    -------
    str
        Data dictionary.
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
    Return summary statistics for the specified dataset.

    Parameters
    ----------
    dataset : str
        Dataset name.

    Returns
    -------
    pd.DataFrame
        Summary statistics.
    """
    if dataset == "boston_housing":
        from shap_app.datasets.boston_housing.loader import raw_boston_housing_summary_statistics

        return raw_boston_housing_summary_statistics()
    elif dataset == "california_housing":
        from shap_app.datasets.california_housing import raw_california_housing_summary_statistics

        return raw_california_housing_summary_statistics()
    else:
        raise ValueError(f"Dataset {dataset} summary statistics not found.")
