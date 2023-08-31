""" Feature engineering functions for the web app. """
import numpy as np
import pandas as pd
from scipy import stats


def normalize_target_variable(
    df: pd.DataFrame, target_col: str, alpha: float = 0.05
) -> pd.DataFrame:
    """
    Normalize the target variable if it is not normally distributed.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the target column.
    target_col : str
        The name of the target column in the DataFrame.
    alpha : float, optional
        Significance level for the hypothesis test. Default is 0.05.

    Returns
    -------
    pd.DataFrame
        The DataFrame with the target column possibly transformed to be
        normally distributed.
    """
    # Validate that the target column exists in the DataFrame
    if target_col not in df.columns:
        raise ValueError(f"Target column {target_col} not found in DataFrame.")

    # Perform D'Agostino and Pearson's test
    stat, p = stats.normaltest(df[target_col])
    reject_null = p < alpha

    # If data is not normally distributed, apply transformation
    if reject_null:
        df[target_col] = np.log1p(df[target_col])

        # Re-run the test to confirm normality
        new_stat, new_p = stats.normaltest(df[target_col])
        new_reject_null = new_p < alpha

        if not new_reject_null:
            print("Data is now normally distributed.")
        else:
            print("Data is still not normally distributed after transformation.")
    else:
        print("Data is normally distributed.")

    return df


def perform_dagostino_pearson_test(df: pd.DataFrame, target_col: str, alpha: float = 0.05) -> dict:
    """
    Perform D'Agostino and Pearson's test to check for normality.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the target column.
    target_col : str
        The name of the target column in the DataFrame.
    alpha : float, optional
        Significance level for the hypothesis test. Default is 0.05.

    Returns
    -------
    dict
        A dictionary containing the test statistic, p-value, and whether to
        reject the null hypothesis.
    """
    # Validate that the target column exists in the DataFrame
    if target_col not in df.columns:
        raise ValueError(f"Target column {target_col} not found in DataFrame.")

    # Perform the test
    stat, p = stats.normaltest(df[target_col])

    # Interpretation
    reject_null = p < alpha

    return {"statistic": stat, "p_value": p, "reject_null": reject_null}


def remove_skew(df: pd.DataFrame, target_col: str, skew_threshold: float = 0.3) -> pd.DataFrame:
    """
    Remove skewness from the target and feature columns in a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing both features and target column.
    target_col : str
        The name of the target column in the DataFrame.
    skew_threshold : float, optional
        The skewness threshold above which the transformation will be applied.
        Default is 0.3.

    Returns
    -------
    pd.DataFrame
        The DataFrame with skewness removed from both features and target
        column.
    """
    # Validate that the target column exists in the DataFrame
    if target_col not in df.columns:
        raise ValueError(f"Target column {target_col} not found in DataFrame.")

    # Remove skewness from the target column
    if np.abs(df[target_col].skew()) > skew_threshold:
        df[target_col] = np.log1p(df[target_col])

    # Remove skewness from feature columns
    feature_cols = [col for col in df.columns if col != target_col]
    for col in feature_cols:
        if np.abs(df[col].skew()) > skew_threshold:
            df[col] = np.log1p(df[col])

    return df
