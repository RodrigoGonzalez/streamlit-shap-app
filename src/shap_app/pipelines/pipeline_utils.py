""" Utility functions for the pipelines. """
from pathlib import Path
from zlib import crc32

import numpy as np
import pandas as pd
from strictyaml import YAML
from strictyaml import load

from shap_app.configs import settings
from shap_app.main import MAIN_DIR


def is_id_in_test_set(identifier: int, test_ratio: float) -> bool:
    """
    Returns True if the last byte of the hash of the identifier is lower
    than or equal to 256 * test_ratio.

    Parameters
    ----------
    identifier : int
        The identifier to hash.
    test_ratio : float
        The ratio of the test set.

    Returns
    -------
    bool
        True if the last byte of the hash of the identifier is lower
        than or equal to 256 * test_ratio.
    """
    return crc32(np.int64(identifier)) < test_ratio * 2**32


def split_data_with_id_hash(
    data: pd.DataFrame, test_ratio: float, id_column: str
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split data into train and test sets.

    Parameters
    ----------
    data : pd.DataFrame
        The data to split.
    test_ratio : float
        The ratio of the test set.
    id_column : str
        The name of the column containing the identifier.

    Returns
    -------
    tuple[pd.DataFrame, pd.DataFrame]
        The train and test sets.
    """
    if id_column not in data.columns and id_column != "index":
        raise ValueError(f"Column {id_column} not found in data.")
    if id_column == "index" and "index" not in data.columns:
        data.reset_index(inplace=True)
    if test_ratio < 0 or test_ratio > 1:
        raise ValueError(f"Test ratio must be between 0 and 1, got {test_ratio}.")

    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))

    if id_column == "index":
        data.drop(id_column, axis=1, inplace=True)
    return data.loc[~in_test_set], data.loc[in_test_set]


def fetch_dataset_card(
    dataset_card_path: Path | None = None, dataset_name: str | None = "boston_housing"
) -> YAML:
    """Parse YAML containing the package configuration."""
    if not dataset_card_path:
        dataset_card_path = Path(
            f"{MAIN_DIR}/{settings.DATASET_DIRECTORY}/{dataset_name}/datasetcard.yml"
        )
    if dataset_card_path:
        with open(dataset_card_path) as conf_file:
            return load(conf_file.read())

    raise OSError(f"Did not find config file at path: {dataset_card_path}")
