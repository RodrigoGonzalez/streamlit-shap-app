""" Exploratory Data Analysis (EDA) Correlations component """
from typing import Literal

import pandas as pd
import seaborn as sns
import streamlit as st
from streamlit_shap import st_shap


def feature_analysis() -> None:
    """Feature analysis section of the EDA page."""
    # TODO: Add data_source: str | None = "boston_housing"
    st.markdown("### Feature Analysis")
    st.markdown(
        """
        Data Science involves the formulation of certain assumptions and
        hypotheses about the dataset, which are then empirically tested through
        various analytical procedures. Based on an initial examination of the
        dataset, we can postulate the following relationships for each feature:

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
    """Generate correlation tables for the specified dataset."""
    pearson_corr = generate_correlation(dataset)

    summary, heat_map = st.columns([1, 2])
    with summary:
        summary.header(f"{method.capitalize()} Correlation Summary")
        st.markdown(f"""{method.capitalize()} Correlations between target and all features.""")
        # TODO: Add height and width parameters to st.dataframe()
        st.dataframe(pearson_corr["TARGET"].sort_values(ascending=False))

    with heat_map:
        heat_map.header(f"{method.capitalize()} Correlation Heatmap")
        sns.heatmap(
            pearson_corr.values,
            cbar=True,
            annot=True,
            square=True,
            fmt=".2f",
            annot_kws={"size": 5},
            yticklabels=pearson_corr.columns,
            xticklabels=pearson_corr.columns,
            cmap="coolwarm",
        )
        st_shap(plot=None)

    if st.checkbox("Display detailed feature correlations"):
        st.markdown(
            f"""{method.capitalize()} Correlations between all features and target variable."""
        )
        st.dataframe(pearson_corr)
