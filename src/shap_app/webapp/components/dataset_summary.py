import matplotlib.pyplot as plt
import pandas as pd
import shap
import streamlit as st

shap.initjs()
plt.style.use("ggplot")


def raw_dataset_summary(dataset: pd.DataFrame) -> None:
    """
    Display dataset summary statistics and data dictionary.

    Parameters
    ----------
    dataset : pd.DataFrame
        Dataset.
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
