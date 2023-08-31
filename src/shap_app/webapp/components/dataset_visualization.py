from copy import deepcopy

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

from shap_app.webapp.components.eda_boxplots import box_plots_section
from shap_app.webapp.components.eda_histograms import histograms_and_kde_plots
from shap_app.webapp.components.outliers import introduction_to_techniques_to_remove_outliers
from shap_app.webapp.components.outliers import remove_outliers_percentile
from shap_app.webapp.components.outliers import remove_outliers_robust_z_score

plt.style.use("ggplot")
sns.set_theme(style="whitegrid")


def visualize_data_introduction(dataset: pd.DataFrame) -> None:
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

    st.markdown(
        """
        ## Univariate Analysis

        We start by visualizing each feature in the dataset. This helps us
        understand the distribution of each feature and identify any outliers
        or anomalies. We can also use this information to determine whether
        we need to transform the data to make it more suitable for modeling.

        ### Box Plots
        """
    )

    box_plots_section(st.session_state["df"])

    st.markdown("---")

    introduction_to_techniques_to_remove_outliers()

    if st.session_state["outliers_dict"]["TARGET"] >= 0:
        remove_target_outliers()

    st.markdown("---")

    histograms_and_kde_plots(st.session_state["df_masked"])


def remove_target_outliers() -> None:
    """
    Remove outliers in the target column.
    """
    threshold = remove_outliers_percentile(st.session_state["df"], "TARGET", 0.05, "upper")
    st.markdown(
        f"""
            #### Remove Target Outliers

            We can remove the outliers in the target column by filtering the
            dataset to only include rows where we use a robust z-score and a
            Z-score threshold of {threshold:.2f} (so as to remove a maximum of
            about 5% of the data. This will help us better visualize the
            distribution of the rest of the data.
            """
    )
    mask = remove_outliers_robust_z_score(st.session_state["df"], "TARGET", threshold, "upper")
    df = deepcopy(st.session_state["df"])
    st.session_state["df_masked"] = df[mask]


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

    # Create a new matplotlib figure
    fig, ax = plt.subplots()

    # Generate the SHAP dependence plot
    num_bins = int(np.sqrt(dataset.shape[0]))
    dataset.hist(bins=num_bins, figsize=(12, 12), ax=ax)

    # Display the matplotlib figure in Streamlit
    st.pyplot(fig, clear_figure=True)

    # st_shap(plot=None)
