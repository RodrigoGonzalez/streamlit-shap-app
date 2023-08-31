""" Streamlit app for SHAP explainers """
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu

from shap_app.main import MAIN_DIR
from shap_app.webapp.components.dataset_summary import raw_dataset_summary
from shap_app.webapp.components.dataset_visualization import visualize_data_introduction
from shap_app.webapp.components.eda_correlated_features import bivariate_analysis_corr_feats
from shap_app.webapp.components.eda_correlations import feature_analysis
from shap_app.webapp.components.eda_correlations import generate_correlation_tables
from shap_app.webapp.components.eda_intro import eda_main_definition
from shap_app.webapp.components.loaders import load_data
from shap_app.webapp.components.loaders import load_model
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

    individual_datapoints = "#visualizing-individual-data-points-and-shap-values-using-tree-shap"
    outliers = "#removing-outliers-and-their-impact-on-machine-learning-models"
    bivariate_corr = "#bivariate-analysis-of-correlated-features"
    st.markdown(
        f"""
        ##  Content Directory

        - [Introduction](#introduction-to-explainable-ai)
        - [Project Overview](#project-overview)
        - [Exploratory Data Analysis](#exploratory-data-analysis-eda)
            - [Dataset Summary Statistics](#dataset-summary-statistics)
            - [Visualize the Data to Gain Insights](#visualize-the-data-to-gain-insights)
            - [Univariate Analysis](#univariate-analysis)
            - [Bivariate Analysis](#bivariate-analysis)
            - [Removing Outliers and Their Impact on Machine Learning Models]({outliers})
            - [Pairwise Feature Correlations](#pairwise-feature-correlations)
            - [Bivariate Analysis of Correlated Features]({bivariate_corr})
        - [SHAP Introduction](#shap-shapley-additive-explanations)
        - [Visualizing SHAP Values](#visualizing-shap-values-using-tree-shap)
        - [Visualizing Individual Data Points]({individual_datapoints})
        - [Feature Importance](#summarize-the-impact-of-all-features)
        """
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

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        This app demonstrates how to use the
        [SHAP](https://shap.readthedocs.io/en/latest/index.html)
        library to explain models. The SHAP (SHapley Additive exPlanations)
        library is a powerful tool for interpreting machine learning models.
        It helps turn these often "black-box" algorithms into transparent
        systems that you can understand and trust.

        While the tool is computationally demanding, especially with large sets
        of data, the insights it provides are invaluable. It helps you
        understand how each factor in your data contributes to the model's
        prediction, offering a level of transparency that's crucial in today's
        data-driven world.

        ### Explainable AI: An Overview

        Explainable AI (XAI) is an emerging field in artificial intelligence
        that focuses on making machine learning models more understandable,
        transparent, and interpretable to humans. The primary goal is to
        demystify the "black box" nature of complex algorithms, such as deep
        learning models, so that stakeholders can gain insights into how
        decisions are made. This is particularly important in sensitive and
        regulated industries like healthcare, finance, and criminal justice,
        where understanding the reasoning behind decisions can have significant
        ethical and legal implications.

        ### Importance of Explainable AI

        The need for explainability arises from the increasing complexity of
        machine learning models and their growing impact on society. While
        complex models like neural networks often deliver high performance,
        their decision-making processes are not easily understandable, even to
        experts. This lack of transparency can lead to mistrust and hinder the
        adoption of AI technologies. Moreover, in some cases, regulations may
        require explanations for decisions made by automated systems. For
        example, the European Union's General Data Protection Regulation (GDPR)
        includes a "right to explanation," where individuals can ask for
        explanations on decisions made by automated systems affecting them.

        ### Approaches to Explainable AI

        Various techniques exist to make AI models more explainable. These can
        be broadly categorized into two types:

        1.  **Intrinsic Explainability**: This involves using inherently
            interpretable models, such as linear regression or decision trees,
            where the model structure itself is simple enough to be understood.

        2.  **Post-hoc Explainability**: This involves applying techniques to
            interpret complex models after they have been trained. Methods like
            LIME (Local Interpretable Model-agnostic Explanations) and SHAP
            (SHapley Additive exPlanations) are commonly used for this purpose.
            These methods approximate the decision boundary of complex models
            using simpler models or provide feature importance scores to
            explain individual predictions.

        ### Strategic Implications and Future Outlook

        Explainable AI is not just a technical requirement but also an ethical
        imperative as AI systems become more integrated into critical
        decision-making processes. It balances the trade-off between
        performance and interpretability, allowing for responsible AI use. As
        machine learning continues to evolve, the field of explainable AI will
        likely become increasingly important, shaping the way models are
        developed, validated, and deployed.
        """
    )

with col2:
    st.image(
        "assets/ai_explainability.jpg",
        caption=("AI Explainability."),
        use_column_width=True,
    )
    st.markdown(
        """
        Source: [Neo4j](https://neo4j.com/blog/ai-graph-technology-ai-explainability/).
        """
    )

st.markdown("---")
st.markdown(
    """
    ## Project Overview
    """
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        This project showcases a user-friendly app designed to make the complex
        world of machine learning easy to understand for anyone. Using a method
        called Shapley values, the app helps explain how different factors or
        "features" influence the outcome predicted by a machine learning model.
        The app is built using Streamlit, a tool that allows for a highly
        interactive and engaging user experience, complete with dynamic images
        and graphs.

        ### Project Motivation

        The driving force behind this project is to demystify machine learning
        models, making them not just understandable but also actionable for
        decision-making in various fields. Whether you're in healthcare,
        finance, or even journalism, understanding why a machine learning model
        makes a particular prediction can be crucial for making informed
        decisions.

        ### Relevance to Non-Technical Audiences

        This project is a prime example of my approach to software development,
        which focuses on creating applications that are not only scalable and
        efficient but also user-friendly and easy to understand. It's
        particularly relevant in today's world where machine learning and
        artificial intelligence are becoming increasingly integrated into our
        daily lives, making it more important than ever to understand how these
        technologies work and make decisions.

        By using this app, individuals, businesses, and organizations can gain
        a better understanding of machine learning models, empowering them to
        make more informed decisions based on transparent and interpretable
        data.
        """
    )

with col2:
    st.image(
        "assets/explainable_ai_info.jpeg",
        caption=("Why are we interested in explainable AI?"),
        use_column_width=True,
    )
    link = (
        "[birlasoft](https://www.birlasoft.com/articles/demystifying-"
        "explainable-artificial-intelligence)"
    )
    st.markdown(
        f"""
        Source: {link}.
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
st.markdown(
    f"""Shape of the dataset: {st.session_state["df"].shape[0]} rows
    and {st.session_state["df"].shape[1]} columns.
    """
)
with st.expander("Model Features and Data Summary"):
    raw_dataset_summary(st.session_state["df"])
st.markdown("---")


# EDA Visualization
st.markdown("# Visualize the Data to Gain Insights")
visualize_data_introduction(st.session_state["df"])
# with st.expander("Visualize Individual Features with Histograms"):
#     # Visualize all features and target
#     raw_dataset_insights(st.session_state["df"])
st.markdown("---")


feature_analysis(st.session_state["df_masked"])
with st.expander(
    "### Additional Detailed Information on Correlations and the Variants of "
    "Correlation Coefficients"
):
    generate_correlation_tables(st.session_state["df_masked"])
bivariate_analysis_corr_feats(st.session_state["df_masked"])

st.markdown("---")

# st.markdown(
#     """
#     ## Feature Selection Using Most Correlated Features
#
#
#     """
# )
# st.markdown("---")
#
#
# st.markdown(
#     """
#     ## Feature Engineering
#     """
# )
# st.markdown("---")


# TODO: Finish this section
# Model information
# st.markdown("## Prediction Models")
# st.markdown("### Prediction Model Information")
# model_info(st.session_state["model"])
# st.markdown("---")


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
st.markdown(
    """
    [Back to Top](#introduction-to-explainable-ai)


    By Rodrigo Gonzalez.


    © Copyright 2023.
    """
)


# # Other explainers
# st.markdown("## LIME (Local Interpretable Model-agnostic Explanations)")
# st.markdown("Coming Soon")
# st.markdown("---")
#
#
# st.markdown("## Partial Dependence Plots")
# st.markdown("Coming Soon")
# st.markdown("---")
