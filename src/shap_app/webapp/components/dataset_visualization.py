import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap
import streamlit as st
from streamlit_shap import st_shap

shap.initjs()
plt.style.use("ggplot")


def visualize_data_introduction() -> None:
    """
    Provide an introduction to the data visualization process.

    This function displays an introductory Markdown text that explains the
    importance and purpose of data visualization in the exploratory phase of
    data analysis. It emphasizes the role of visualization in identifying
    patterns, anomalies, trends, correlations, and outliers in the dataset,
    which can guide subsequent modeling and validate the appropriateness of
    the data for the chosen model.

    Returns
    -------
    None
        This function does not return any value. It displays an introductory
        text about data visualization.
    """
    st.markdown(
        "Here we delve into the exploratory phase of our data analysis. "
        "This crucial step involves a deep dive into the dataset, where we uncover "
        "patterns, spot anomalies, test hypotheses, and check assumptions with the "
        "help of summary statistics and graphical representations. Visualization "
        "is a powerful tool that aids in understanding complex data sets. By "
        "creating charts, graphs, and other visual depictions of data, we can more "
        "easily identify trends, correlations, and outliers that might not be "
        "apparent from looking at raw data alone. This process not only provides "
        "valuable insights that can guide the subsequent modeling but also helps "
        "us validate the appropriateness of our data for the chosen model. This "
        "stage is about transforming our data from a raw form into knowledge and "
        "insights, setting the stage for further analysis and predictive modeling."
    )


def raw_dataset_insights(dataset: pd.DataFrame) -> None:
    """
    Display dataset summary statistics and data dictionary.

    This function takes a pandas' DataFrame as input and generates a histogram
    for each column in the DataFrame. The number of bins for the histogram is
    determined by the square root of the rows in the DataFrame. The histograms
    provide a visual representation of the data distribution for each feature
    in the dataset.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which the histograms are to be generated. Each column
        represents a feature and each row represents an observation.

    Returns
    -------
    None
        This function does not return any value. It generates and displays
        histograms for each feature in the dataset.
    """
    num_bins = int(np.sqrt(dataset.shape[0]))
    dataset.hist(bins=num_bins, figsize=(12, 12))
    st_shap(plot=None)
