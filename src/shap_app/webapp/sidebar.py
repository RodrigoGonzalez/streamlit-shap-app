""" Sidebar for the web app. """
import streamlit as st

from shap_app.webapp.components.dataset_info import data_dictionary


def sidebar_info(dataset: str = "boston_housing") -> None:
    """
    Display sidebar information for the web application.

    This function generates the sidebar for the web application. The sidebar
    includes project goals, data dictionary, and resources. The content of the
    data dictionary is determined by the dataset parameter.

    Parameters
    ----------
    dataset : str, optional
        The name of the dataset for which the data dictionary is to be
        displayed.
        Default is "boston_housing".

    Returns
    -------
    None
    """
    with st.sidebar.expander("## Project Goals"):
        st.markdown(
            """
            1.  Develop an intuitive understanding of Shapley values and their
                application in providing comprehensive explanations for machine
                learning model predictions.
            2.  Create a user-friendly interface using Streamlit to visualize
                SHAP prediction explanations, enhancing transparency and trust
                in machine learning models.
            3.  Implement a practical use-case of prediction explanations in
                to use ongoing projects, demonstrating the value of
                interpretability in real-world applications.
            4.  Demonstrate the potential of SHAP (SHapley Additive exPlanations)
                in providing a unified measure of feature importance across
                different models.
            5.  Showcase the versatility of the application in handling
                various different datasets and models, emphasizing its
                adaptability in various business contexts.
            """
        )

    with st.sidebar.expander("Data Dictionary"):
        st.markdown(data_dictionary(dataset=dataset))

    with st.sidebar.expander("Resources"):
        ml_book = "https://christophm.github.io/interpretable-ml-book/shap.html"
        st.markdown(
            f"""
            ### Explainable AI:
            - [Interpretable Machine Learning]({ml_book}) by Christoph Molnar

            ### SHAP Tutorials:
            - [SHAP documentation](https://shap.readthedocs.io/en/latest/index.html)


            """
        )
