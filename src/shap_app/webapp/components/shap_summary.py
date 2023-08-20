import numpy as np
import pandas as pd
import shap
import streamlit as st
from streamlit_shap import st_shap

SUMMARY_PLOTS = {
    "Dot Plot": "dot",
    "Layered Violin Plot": "layered_violin",
    "Violin Plot": "violin",
}


def shap_feature_summary(dataset: pd.DataFrame, shap_values: np.ndarray) -> None:
    """
    Display SHAP feature importance.

    This function generates a SHAP summary plot and a SHAP dependence plot.
    The summary plot provides an overview of the most important features for
    the model, showing the SHAP values of every feature for every sample. The
    dependence plot shows how a single feature affects the output of the model,
    plotting the SHAP value of that feature versus its value for all the
    examples in the dataset.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset used to train the model. Each row represents a sample and
        each column represents a feature.
    shap_values : np.ndarray
        The SHAP values calculated for the model. Each row corresponds to a
        sample and each column corresponds to a feature. The SHAP values
        represent the contribution of each feature to the prediction for a
        sample.

    Returns
    -------
    None
    """
    st.markdown(
        "A SHAP value for a feature of a specific prediction represents how "
        "much the model prediction changes when we observe that feature. In the "
        "summary plot below we plot all the SHAP values for a single feature "
        "on a row, where the x-axis is the SHAP value "
        # "(which for this model is in units of log odds of winning)"
        ". By doing this for all features, we see which features drive the "
        "model’s prediction a lot, and which only effect the prediction a "
        "little. Note that when points don’t fit together on the line they "
        "pile up vertically to show density."
    )
    st.markdown("### SHAP Feature Impact")

    summary_plot, dependence_plot = st.columns(2)

    with summary_plot:
        st.markdown(
            "To get an overview of which features are most important for a model "
            "we can plot the SHAP values of every feature for every sample. The "
            "plot below sorts features by the sum of SHAP value magnitudes over "
            "all samples, and uses SHAP values to show the distribution of the "
            "impacts each feature has on the model output. The color represents "
            "the feature value (red high, blue low). This reveals for example that "
            "a high LSTAT (% lower status of the population) lowers the predicted "
            "home price."
        )
        button = st.radio(
            "Select the type of summary plot to display",
            SUMMARY_PLOTS.keys(),
            index=0,
            horizontal=True,
            key="summary_radio",
        )
        st_shap(
            shap.summary_plot(shap_values, dataset, plot_type=SUMMARY_PLOTS[button]),
            height=None,
            width=650,
        )

    with dependence_plot:
        feature = st.selectbox("Choose variable", dataset.columns)
        st.markdown(f"### {feature} importance on housing price")
        st.markdown(
            "To understand how a single feature effects the output of the model "
            "we can plot the SHAP value of that feature vs. the value of the "
            "feature for all the examples in a dataset. Since SHAP values "
            "represent a feature’s responsibility for a change in the model "
            "output, the plot below represents the change in predicted house "
            f"price as {feature} changes. Vertical dispersion at a single value of {feature} "
            "represents interaction effects with other features. To help reveal "
            "these interactions the dependence plot automatically selects another "
            "feature for coloring."
        )
        st_shap(shap.dependence_plot(feature, shap_values, dataset))
