import os

import matplotlib
import numpy as np
import pandas as pd
import shap
import streamlit as st
from matplotlib import pyplot as plt

matplotlib.use("Agg")

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
        _generate_shap_summary_plot(dataset, shap_values)

    with dependence_plot:
        generate_shap_dependence_plot(dataset, shap_values)


def _generate_shap_summary_plot(dataset: pd.DataFrame, shap_values: np.ndarray) -> None:
    """
    Generate a SHAP summary plot.

    This function generates a SHAP summary plot which provides an overview of
    the most important features for the model. It shows the SHAP values of
    every feature for every sample. The plot sorts features by the sum of SHAP
    value magnitudes over all samples, and uses SHAP values to show the
    distribution of the impacts each feature has on the model output. The color
    represents the feature value (red high, blue low).

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
        (
            "Select the type of summary plot to display. Click on the "
            "figure for an enlarged view."
        ),
        SUMMARY_PLOTS.keys(),
        index=0,
        horizontal=True,
        key="summary_radio",
    )

    generate_shap_summary_plot(button, dataset, shap_values)


def generate_shap_summary_plot(
    button: str,
    dataset: pd.DataFrame,
    shap_values: np.ndarray,
    base_fig_name: str = "shap_summary_plot",
) -> None:
    """
    Generate and display a SHAP summary plot.

    This function generates a SHAP summary plot based on the selected plot
    type. The plot is then displayed in the Streamlit application. The plot
    type is determined by the button parameter, which should match a key in the
    SUMMARY_PLOTS dictionary.

    Parameters
    ----------
    button : str
        The type of SHAP summary plot to generate. This should match a key in the
        SUMMARY_PLOTS dictionary.
    dataset : pd.DataFrame
        The dataset used to train the model. Each row represents a sample and
        each column represents a feature.
    shap_values : np.ndarray
        The SHAP values calculated for the model. Each row corresponds to a
        sample and each column corresponds to a feature. The SHAP values
        represent the contribution of each feature to the prediction for a
        sample.
    base_fig_name : str, optional
        The base name of the figure to save, given that button gives different
        types of plots.
        Default is "shap_summary_plot".

    Returns
    -------
    None
    """
    image_file = f"assets/{base_fig_name}_{SUMMARY_PLOTS[button]}.png"

    if os.path.exists(image_file):
        st.image(
            image_file,
            caption=f"{button} SHAP Summary Plot",
            use_column_width=True,
        )

    else:
        # Generate the SHAP summary plot
        shap.summary_plot(shap_values, dataset, plot_type=SUMMARY_PLOTS[button], show=False)

        # Get the current matplotlib figure
        summary_plot_fig = plt.gcf()
        summary_plot_fig.savefig(image_file)
        # Display the matplotlib figure in Streamlit
        st.pyplot(summary_plot_fig, clear_figure=True)


def generate_shap_dependence_plot(
    dataset: pd.DataFrame,
    shap_values: np.ndarray,
    base_fig_name: str = "shap_dependence_plot",
) -> None:
    """
    Generate a SHAP dependence plot.

    This function generates a SHAP dependence plot for a selected feature.
    The plot shows how a single feature affects the output of the model,
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
    base_fig_name : str, optional
        The base name of the figure to save, given that button gives different
        types of plots.
        Default is "shap_summary_plot".

    Returns
    -------
    None
    """
    feature = st.selectbox("Choose variable", dataset.columns)
    st.markdown(
        f"""
        ### {feature} importance on housing price

        To understand how a single feature effects the output of the model we
        can plot the SHAP value of that feature vs. the value of the feature
        for all the examples in a dataset. Since SHAP values represent a
        feature’s responsibility for a change in the model output, the plot
        below represents the change in predicted house price as {feature}
        changes. Vertical dispersion at a single value of {feature} represents
        interaction effects with other features. To help reveal these
        interactions the dependence plot automatically selects another feature
        for coloring.
        """
    )

    image_file = f"assets/{base_fig_name}_{feature}.png"

    if os.path.exists(image_file):
        st.image(
            image_file,
            caption=f"SHAP dependence plot for {feature}, colored by an interaction feature",
            use_column_width=True,
        )

    else:
        # Create a new matplotlib figure
        fig, ax = plt.subplots()

        # Generate the SHAP dependence plot
        shap.dependence_plot(feature, shap_values, dataset, show=False, ax=ax)

        # Get the current matplotlib figure
        shap_dependence_plot = plt.gcf()
        shap_dependence_plot.savefig(image_file)
        # Display the matplotlib figure in Streamlit
        st.pyplot(shap_dependence_plot, clear_figure=True)
