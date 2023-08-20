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
    """Return summary statistics for the raw Boston housing dataset."""
    df = load_boston_housing_data()
    return df.describe()


def load_boston_housing_data() -> pd.DataFrame:
    """Load Boston data."""
    csv_path = Path(f"{MAIN_DIR}/{settings.DATASET_DIRECTORY}/{DATA_SET}/{DATA_SET}.csv")
    if not csv_path.is_file():
        _save_boston_housing_locally(csv_path)
    return pd.read_csv(csv_path)


def load_boston_housing_train_test(
    test_ratio: float = 0.2,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load Boston training and test data sets."""
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
    Saves the Boston dataset locally.

    Parameters
    ----------
    csv_path : Path
        Path to the csv file.
    """
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep=r"\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    result = pd.DataFrame(data, columns=COLUMNS)
    result["TARGET"] = raw_df.values[1::2, 2]
    result.to_csv(csv_path, index=False)
