from pathlib import Path

import numpy as np
import pandas as pd

from shap_app.configs import settings
from shap_app.main import MAIN_DIR
from shap_app.pipelines.pipeline_utils import split_data_with_id_hash

DATA_SET = "boston_housing"

COLUMNS = [
    "CRIM",
    "ZN",
    "INDUS",
    "CHAS",
    "NOX",
    "RM",
    "AGE",
    "DIS",
    "RAD",
    "TAX",
    "PTRATIO",
    "B",
    "LSTAT",
]


def raw_boston_housing_summary_statistics() -> pd.DataFrame:
    """
    Return summary statistics for the raw Boston housing dataset.

    This function loads the Boston housing dataset and calculates the summary
    statistics including the count, mean, standard deviation, minimum, 25th
    percentile, median, 75th percentile, and maximum for each column. The
    result is returned as a pandas' DataFrame.

    Returns
    -------
    pd.DataFrame
        The Boston housing dataset summary statistics in the form of a pandas'
        DataFrame.
    """
    df = load_boston_housing_data()
    return df.describe()


def load_boston_housing_data() -> pd.DataFrame:
    """
    Load Boston Housing dataset.

    This function checks if the Boston Housing dataset is already present in
    the form of a CSV file. If not, it calls the function
    `_save_boston_housing_locally` to download the dataset and save it locally
    as a CSV file. Finally, it reads the CSV file and returns it as a pandas'
    DataFrame.

    Returns
    -------
    pd.DataFrame
        The Boston Housing dataset in the form of a pandas' DataFrame.
    """
    csv_path = Path(f"{MAIN_DIR}/{settings.DATASET_DIRECTORY}/{DATA_SET}/{DATA_SET}.csv")
    if not csv_path.is_file():
        _save_boston_housing_locally(csv_path)
    return pd.read_csv(csv_path)


def load_boston_housing_train_test(
    test_ratio: float = 0.2,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load Boston Housing training and test datasets.

    This function loads the Boston Housing dataset and splits it into training
    and test datasets based on the provided test_ratio. The datasets are saved
    locally as CSV files if they do not already exist. The function then reads
    the CSV files and returns them as pandas' DataFrames.

    Parameters
    ----------
    test_ratio : float, optional
        The ratio of the dataset to include in the test split. Default is 0.2.

    Returns
    -------
    tuple[pd.DataFrame, pd.DataFrame]
        The Boston Housing training and test datasets in the form of pandas'
        DataFrames.

    Raises
    ------
    ValueError
        If the test_ratio is not between 0 and 1.
    """
    if test_ratio < 0 or test_ratio > 1:
        raise ValueError(f"Test ratio must be between 0 and 1, got {test_ratio}.")
    train_ratio = 1 - test_ratio
    train_csv_path = Path(
        f"{MAIN_DIR}/{settings.DATASET_DIRECTORY}/{DATA_SET}/{DATA_SET}_train-{train_ratio:.2f}.csv"
    )
    test_csv_path = Path(
        f"{MAIN_DIR}/{settings.DATASET_DIRECTORY}/{DATA_SET}/{DATA_SET}_test-{test_ratio:.2f}.csv"
    )
    if not train_csv_path.is_file() or not test_csv_path.is_file():
        df = load_boston_housing_data()
        train, test = split_data_with_id_hash(df, test_ratio, "index")
        train.to_csv(train_csv_path, index=False)
        test.to_csv(test_csv_path, index=False)

    return pd.read_csv(train_csv_path), pd.read_csv(test_csv_path)


def _save_boston_housing_locally(csv_path: Path) -> None:
    """
    This function saves the Boston Housing dataset locally as a CSV file.

    The Boston Housing dataset is downloaded from the source and then saved
    locally in the specified path as a CSV file. This is done to facilitate
    faster loading of the dataset in future uses.

    Parameters
    ----------
    csv_path : Path
        The path where the Boston Housing dataset CSV file will be saved.
        This path should include the name of the file along with its extension (.csv).
    """
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep=r"\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    result = pd.DataFrame(data, columns=COLUMNS)
    result["TARGET"] = raw_df.values[1::2, 2]
    result.to_csv(csv_path, index=False)
