""" Sidebar for the web app. """
import streamlit as st

from shap_app.webapp.components.dataset_info import data_dictionary


def sidebar_info(dataset: str = "boston_housing") -> None:
    """
    Display sidebar information.

    Parameters
    ----------
    dataset : str
        Dataset name.

    Returns
    -------

    """
    with st.sidebar.expander("## Project Goals"):
        st.markdown(
            """
            1. To provide client with a model for Boston housing prices, based on the
               classic dataset from the paper **'Hedonic prices and the demand
               for clean air'**, J. Environ. Economics & Management, vol.5, 81-102, 1978'
            2. Explain how the model works using the Shapley Additive Explanations (SHAP) framework
            3. Get buy-in from relevant stakeholders, then use this model to predict which
               houses are good investment opportunities
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
