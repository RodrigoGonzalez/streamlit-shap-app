import shutil
import tarfile
from pathlib import Path

import pandas as pd

from shap_app.configs import settings
from shap_app.main import MAIN_DIR


def load_california_housing_data() -> pd.DataFrame:
    """Load California Housing data."""
    dataset_path = Path(f"{MAIN_DIR}/{settings.DATASET_DIRECTORY}/california_housing")
    csv_path = Path(f"{dataset_path}/california_housing.csv")
    if not csv_path.is_file():
        tarball_path = Path(f"{dataset_path}/california_housing.tgz")
        with tarfile.open(tarball_path) as tar:
            tar.extractall(path=dataset_path)
        shutil.move(f"{dataset_path}/housing/housing.csv", csv_path)
    return pd.read_csv(csv_path)


def raw_california_housing_summary_statistics() -> pd.DataFrame:
    """Return summary statistics for the raw Boston housing dataset."""
    df = load_california_housing_data()
    return df.describe()


# def raw_california_housing_info() -> pd.DataFrame:
#     """Return summary statistics for the raw Boston housing dataset."""
#     df = load_california_housing_data()
#     return df.info()
