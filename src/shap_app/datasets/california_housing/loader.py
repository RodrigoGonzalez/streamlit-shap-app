import shutil
import tarfile
from pathlib import Path

import pandas as pd

from shap_app.configs import settings
from shap_app.main import MAIN_DIR


def load_california_housing_data() -> pd.DataFrame:
    """
    Load California Housing data from a CSV file.

    This function checks if the California housing dataset is already present
    in the form of a CSV file. If not, it extracts the dataset from a tarball
    file and saves it as a CSV file for future use. Finally, it reads the CSV
    file and returns it as a pandas' DataFrame.

    Returns
    -------
    pd.DataFrame
        The California housing dataset in the form of a pandas' DataFrame.
    """
    dataset_path = Path(f"{MAIN_DIR}/{settings.DATASET_DIRECTORY}/california_housing")
    csv_path = Path(f"{dataset_path}/california_housing.csv")
    if not csv_path.is_file():
        tarball_path = Path(f"{dataset_path}/california_housing.tgz")
        with tarfile.open(tarball_path) as tar:
            tar.extractall(path=dataset_path)
        shutil.move(f"{dataset_path}/housing/housing.csv", csv_path)
    return pd.read_csv(csv_path)


def raw_california_housing_summary_statistics() -> pd.DataFrame:
    """
    Return summary statistics for the raw California housing dataset.

    This function loads the California housing dataset and calculates the
    summary statistics including the count, mean, standard deviation, minimum,
    25th percentile, median, 75th percentile, and maximum for each column. The
    result is returned as a pandas' DataFrame.

    Returns
    -------
    pd.DataFrame
        The summary statistics of the California housing dataset.
    """
    df = load_california_housing_data()
    return df.describe()


# def raw_california_housing_info() -> pd.DataFrame:
#     """Return summary statistics for the raw Boston housing dataset."""
#     df = load_california_housing_data()
#     return df.info()
