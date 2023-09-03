""" Helper functions for charts in the webapp. """
from __future__ import annotations

from collections.abc import Callable
from typing import Any

import pandas as pd


def rerun_on_attribute_error(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """
    Executes the given function and reruns it once if an AttributeError is
    caught.

    Example usage

    def example_function(x):
    return x.attribute_that_does_not_exist

    result = rerun_on_attribute_error(example_function, "some_value")


    Parameters
    ----------
    func : Callable[..., Any]
        The function to be executed.
    args : Any
        Positional arguments to pass to `func`.
    kwargs : Any
        Keyword arguments to pass to `func`.

    Returns
    -------
    Any
        The result of the function execution.

    Raises
    ------
    Exception
        Propagates any exception other than AttributeError raised during
        function execution.
    """

    try:
        return func(*args, **kwargs)
    except AttributeError:
        print("AttributeError caught. Rerunning the function...")
        return func(*args, **kwargs)
    except Exception as e:
        print(f"An exception of type {type(e).__name__} occurred. Arguments:\n{e.args}")
        raise


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
