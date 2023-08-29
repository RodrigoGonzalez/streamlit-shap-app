import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

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
        ### Univariate Analysis

        We start by visualizing each feature in the dataset. This helps us
        understand the distribution of each feature and identify any outliers
        or anomalies. We can also use this information to determine whether
        we need to transform the data to make it more suitable for modeling.

        #### Box Plots
        """
    )

    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        st.markdown(
            """
            Box plots are a great way to visualize the distribution of a feature.
            They provide a quick and easy way to visualize the range, median,
            quartiles, and outliers in the data. The box represents the inter-quartile
            range (IQR), which is the range between the first and third quartiles.
            The line in the middle of the box represents the median. The whiskers
            represent the range of the data, excluding outliers. Outliers are
            represented by dots outside the whiskers.

            It looks like we have some outliers in the dataset. Let's take a closer
            look at them:
            """
        )

        outliers = dataset.apply(
            lambda x: (
                (x < (x.quantile(0.25) - 1.5 * (x.quantile(0.75) - x.quantile(0.25))))
                | (x > (x.quantile(0.75) + 1.5 * (x.quantile(0.75) - x.quantile(0.25))))
            ).sum()
        )
        outliers_percent = outliers * 100.0 / np.shape(dataset)[0]
        for k, percent in outliers_percent.items():
            if percent:
                st.markdown(f"- Column {k} percent outliers = {percent:.2f}%")

    with col2:
        _create_visualization_box_plots(dataset)

    st.markdown(
        """
        #### Histograms and KDE Plots
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
        _create_visualization_histogram_plots(dataset)


def _create_visualization_box_plots(dataset: pd.DataFrame) -> None:
    # Create a new matplotlib figure
    fig, axs = plt.subplots(ncols=7, nrows=_get_num_rows_for_figures(dataset), figsize=(20, 10))
    axs = axs.flatten()
    for index, (k, v) in enumerate(dataset.items()):
        sns.boxplot(y=k, data=dataset, ax=axs[index], palette="mako")
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
    st.pyplot(fig, clear_figure=True)
    st.markdown(
        "<h3 style='text-align: center;'>Box Plots of Each Feature</h3>", unsafe_allow_html=True
    )


def _create_visualization_histogram_plots(dataset: pd.DataFrame) -> None:
    fig, axs = plt.subplots(ncols=7, nrows=_get_num_rows_for_figures(dataset), figsize=(20, 10))
    axs = axs.ravel()
    for index, column in enumerate(dataset.columns):
        sns.histplot(dataset[column], ax=axs[index], kde=True, color="#003153")
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=5.0)
    st.pyplot(fig, clear_figure=True)
    st.markdown(
        "<h3 style='text-align: center;'>Histograms of Each Feature with KDE Plots</h3>",
        unsafe_allow_html=True,
    )


def _get_num_rows_for_figures(dataset: pd.DataFrame) -> int:
    n_rows = dataset.shape[1] // 7
    if dataset.shape[1] % 7 != 0:
        n_rows += 1

    return n_rows


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
