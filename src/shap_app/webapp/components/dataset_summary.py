import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

plt.style.use("ggplot")


def raw_dataset_summary(dataset: pd.DataFrame) -> None:
    """
    Display the summary statistics and data dictionary of the given dataset.

    This function takes a pandas' DataFrame as input and displays the summary
    statistics and data dictionary of the dataset. The summary statistics
    include count, mean, standard deviation, minimum, 25th percentile, median,
    75th percentile, and maximum of each feature in the dataset. The data
    dictionary provides detailed information about the dataset including the
    description of each feature, their data types, and other relevant details.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which the summary statistics and data dictionary are
        to be displayed.

    Returns
    -------
    None
        This function does not return any value. It displays the summary
        statistics and data dictionary of the dataset.
    """
    max_value = dataset.shape[0]
    slider_value_summary = st.slider(
        label="Select number of observations to visually inspect",
        min_value=1,
        max_value=max_value,
        value=20,
        key="data_summary_slider",
        help="Slide to select number of observations to visually inspect",
    )
    # Display data
    st.dataframe(dataset.head(slider_value_summary))

    # Conditionally calculate summary statistics
    if st.checkbox("Display summary statistics for visible sample?"):
        st.markdown(f"""Sample statistics based on {slider_value_summary} observations:""")
        df_describe = dataset.head(slider_value_summary).describe()
        # df_describe = df_describe.append(
        #     dataset.head(slider_value_summary).agg(['skew', 'kurtosis'])
        # )
        st.dataframe(df_describe)
