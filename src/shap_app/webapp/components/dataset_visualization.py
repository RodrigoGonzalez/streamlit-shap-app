import matplotlib.pyplot as plt
import pandas as pd
import shap
import streamlit as st
from streamlit_shap import st_shap

shap.initjs()
plt.style.use("ggplot")


def visualize_data_introduction() -> None:
    """Visualize data introduction"""
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

    Parameters
    ----------
    dataset : pd.DataFrame
        Dataset.
    """
    # TODO: Set number of bins based on number of observations
    dataset.hist(bins=50, figsize=(12, 12))
    st_shap(plot=None)
