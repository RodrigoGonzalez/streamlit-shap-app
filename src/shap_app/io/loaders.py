""" Dataset Loaders for the SHAP App. """
import pandas as pd

from shap_app.datasets.boston_housing.loader import load_boston_housing_data
from shap_app.datasets.california_housing.loader import load_california_housing_data


def load_full_dataset(dataset_name: str = "boston_housing") -> pd.DataFrame:
    """
    Loads and returns the dataset.
    Parameters
    ----------
    dataset_name : str
        The Dataset to load.

    Returns
    -------
    pd.DataFrame
        The dataset.
    """
    if dataset_name == "boston_housing":
        return load_boston_housing_data()
    elif dataset_name == "california_housing":
        return load_california_housing_data()
    raise ValueError(f"Unknown dataset: {dataset_name}")
