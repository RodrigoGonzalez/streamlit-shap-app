import os

import pandas as pd
import seaborn as sns
import streamlit as st
from matplotlib import pyplot as plt

from shap_app.webapp.chart_helpers import get_num_rows_for_figures


def histograms_and_kde_plots(dataset: pd.DataFrame) -> None:
    """
    Display histograms and KDE plots for each feature in the dataset.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which the histograms and KDE plots are to be generated.
        Each column represents a feature and each row represents an observation.

    Returns
    -------
    None
    """
    st.markdown(
        """
        ### Histograms and KDE Plots
        """
    )
    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.markdown(
            """
            Histograms are a powerful tool for visualizing the distribution of a
            feature. They provide a visual representation of data by dividing the
            entire range of values into a series of intervals (or 'bins') and then
            count how many values fall into each bin. This gives us a sense of the
            data's underlying frequency distribution, including the range, median,
            quartiles, and outliers.

            KDE (Kernel Density Estimation) plots are a statistical technique for
            smoothing a histogram to create a continuous curve. They provide a more
            refined view of the data distribution. KDE plots estimate the probability
            density function of a random variable, which helps in identifying the
            shape of the distribution and the values where data points are more likely
            to occur. Like histograms, KDE plots can also help visualize the range,
            median, quartiles, and outliers in the data.
            """
        )
    with col2:
        create_visualization_histogram_plots(dataset)


def create_visualization_histogram_plots(
    dataset: pd.DataFrame, fig_name: str = "histogram_plots"
) -> None:
    """
    Create histograms and KDE plots for each feature in the dataset.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which the histograms and KDE plots are to be generated.
    fig_name : str, optional
        The name of the figure to save.
        Default is "histogram_plots".

    Returns
    -------
    None
    """
    image_file = f"assets/{fig_name}.png"

    if os.path.exists(image_file):
        st.image(
            image_file,
            caption=("Histograms of Each Feature with KDE Plots"),
            use_column_width=True,
        )

    else:
        fig, axs = plt.subplots(ncols=7, nrows=get_num_rows_for_figures(dataset), figsize=(20, 10))
        axs = axs.ravel()
        for index, column in enumerate(dataset.columns):
            sns.histplot(dataset[column], ax=axs[index], kde=True, color="#003153")
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)

        histogram_plot = plt.gcf()
        histogram_plot.savefig(image_file)
        st.pyplot(histogram_plot, clear_figure=True)

        st.markdown(
            "<h3 style='text-align: center;'>Histograms of Each Feature with KDE Plots</h3>",
            unsafe_allow_html=True,
        )
