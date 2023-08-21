""" Streamlit app for SHAP explainers """
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu

from shap_app.main import MAIN_DIR
from shap_app.webapp.components.dataset_summary import raw_dataset_summary
from shap_app.webapp.components.dataset_visualization import raw_dataset_insights
from shap_app.webapp.components.dataset_visualization import visualize_data_introduction
from shap_app.webapp.components.eda_correlations import feature_analysis
from shap_app.webapp.components.eda_correlations import generate_correlation_tables
from shap_app.webapp.components.eda_intro import eda_main_definition
from shap_app.webapp.components.loaders import load_data
from shap_app.webapp.components.loaders import load_model
from shap_app.webapp.components.model_info import model_info
from shap_app.webapp.components.project_intro import dataset_introduction
from shap_app.webapp.components.shap import main_shap_plot
from shap_app.webapp.components.shap import tree_shap_components_loader
from shap_app.webapp.components.shap_intro import main_shap_description
from shap_app.webapp.components.shap_single import individual_tree_shap_plots
from shap_app.webapp.components.shap_summary import shap_feature_summary
from shap_app.webapp.sidebar import sidebar_info

plt.style.use("ggplot")

# st.set_option("client.showErrorDetails", True)
st.set_page_config(page_title="Explainable AI", page_icon="😎", layout="wide")

# Add custom CSS
st.markdown(
    """
    <style>
    img {
        max-width: 100%;
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    selected = option_menu(
        "Choose Dataset To Explore",
        ["Boston Housing Prices"],
        # ["Boston Housing Prices", "California Housing Prices"],
        # icons=["gear"],
        menu_icon="bookmark-fill",
        # menu_icon="robot",
        default_index=0,
    )


# Sidebar information
sidebar_info()


def set_session_state(dataset_name: str = "boston_housing") -> None:
    """Set session state variables"""
    st.session_state["dataset"] = dataset_name

    model = load_model(f"{MAIN_DIR}/trained_models/{dataset_name}/catboost_regressor.pkl")
    df = load_data(dataset_name)
    df_target = df["TARGET"]
    df_x = df.drop("TARGET", axis=1, inplace=False)
    explainer, shap_explanation, shap_values = tree_shap_components_loader(
        model=model,
        dataset=df_x,
    )

    st.session_state["model"] = model
    st.session_state["df"] = df
    st.session_state["X"] = df_x
    st.session_state["target"] = df_target
    st.session_state["explainer"] = explainer
    st.session_state["shap_values"] = shap_values
    st.session_state["shap_explanation"] = shap_explanation


set_session_state()

# Streamlit app
st.markdown("# Introduction to Explainable AI")
st.markdown(
    """
    This app demonstrates how to use the [SHAP](https://shap.readthedocs.io/en/latest/index.html)
    library to explain models.
    """
)
st.markdown("---")


# Introduction to dataset
dataset_introduction()
st.markdown("---")


# EDA Part 1
st.markdown("## Exploratory Data Analysis (EDA)")
eda_main_definition()
st.markdown("---")


# Dataset Summary
st.markdown("### Dataset Summary Statistics")
with st.expander("Model Features and Data Summary"):
    raw_dataset_summary(st.session_state["df"])
st.markdown("---")


# EDA Visualization
st.markdown("### Visualize the Data to Gain Insights")
visualize_data_introduction()
with st.expander("Visualize Individual Features with Histograms"):
    # Visualize all features and target
    raw_dataset_insights(st.session_state["df"])
with st.expander("Examining Correlations"):
    feature_analysis()
    generate_correlation_tables(st.session_state["df"])
st.markdown("---")


# Model information
st.markdown("## Prediction Models")
st.markdown("### Prediction Model Information")
model_info(st.session_state["model"])
st.markdown("---")


# Explaining the model
st.markdown("## SHAP (SHapley Additive exPlanations)")
main_shap_description()
st.markdown("## Visualizing SHAP Values using Tree SHAP")
main_shap_plot()
st.markdown("---")


# Visualizing Individual SHAP Values
st.markdown("## Visualizing Individual Data Points and SHAP Values using Tree SHAP")
individual_tree_shap_plots(
    dataset=st.session_state["X"],
    explainer=st.session_state["explainer"],
    shap_values=st.session_state["shap_values"],
    shap_explanation=st.session_state["shap_explanation"],
)
st.markdown("---")


# Display data
st.markdown("## Summarize The Impact of All Features")
shap_feature_summary(dataset=st.session_state["X"], shap_values=st.session_state["shap_values"])
st.markdown("---")


# Display link to get back to the top
st.markdown("[Back to Top](#introduction-to-explainable-ai)")


# # Other explainers
# st.markdown("## LIME (Local Interpretable Model-agnostic Explanations)")
# st.markdown("Coming Soon")
# st.markdown("---")
#
#
# st.markdown("## Partial Dependence Plots")
# st.markdown("Coming Soon")
# st.markdown("---")
