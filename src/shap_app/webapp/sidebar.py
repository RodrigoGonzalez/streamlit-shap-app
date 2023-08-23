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
        medium_1 = (
            "https://medium.com/towards-data-science/shap-explained-the-way-i-wish"
            "-someone-explained-it-to-me-ab81cc69ef30"
        )
        medium_2 = (
            "https://medium.com/@gabrieltseng/interpreting-complex-models-with-shap-"
            "values-1c187db6ec83"
        )
        st.markdown(
            f"""
            ### Explainable AI:
            - [Interpretable Machine Learning]({ml_book}) by Christoph Molnar

            ### SHAP Tutorials:
            - [SHAP documentation](https://shap.readthedocs.io/en/latest/index.html)
            - [Understanding SHAP Values](
              https://towardsdatascience.com/understanding-shap-values-1c1b7a0e57b7)
            - [Kaggle - Machine Learning Explainability](
              https://www.kaggle.com/learn/machine-learning-explainability)
            - [SHAP Values Explained Exactly How You Wished Someone Explained to You]({medium_1})
            - [Interpreting complex models with SHAP values]({medium_2})

            ### Interesting SHAP Papers:
            - [A Unified Approach to Interpreting Model Predictions](
               https://arxiv.org/abs/1705.07874)
            - [Consistent Individualized Feature Attribution for Tree Ensembles](
               https://arxiv.org/abs/1802.03888)
            - [Explainable AI for Trees: From Local Explanations to Global Understanding](
               https://arxiv.org/abs/1905.04610)
            - [Fairness-aware Explainable AI: A Decision-Making Perspective](
               https://arxiv.org/abs/2006.11458)
            - [Interpretable Machine Learning: Definitions, Methods, and Applications](
               https://arxiv.org/abs/1901.04592)
            - [SHAP-Sp: A Data-efficient Algorithm for Model Interpretation](
               https://arxiv.org/abs/2002.03222)
            - [On the Robustness of Interpretability Methods](
               https://arxiv.org/abs/2001.07538)
            - [Towards Accurate Model Interpretability by Training Interpretable Models](
               https://arxiv.org/abs/2006.16234)
            - [Understanding Black-box Predictions via Influence Functions](
               https://arxiv.org/abs/1703.04730)
            - [From Local Explanations to Global Understanding with Explainable AI for Trees](
                https://arxiv.org/abs/1905.04610)

            ### SHAP (SHapley Additive exPlanations)
            - [Shapley Values Wikipedia Page](https://en.wikipedia.org/wiki/Shapley_value)
            - [SHAP (SHapley Additive exPlanations)](
                https://shap.readthedocs.io/en/latest/index.html)
            """
        )

    with st.sidebar.expander("About Me"):
        st.markdown(
            """
            ### Created By: Rodrigo Gonzalez
            - Email: r[at]rodrigo-gonzalez.com

            #### SHAP Application:
            - [GitHub Repo](https://github.com/RodrigoGonzalez/streamlit-shap-app/)
            - [PyPi Distribution](https://pypi.org/project/shap-app/)
            - [Streamlit](https://shap-app.streamlit.app/)

            #### Professional Links:
            - [Website: rodrigo-gonzalez.com](https://rodrigo-gonzalez.com)
            - [Blog: rodrigo.ai](https://rodrigo.ai)
            - [LinkedIn](https://www.linkedin.com/in/rodrigo-gonzalez/)

            #### About Me:
            Machine Learning Engineer with a focus on Deep Learning/ Data Scientist.
            I am passionate about building and deploying machine learning models
            to solve real-world problems. I am also interested in the intersection
            of Artificial Intelligence, the Creative Arts, and the impact of AI on society.
            """
        )
