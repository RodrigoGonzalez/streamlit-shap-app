""" Exploratory Data Analysis (EDA) Correlations component """
import os
from typing import Literal

import matplotlib
import pandas as pd
import seaborn as sns
import streamlit as st
from matplotlib import pyplot as plt

matplotlib.use("Agg")


def feature_analysis(dataset: pd.DataFrame) -> None:
    """
    This function generates the feature analysis section of the EDA page.

    The feature analysis section provides an initial examination of the
    dataset, formulating certain assumptions and hypotheses about the
    relationships between different features. These hypotheses are then
    empirically tested through various analytical procedures.

    Returns
    -------
    None
    """
    # TODO: Add data_source: str | None = "boston_housing"
    st.markdown(
        """
        ## Bivariate Analysis

        In this section, we will explore the relationship between the target
        variable (the variable we want to predict) and each feature (input
        variable) in the dataset. This analysis is crucial as it helps us
        understand how each feature influences the target variable. It also
        aids in identifying any unusual data points, known as outliers, or any
        irregularities in the data.

        The insights derived from this analysis can guide us in data
        preprocessing steps such as feature transformation, which can make the
        data more suitable for modeling and potentially improve the performance
        of our predictive models.
        """
    )

    pearson_corr = generate_correlation(dataset)
    st.session_state["pearson_corr"] = pearson_corr

    st.markdown("## Pairwise Feature Correlations")
    st.markdown(
        """
        Correlations between target and all features.

        ### Correlation Analysis

        Correlation analysis is a statistical method used to evaluate the
        strength and direction of the relationship between two variables.
        The correlation coefficient ranges from -1 to 1. A value close to 1
        implies a strong positive relationship, a value close to -1 implies
        a strong negative relationship, and a value close to 0 implies no
        relationship.

        By examining the correlation between the target variable and each
        feature, we can identify which features are most likely to influence
        the target variable. This can be particularly useful in feature
        selection for our predictive model.

        Data Science involves the formulation of certain assumptions and
        hypotheses about the dataset, which are then empirically tested through
        various analytical procedures.

        ### Pearson Correlation Heatmap
        """
    )
    col1, col2 = st.columns([0.4, 0.6])

    with col1:
        st.markdown(
            """
            #### What is Pearson Correlation?

            Pearson correlation is a statistical measure that quantifies the
            linear relationship between two variables. It ranges from -1 to 1,
            where:

            - -1 indicates a perfect negative correlation
            - 0 indicates no correlation
            - 1 indicates a perfect positive correlation

            #### What is a Heatmap?

            A heatmap is a graphical representation of data where individual
            values are represented as colors. It's often used to visualize
            complex data structures, such as matrices, to make them easier to
            understand.

            #### What Does a Pearson Correlation Heatmap Show?

            A Pearson correlation heatmap shows the Pearson correlation
            coefficients between multiple variables in a dataset. Each cell in
            the heatmap corresponds to the Pearson correlation coefficient
            between two variables. The color of the cell indicates the strength
            and direction of the correlation:

            - Dark blue for strong negative correlation
            - Light colors for weak correlation
            - Dark red for strong positive correlation
            """
        )

    with col2:
        generate_heat_map(pearson_corr)

    with st.expander("### How to Interpret the Heatmap"):
        st.markdown(
            """
            1.  **Diagonal Line**: The diagonal line from the top-left to the
                bottom-right will always be colored with the strongest positive
                correlation (usually dark red) because any variable is
                perfectly correlated with itself.

            2.  **Symmetry**: The heatmap is symmetrical along the diagonal
                line, meaning the correlation between variable A and variable B
                is the same as between variable B and variable A.

            3.  **Strength and Direction**: The color intensity and hue give
                you a quick visual understanding of the relationship between
                variables. Darker colors signify stronger correlations.

            4.  **Identifying Multicollinearity**: If two independent variables
                are highly correlated (either positively or negatively), it may
                indicate multicollinearity, which could be problematic in some
                models like linear regression.

            5.  **Target Variable**: If you include the target variable in the
                heatmap, you can quickly identify which features are most
                correlated with the target, aiding in feature selection.
            """
        )

    st.markdown(
        """
        #### Initial Findings

        Based on an initial examination of the
        dataset, we can form the following relationships for the following
        features:

        - The 'RM' feature, representing the average number of rooms per dwelling,
          is likely to exhibit a direct correlation with the housing price. The
          rationale behind this assumption is that larger houses, characterized
          by a higher number of rooms, typically accommodate more individuals
          and are generally priced higher due to increased demand. Hence, 'RM'
          and housing prices are hypothesized to be directly proportional.

        - The 'LSTAT' feature, indicating the percentage of lower status
          population, is hypothesized to have an inverse relationship with the
          housing price. The underlying premise is that neighborhoods with a
          higher proportion of lower status population are likely to have lower
          purchasing power, which in turn, could lead to lower housing prices.
          Thus, 'LSTAT' and housing prices are expected to be inversely proportional.

        - The 'PTRATIO' feature, denoting the pupil-teacher ratio, is also
          anticipated to be inversely proportional to the housing price. A
          higher pupil-teacher ratio might suggest a lower number of schools
          in the neighborhood, possibly due to lower tax income. This could be
          indicative of lower average income in the neighborhood, which could
          potentially lead to lower housing prices. Therefore, 'PTRATIO' and
          housing prices are hypothesized to be inversely proportional.

        """
    )


def generate_heat_map(pearson_corr: pd.DataFrame, fig_name: str = "heat_map") -> None:
    """
    Generate a heatmap of Pearson correlation coefficients.

    Parameters
    ----------
    pearson_corr : pd.DataFrame
        A DataFrame containing the Pearson correlation coefficients.
    fig_name : str, optional
        The name of the figure to save. Default is "heat_map".

    Returns
    -------
    None
    """
    image_file = f"assets/{fig_name}.png"

    if os.path.exists(image_file):
        st.image(
            image_file,
            caption="A Heatmap of Pearson Correlation Coefficients",
            use_column_width=True,
        )

    else:
        # Create a new matplotlib figure
        plt.figure(figsize=(12.8, 9.6))

        # Generate the heatmap
        sns.heatmap(
            pearson_corr.values,
            cbar=True,
            annot=True,
            square=True,
            fmt=".2f",
            annot_kws={"size": 12},
            yticklabels=pearson_corr.columns,
            xticklabels=pearson_corr.columns,
            cmap="coolwarm",
        )
        plt.xticks(rotation=90)
        plt.yticks(rotation=0)

        heat_map = plt.gcf()
        heat_map.savefig(image_file)
        st.pyplot(heat_map, clear_figure=True)


def generate_correlation(
    dataset: pd.DataFrame, method: Literal["pearson", "kendall", "spearman"] = "pearson"
) -> pd.DataFrame:
    """Generate correlation tables for the specified dataset."""
    if method not in ["pearson", "kendall", "spearman"]:
        raise ValueError(
            f"Correlation method {method} not supported. Use one of: pearson, kendall, spearman"
        )
    corr = dataset.corr(method=method)
    sorted_target_corr = corr["TARGET"].sort_values(ascending=False)
    return dataset[sorted_target_corr.index].corr(method=method)


def generate_correlation_tables(
    dataset: pd.DataFrame, method: Literal["pearson", "kendall", "spearman"] = "pearson"
) -> None:
    """
    Generate correlation tables for the specified dataset.

    This function calculates the correlation between all pairs of features in
    the dataset using the specified method. The correlation methods supported
    are Pearson, Kendall, and Spearman. The function returns a DataFrame where
    each cell represents the correlation between a pair of features.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset for which to calculate feature correlations.
    method : str, optional
        The method to use for calculating correlations. Must be one of
        "pearson", "kendall", or "spearman".
        Default is "pearson".

    Returns
    -------
    pd.DataFrame
        A DataFrame where each cell represents the correlation between a pair
        of features.

    Raises
    ------
    ValueError
        If the specified method is not one of "pearson", "kendall", or
        "spearman".
    """
    pearson_corr = generate_correlation(dataset)
    kendall_corr = generate_correlation(dataset, method="kendall")
    spearman_corr = generate_correlation(dataset, method="spearman")

    # Save correlations
    st.session_state["pearson_corr"] = pearson_corr
    st.session_state["kendall_corr"] = kendall_corr
    st.session_state["spearman_corr"] = spearman_corr

    st.header("Correlation Summaries")
    st.markdown(
        """
        Correlation is a statistical measure that describes the degree to which
        two variables change together. If one variable tends to go up when the
        other goes up, there is a positive correlation between them.
        Conversely, if one variable tends to go down when the other goes up,
        there is a negative correlation.
        """
    )

    display_pearson_info(st.session_state["pearson_corr"])
    display_kendall_info(st.session_state["kendall_corr"])
    display_spearman_info(st.session_state["spearman_corr"])

    if st.checkbox("\n Display detailed feature correlation tables"):
        _display_full_correlation_tables(
            st.session_state["pearson_corr"],
            st.session_state["kendall_corr"],
            st.session_state["spearman_corr"],
        )


def display_pearson_info(pearson_corr: pd.DataFrame) -> None:
    """
    Display Pearson correlation information.

    Parameters
    ----------
    pearson_corr : pd.DataFrame
        A DataFrame containing the Pearson correlation coefficients.

    Returns
    -------
    None
        This function does not return anything.
    """
    st.markdown("### Pearson Correlation")
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        pearson = (
            "https://latex.codecogs.com/svg.image?r=\\frac{\\sum_{i=1}^{n}(x_i-\\bar"
            "{x})(y_i-\\bar{y})}{\\sqrt{\\sum_{i=1}^{n}(x_i-\\bar{x})^2\\sum_{i=1}^{n}"
            "(y_i-\\bar{y})^2}}"
        )
        st.markdown(
            f"""
            Pearson Correlations between target and all features.

            **Mathematical Formula**:

            <div align="center">
                <img src="{pearson}" title="Pearson Correlation" />
            </div>

            **What it Measures**:

            Pearson's correlation coefficient measures
            the linear relationship between two datasets. The values range
            from -1 to 1, where -1 indicates a perfect negative linear
            relationship, 1 indicates a perfect positive linear relationship,
            and 0 indicates no linear relationship.

            **Typical Use-Cases**:

            Widely used in finance for risk assessment,
            in psychology to assess relationships between variables, and in
            machine learning feature selection.

            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.dataframe(pearson_corr["TARGET"].sort_values(ascending=False), use_container_width=False)


def display_kendall_info(kendall_corr: pd.DataFrame) -> None:
    """
    Display Kendall correlation information.

    Parameters
    ----------
    kendall_corr : pd.DataFrame
        A DataFrame containing the Pearson correlation coefficients.

    Returns
    -------
    None
        This function does not return anything.
    """
    st.markdown("### Kendall Correlation (Kendall's Tau)")
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        kendall = (
            "https://latex.codecogs.com/svg.image?\\tau=\\frac{(n_{\\text{concordant}}"
            "-n_{\\text{discordant}})}{\\sqrt{(n_{\\text{concordant}}&plus;n_{\\text"
            "{discordant}})(n_{\\text{concordant}}&plus;n_{\\text{ties}})}}"
        )

        st.markdown(
            f"""
            Kendall Correlations between target and all features.

            **Mathematical Formula**:

            <div align="center">
                <img src="{kendall}" title="Kendall Correlation" />
            </div>

            \n
            **What it Measures**:

            Kendall's Tau assesses the strength and
            direction of the ordinal association between two measured
            quantities. It takes into account the ranks of the values and
            deals well with data that has ties.

            **Typical Use-Cases**:

            Commonly used in non-parametric statistics,
            for example, in social science research, to measure ordinal
            associations, and in time-series analysis.

            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.dataframe(kendall_corr["TARGET"].sort_values(ascending=False), use_container_width=False)


def display_spearman_info(spearman_corr: pd.DataFrame) -> None:
    """
    Display Spearman correlation information.

    Parameters
    ----------
    spearman_corr : pd.DataFrame
        A DataFrame containing the Pearson correlation coefficients.

    Returns
    -------
    None
        This function does not return anything.
    """
    st.markdown("### Spearman Correlation (Spearman's Rho)")
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        spearman = (
            "https://latex.codecogs.com/svg.image?\\rho=1-\\frac{6\\sum&space;d_i^2}{n(n^2-1)}"
        )
        st.markdown(
            f"""
            Spearman Correlations between target and all features.

            **Mathematical Formula**:

            <div align="center">
                <img src="{spearman}" title="Spearman Correlation" />
            </div>

            where d<sub><i>i</i></sub> is the difference between the ranks of
            each observation.

            **What it Measures**:

            Spearman's Rho measures the strength and
            direction of the monotonic relationship between two datasets.
            Unlike Pearson, it does not assume that the relationship is linear,
            nor does it require the variables to be measured on interval
            scales.

            **Typical Use-Cases**:

            Used when the data are not normally
            distributed or when the data are ordinal in nature.

            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.dataframe(
            spearman_corr["TARGET"].sort_values(ascending=False), use_container_width=False
        )
    st.markdown(
        """
        ### Summary

        - **Pearson**: Best for measuring linear relationships between interval
            or ratio-scaled variables.
        - **Kendall**: Good for ordinal data and when you have a small sample
            size. It's computationally more intensive than Pearson or Spearman.
        - **Spearman**: Useful for ordinal data or when the data doesn't meet
            the normality assumption. It's less sensitive to outliers compared
            to Pearson.
        """
    )
    st.markdown("---")


def _display_full_correlation_tables(
    pearson_corr: pd.DataFrame, kendall_corr: pd.DataFrame, spearman_corr: pd.DataFrame
) -> None:
    """
    Display full correlation tables.

    Parameters
    ----------
    pearson_corr : DataFrame
        Pearson Correlations between all features and target variable.
    kendall_corr : DataFrame
        Kendall Correlations between all features and target variable.
    spearman_corr : DataFrame
        Spearman Correlations between all features and target variable.
    """
    st.markdown("""Pearson Correlations between all features and target variable.""")
    st.dataframe(pearson_corr)

    st.markdown("""Kendall Correlations between all features and target variable.""")
    st.dataframe(kendall_corr)

    st.markdown("""Spearman Correlations between all features and target variable.""")
    st.dataframe(spearman_corr)
