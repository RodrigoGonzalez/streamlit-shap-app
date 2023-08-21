""" Dataset Loaders for the SHAP App. """
import pandas as pd

from shap_app.datasets.boston_housing.loader import load_boston_housing_data
from shap_app.datasets.california_housing.loader import load_california_housing_data


def load_full_dataset(dataset_name: str = "boston_housing") -> pd.DataFrame:
    """
    Load and return the specified dataset.

    This function loads the specified dataset and returns it as a pandas'
    DataFrame. The dataset is loaded from the local directory if it exists,
    otherwise it is downloaded from the source. Currently, this function
    supports the loading of 'boston_housing' and 'california_housing' datasets.

    Parameters
    ----------
    dataset_name : str, optional
        The name of the dataset to load. Default is 'boston_housing'.

    Returns
    -------
    pd.DataFrame
        The loaded dataset in the form of a pandas' DataFrame.

    Raises
    ------
    ValueError
        If the specified dataset is not supported.
    """
    if dataset_name == "boston_housing":
        return load_boston_housing_data()
    elif dataset_name == "california_housing":
        return load_california_housing_data()
    raise ValueError(f"Unknown dataset: {dataset_name}")
