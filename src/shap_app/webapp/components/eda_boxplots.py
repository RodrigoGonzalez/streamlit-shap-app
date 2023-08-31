import os

import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from matplotlib import pyplot as plt

from shap_app.webapp.chart_helpers import get_num_rows_for_figures


def box_plots_section(dataset: pd.DataFrame) -> None:
    """
    Display box plots for each feature in the dataset.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which the box plots are to be generated. Each column
        represents a feature and each row represents an observation.

    Returns
    -------
    None
    """
    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        box_plots_summary(dataset)
    with col2:
        create_visualization_box_plots(dataset)


def box_plots_summary(dataset: pd.DataFrame) -> None:
    """
    Display a summary of the box plots.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which the box plots are to be generated. Each column
        represents a feature and each row represents an observation.

    Returns
    -------
    None
    """
    st.markdown(
        """
        Box plots are a great way to visualize the distribution of a feature.
        They provide a quick and easy way to visualize the range, median,
        quartiles, and outliers in the data. The box represents the interquartile
        range (IQR), which is the range between the first and third quartiles.
        The line in the middle of the box represents the median. The whiskers
        represent the range of the data, excluding outliers. Outliers are
        represented by dots outside the whiskers.

        It looks like we have some outliers in the dataset. Let's take a closer
        look at them:
        """
    )
    # Calculate the number of outliers in each column
    outliers = calculate_outliers_using_iqr(dataset)
    outliers_percent = calculate_outliers_percent_from_outliers(dataset, outliers)

    # Display the outliers and also save outliers_percent in session state

    for k, percent in outliers_percent.items():
        if percent:
            st.markdown(f"- Column {k} percent outliers = {percent:.2f}%")

    st.session_state["outliers_percent"] = outliers_percent
    st.session_state["outliers_dict"] = outliers.to_dict()


def calculate_outliers_percent_from_outliers(
    dataset: pd.DataFrame, outliers: pd.Series
) -> pd.Series:
    """
    Calculate the percentage of outliers in each column of a dataset.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which the outliers are to be calculated. Each column
        represents a feature and each row represents an observation.
    outliers : pd.Series
        A Pandas' Series containing the number of outliers in each column of
        the dataset.

    Returns
    -------
    pd.Series
        A Pandas' Series containing the percentage of outliers in each column
        of the dataset.
    """
    return outliers * 100.0 / np.shape(dataset)[0]


def calculate_outliers_using_iqr(dataset: pd.DataFrame) -> pd.Series:
    """
    Calculate the number of outliers in each column of a dataset using the
    interquartile range (IQR) method.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which the outliers are to be calculated. Each column
        represents a feature and each row represents an observation.

    Returns
    -------
    pd.Series
        A Pandas' Series containing the number of outliers in each column of
        the dataset.
    """
    return dataset.apply(
        lambda x: (
            (x < (x.quantile(0.25) - 1.5 * (x.quantile(0.75) - x.quantile(0.25))))
            | (x > (x.quantile(0.75) + 1.5 * (x.quantile(0.75) - x.quantile(0.25))))
        ).sum()
    )


def create_visualization_box_plots(dataset: pd.DataFrame, fig_name: str = "box_plots") -> None:
    """
    Create box plots for each feature in the dataset.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which the box plots are to be generated. Each column
        represents a feature and each row represents an observation.
    fig_name : str, optional
        The name of the figure to save.
        Default is "box_plots".

    Returns
    -------
    None
    """
    image_file = f"assets/{fig_name}.png"

    if os.path.exists(image_file):
        st.image(
            image_file,
            caption="Box Plots of Each Feature",
            use_column_width=True,
        )

    else:
        # Create a new matplotlib figure
        fig, axs = plt.subplots(ncols=7, nrows=get_num_rows_for_figures(dataset), figsize=(20, 10))
        axs = axs.flatten()
        for index, (k, v) in enumerate(dataset.items()):
            sns.boxplot(y=k, data=dataset, ax=axs[index], palette="mako")
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)

        box_plot = plt.gcf()
        box_plot.savefig(image_file)
        st.pyplot(box_plot, clear_figure=True)

        st.markdown(
            "<h3 style='text-align: center;'>Box Plots of Each Feature</h3>", unsafe_allow_html=True
        )
