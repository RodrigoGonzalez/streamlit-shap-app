""" Exploratory Data Analysis (EDA) Introduction component """
import streamlit as st


def eda_main_definition() -> None:
    """
    Main EDA definition

    This function provides the main definition of Exploratory Data Analysis
    (EDA) in the context of the application. It uses the Streamlit library to
    display Markdown text on the web application. The Markdown text provides
    a detailed explanation of EDA, its importance, and the various steps
    involved in the process.

    Returns
    -------
    None
    """

    st.markdown(
        """
        Exploratory Data Analysis (EDA) is an approach to analyzing datasets, often large ones,
        to summarize their main characteristics, often using visual methods. It's a crucial step
        in the data analysis process because it allows the analyst to understand the patterns,
        spot anomalies, test hypotheses, and check assumptions related to the dataset.

        EDA is primarily used to see what data can reveal beyond the formal modeling or hypothesis
        testing task and provides a provides a better understanding of data variables and the
        relationships between them. It can also help determine if the statistical techniques
        that are planning to be used for data analysis are appropriate.

        These can include:
        - Data collection
        - Data cleaning
        - Data wrangling or munging
        - Data profiling
        - Visualization
        - Hypothesis Testing
        - Correlation
        """
    )
    with st.expander("A description of the main steps and techniques involved in EDA"):
        st.markdown(
            """
            #### Data Collection

            This is the process of gathering data from various sources. The data
            could be collected from a database, files, online repositories, web
            scraping, APIs, etc.

            #### Data Cleaning

            This step involves preprocessing the data to handle missing values,
            outliers, incorrect data, etc. This is important because the quality
            of data and the useful information that can be derived from it directly
            affects the ability to perform EDA.

            #### Data Wrangling or Munging

            This is the process of converting or mapping data from its raw form
            into another format that allows for more convenient consumption and
            organization of the data. It involves transforming and mapping data
            from one "raw" data form into another format with the intent of making
            it more appropriate and valuable for a variety of downstream purposes,
            such as analytics.

            #### Data Profiling

            This involves statistics or summaries of the data like mean, median,
            mode, count, etc. It also includes understanding the distribution of
            data, the presence of skewness, etc.

            #### Visualization

            This involves creating charts, plots, histograms, box-plots, etc. to
            understand the distribution, count, relationship between two variables,
            spotting outliers, etc. Visualization can provide valuable insights that
            are not apparent from looking at the raw data.

            #### Correlation

            This involves understanding the relationship between different variables
            in the dataset. This is important in the context of a machine learning or
            statistical modeling task.

            #### Hypothesis Testing

            This is a statistical method that is used in making statistical decisions
            using experimental data. It's basically an assumption that we make about
            the population parameter.

            #### Dimensionality Reduction

            This technique is used to reduce the number of random variables under
            consideration, by obtaining a set of principal variables. It can be
            divided into feature selection and feature extraction.
            """
        )
    st.markdown(
        """
        EDA is not a rigid process and it can vary a lot depending on the dataset and the goal of
        the analysis. It's more of an art or a practice and less of an algorithmic or procedural
        approach. The main goal of EDA is to maximize the analyst's insight into a dataset and
        into the underlying structure of a dataset, while providing all of the
        specific items that an analyst would want to extract from a dataset, such as a
        good-fitting, parsimonious model, a list of outliers, a sense of robustness of
        conclusions, and estimates for parameters.
        """
    )
