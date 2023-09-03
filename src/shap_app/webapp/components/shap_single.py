""" SHAP Single Component """
import matplotlib
import numpy as np
import pandas as pd
import shap
import streamlit as st
from matplotlib import pyplot as plt
from streamlit_shap import st_shap

from shap_app.webapp.chart_helpers import rerun_on_attribute_error

matplotlib.use("Agg")


def get_single_explanation(
    individual_shap_values: np.ndarray,
    dataset: pd.DataFrame,
    data_source: str | None = "boston_housing",
) -> pd.DataFrame:
    """
    Generate a DataFrame that provides an explanation of the SHAP values for a
    single observation.

    This function takes the SHAP values for a single observation, the dataset
    used for the SHAP plot, and the data source (default is "boston_housing").
    It returns a DataFrame that contains the SHAP values and their absolute
    values, sorted by the absolute values in descending order. If the data
    source is  "boston_housing", it also includes a column that provides a text
    explanation of the impact of the SHAP values on the median price.

    Parameters
    ----------
    individual_shap_values : np.ndarray
        The SHAP values for a single observation. These values indicate how
        much each feature in the observation contributes to the prediction.
    dataset : pd.DataFrame
        The dataset used for the SHAP plot. This dataset should include the
        features used in the model.
    data_source : str | None, optional
        The data source used for the SHAP plot. This is used to determine the
        text explanation for the impact of the SHAP values. By default, it is
        "boston_housing".

    Returns
    -------
    pd.DataFrame
        A DataFrame that contains the SHAP values and their absolute values,
        sorted by the absolute values in descending order. If the data source
        is "boston_housing", it also includes a column that provides a text
        explanation of the SHAP values on the median price.
    """
    df = pd.DataFrame(individual_shap_values, index=dataset.columns, columns=["SHAP Value"])
    df["Absolute_Values"] = df["SHAP Value"].abs()
    df.sort_values(by="Absolute_Values", ascending=False, inplace=True)

    if data_source == "boston_housing":

        def apply_text_explanation(shap_value: float) -> str:
            """Apply text explanation to shap value."""
            shap_value = shap_value * 1000
            if shap_value > 0:
                return (
                    f" has a positive impact, and "
                    f"increases the predicted value by $ {shap_value:.2f}"
                )
            else:
                return (
                    f" has a negative impact, and "
                    f"decreases the predicted value by -$ {abs(shap_value):.2f}"
                )

        df["SHAP Value Impact of the Median Price"] = df.index + df["SHAP Value"].apply(
            apply_text_explanation
        )
    else:
        raise ValueError(f"Unknown data source: {data_source}")

    return df


def individual_tree_shap_plots(
    dataset: pd.DataFrame,
    explainer: shap.TreeExplainer,
    shap_values: np.ndarray,
    shap_explanation: shap.Explanation,
    data_source: str | None = "boston_housing",
) -> None:
    """Create individual SHAP plot"""
    st.markdown(
        """
        **Base Value**: This is the average prediction of the
        model across all instances. In other words, it's what
        you would predict if you didn't know any features for
        the current output. It's the starting point of the plot.

        **SHAP Values**: Each feature used in the model is
        assigned a SHAP value. This value represents how much
        knowing that feature changes the output of the model
        for the instance in question. The SHAP value for a
        feature is proportional to the difference between the
        prediction for the instance and the base value, and
        it's allocated according to the contribution of each
        feature.

        **Color**: The features are color-coded based on their
        values for the specific instance. High values are shown
        in red, and low values are shown in blue. This provides
        a visual way to see which features are high or low for
        the given instance, and how that contributes to the
        prediction.

        **Position on the X-axis**: The position of a SHAP value
        on the X-axis shows whether the effect of that value is
        associated with a higher or lower prediction. If a
        feature's SHAP value is positioned to the right of the
        base value, it means that this feature increases the
        prediction; if it's to the left, it decreases the
        prediction.

        **Size of the SHAP Value**: The magnitude of a SHAP
        value tells you the importance of that feature in
        contributing to the difference between the actual
        prediction and the base value. Larger SHAP values
        (either positive or negative) have a bigger impact.
        """
    )

    max_value = dataset.shape[0]

    slider_value = st.slider(
        label="Select data point to visually inspect",
        min_value=1,
        max_value=max_value,
        value=100,
        key="individual_shap_values_slider",
        help="Slide to select number of observations to visually inspect",
    )

    # forced_plot = plt.gcf()

    st_shap(
        shap.force_plot(
            base_value=explainer.expected_value,
            shap_values=shap_values[slider_value, :],
            features=dataset.iloc[slider_value, :],
            feature_names=None,
            out_names=None,
            link="identity",
            plot_cmap="RdBu",
            matplotlib=False,
            show=True,
            figsize=(20, 3),
            ordering_keys=None,
            ordering_keys_time_format=None,
            text_rotation=0,
            contribution_threshold=0.05,
        )
    )

    # if forced_plot is not None:
    #     st.pyplot(forced_plot, clear_figure=True)

    st.markdown("### Waterfall SHAP Plot")

    waterfall_plot, explanation = st.columns(2, gap="medium")

    with waterfall_plot:
        st.markdown(
            """
            The waterfall plot shows how each feature in a given instance
            contributes to the final prediction. The plot is made of stacked
            bars, where each bar represents a feature value for a given
            instance. The height of the bar shows the SHAP value of that
            feature.
            """
        )
        rerun_on_attribute_error(plot_waterfall, shap_explanation, slider_value)

    with explanation:
        st.markdown(
            "The table below shows the change in the expected value for each "
            "feature in the selected instance, ordered by absolute value of the "
            "SHAP contribution. "
        )
        df = get_single_explanation(
            individual_shap_values=shap_values[slider_value, :],
            dataset=dataset,
            data_source=data_source,
        )
        column_to_use = (
            "SHAP Value Impact of the Median Price"
            if data_source == "boston_housing"
            else "SHAP Value "
        )
        # Convert the selected column to a list
        data_list = df[column_to_use].tolist()
        # Generate a markdown string with list items for each element in the list
        markdown_string = "\n".join([f"- {item}" for item in data_list])
        # Display the generated markdown string
        st.markdown("**SHAP Value Impact of the Median Price**")
        st.markdown(markdown_string)


def plot_waterfall(shap_explanation: shap.Explanation, slider_value: int) -> None:
    """
    Generate a waterfall plot for a given SHAP explanation and slider value.

    This function takes a SHAP explanation and a slider value as input and
    generates a waterfall plot. The waterfall plot visually represents the
    contribution of each feature to the final prediction for a specific
    instance.

    Each bar in the plot corresponds to a feature, and the height of the bar
    indicates the SHAP value of that feature. The SHAP values are calculated
    for the instance specified by the slider value.

    Parameters
    ----------
    shap_explanation : shap.Explanation
        The SHAP explanation object, which contains the SHAP values for all
        instances in the dataset.
    slider_value : int
        The slider value that specifies the instance for which the waterfall
        plot is generated.

    Returns
    -------
    None
    """
    # Generate the SHAP plot as HTML
    fig, axs = plt.subplots()
    shap.waterfall_plot(
        shap_values=shap_explanation[slider_value, :],
        max_display=30,
        show=False,
    )
    # Display the matplotlib figure in Streamlit
    waterfall_fig = plt.gcf()
    if waterfall_fig is not None:
        st.pyplot(waterfall_fig, clear_figure=True)

    st.markdown(
        "Where E[f(x)] is the Expected Value of the model output for the "
        "given input (i.e., f(x))."
    )
