import pandas as pd


def get_num_rows_for_figures(dataset: pd.DataFrame, figs_per_row: int = 7) -> int:
    """
    Calculate the number of rows required to display the figures for a dataset.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which the number of rows is to be calculated. Each
        column represents a feature and each row represents an observation.
    figs_per_row : int, optional
        The number of figures to display per row, by default 7.

    Returns
    -------
    int
    """
    n_rows = dataset.shape[1] // figs_per_row
    if dataset.shape[1] % figs_per_row != 0:
        n_rows += 1

    return n_rows
