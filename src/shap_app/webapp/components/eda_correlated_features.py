""" Correlated Features Component """
import os
from copy import deepcopy

import pandas as pd
import seaborn as sns
import streamlit as st
from matplotlib import pyplot as plt
from sklearn import preprocessing

from shap_app.webapp.chart_helpers import get_num_rows_for_figures

plt.style.use("ggplot")
sns.set_theme(style="whitegrid")


def bivariate_analysis_corr_feats(dataset: pd.DataFrame) -> None:
    """
    Perform bivariate analysis of correlated features.
    """
    st.markdown(
        """
        ## Bivariate Analysis of Correlated Features

        We can use a scatter plot to visualize the relationship between two
        features. This helps us understand how the features are related to each
        other and whether there is a linear relationship between the features.

        First, we will identify features that have a correlation value above a
        specified threshold with respect to the target column. We will use 0.5
        as the threshold. This means that we will identify features that have a
        correlation value (absolute) greater than 0.5. We will then use these
        features to create a scatter plot matrix.
        """
    )
    correlation_data = dataset.corr()
    correlated_features = get_correlated_features(correlation_data, "TARGET", 0.5)

    st.markdown(
        """
        ### Scatter Plot Matrix and Feature Correlation
        """
    )
    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        st.markdown(
            """
            The scatter plot matrix provides a comprehensive view of the
            pairwise relationships between numerical features that exhibit a
            significant correlation with the target variable. Specifically,
            this matrix includes only those features that have an absolute
            correlation value greater than 0.5 with the target column. This
            threshold is chosen to focus on relationships that are more likely
            to be meaningful, thereby aiding in feature selection and model
            interpretability.

            #### Features Strongly Correlated with the Target Variable

            The table below enumerates the features that meet the correlation
            criterion. These features have an absolute correlation value
            greater than 0.5 when compared to the target column. Understanding
            these correlations is crucial for predictive modeling, as features
            with high correlation to the target variable are often good
            predictors and should be considered for inclusion in the model.
            """
        )
        st.dataframe(correlated_features)

    with col2:
        plot_pairplot(correlated_features, dataset)

    st.markdown(
        """
        ### Scaled Feature Relationships with the Target Variable

        This figure presents a series of regression plots that explore the
        relationships between various scaled features—such as LSTAT (percentage
        of lower status population), INDUS (proportion of non-retail business
         acres), NOX (nitric oxide concentration), PTRATIO (pupil-teacher
         ratio), RM (average number of rooms), TAX (property tax rate),
         DIS (weighted distances to employment centers), and AGE (proportion of
         owner-occupied units built prior to 1940)—and the Median Home Value
         (TARGET).

         The features have been scaled using Min-Max scaling for
         better comparability. Each subplot provides a linear regression fit to
         indicate the trend between the feature and the target.
        """
    )

    plot_scaled_reg_plots(correlated_features, dataset)


def plot_scaled_reg_plots(
    correlated_features: pd.DataFrame, dataset: pd.DataFrame, fig_name: str = "scaled_reg_plots"
) -> None:
    """
    Plot scaled regression plots.

    Parameters
    ----------
    correlated_features : pd.DataFrame
        A DataFrame with the features that have a correlation value (absolute)
        greater than the threshold. The DataFrame has a single column
        'Correlation' with the correlation values and the index is the feature
        names.
    dataset : pd.DataFrame
        The dataset for which the reg plots are to be generated. Each column
        represents a feature and each row represents an observation.
    fig_name : str
        The name of the figure to save.

    Returns
    -------
    None
    """
    image_file = f"assets/{fig_name}.png"

    if os.path.exists(image_file):
        st.image(
            image_file,
            caption="Regression Analysis of Scaled Housing Features vs. Median Home Value",
            use_column_width=True,
        )

    else:
        # Let's scale the columns before plotting them against the target
        min_max_scaler = preprocessing.MinMaxScaler()
        columns = [column for column in correlated_features.index if column != "TARGET"]
        x = dataset.loc[:, columns]
        y = dataset["TARGET"]
        df = pd.DataFrame(data=min_max_scaler.fit_transform(x), columns=columns)
        fig, axs = plt.subplots(ncols=3, nrows=get_num_rows_for_figures(x, 3), figsize=(24, 8))
        axs = axs.flatten()
        for i, k in enumerate(columns):
            sns.regplot(
                y=y,
                x=df[k],
                ax=axs[i],
                robust=True,
                color="#003153",
                scatter_kws={"s": 10, "alpha": 0.4, "linewidths": 0.5},
            )
        plt.tight_layout(pad=0.4, w_pad=1.0, h_pad=2.5)
        reg_plots = plt.gcf()
        reg_plots.savefig(image_file)
        st.pyplot(reg_plots, clear_figure=True)


def plot_pairplot(
    correlated_features: pd.DataFrame,
    dataset: pd.DataFrame,
    fig_name: str = "pairplot",
) -> None:
    """
    Plot pairplot.

    List of Palette Options in Seaborn
        1.  deep: A balanced color palette with a mix of bright and muted
            colors.
        2.  muted: Similar to deep but with slightly muted colors.
        3.  bright: A palette with bright, high-saturation colors.
        4.  pastel: A palette with soft, pastel shades.
        5.  dark: A palette with dark, low-saturation colors.
        6.  colorblind: A palette designed to be legible by those with color
            vision deficiencies.
        7.  rocket: A perceptually uniform color map, suitable for accurately
            representing data in heatmaps.
        8.  mako: A perceptually uniform color map, similar to rocket but with
            a different color range.
        9.  flare: A perceptually uniform color map with a bright, fiery range
            of colors.
        10. cubehelix: A palette with a helix-like color range.
        11. coolwarm: A diverging palette with cool and warm colors.
        12. RdBu_r: Red-Blue reversed, another diverging palette.
        13. husl: A palette based on the HSL color space.
        14. hls: A palette based on the HLS color space.
        15. Set1, Set2, Set3: Different sets of categorical colors.

    Parameters
    ----------
    correlated_features : pd.DataFrame
        A DataFrame with the features that have a correlation value (absolute)
        greater than the threshold. The DataFrame has a single column
        'Correlation' with the correlation values and the index is the feature
        names.
    dataset : pd.DataFrame
        The dataset for which the pairplot is to be generated. Each column
        represents a feature and each row represents an observation.
    fig_name : str
        The name of the figure to save.

    Returns
    -------
    None
    """
    image_file = f"assets/{fig_name}.png"

    if os.path.exists(image_file):
        st.image(
            image_file,
            caption=(
                "Visualize Pairwise Relationships to Uncover Correlations and "
                "Patterns in the Dataset"
            ),
            use_column_width=True,
        )

    else:
        pairplot_df = deepcopy(dataset[correlated_features.index])
        pairplot_df["Target Values"] = pairplot_df["TARGET"]
        sns.pairplot(
            pairplot_df,
            hue="Target Values",
            # hue_order=None,
            palette="flare",
            vars=None,
            x_vars=None,
            y_vars=None,
            kind="scatter",
            diag_kind="hist",
            markers=None,
            height=2.5,
            aspect=1,
            corner=False,
            dropna=False,
            plot_kws=None,
            diag_kws=None,
            grid_kws=None,
            size=None,
        )
        # plt.tight_layout()
        pairplot = plt.gcf()
        pairplot.savefig(image_file)
        st.pyplot(pairplot, clear_figure=True)


def get_correlated_features(
    correlation_data: pd.DataFrame,
    column: str,
    threshold: float,
) -> pd.DataFrame:
    """
    Identify and return features that have a correlation value above a
    specified threshold.

    This function iterates over the provided correlation data, and for each
    feature, it checks if the absolute correlation value is greater than the
    specified threshold. If it is, the feature and its correlation value are
    added to lists. These lists are then used to create a DataFrame that is
    returned.

    Parameters
    ----------
    correlation_data : pd.DataFrame
        The correlation data for the features. The index should be the feature
        names and the values should be the correlation values.
    column : str
        The name of the column to use as the one to compare the correlation
        values to.
    threshold : float
        The correlation value threshold. Features with a correlation value
        (absolute) greater than this threshold will be included in the returned
        DataFrame.

    Returns
    -------
    pd.DataFrame
        A DataFrame with the features that have a correlation value (absolute)
        greater than the threshold. The DataFrame has a single column
        'Correlation' with the correlation values and the index is the feature
        names.
    """
    correlated_features = correlation_data[correlation_data.abs() > threshold][column]
    correlated_features.dropna(axis=0, inplace=True)
    return pd.DataFrame(
        correlated_features.values,
        index=correlated_features.index,
        columns=["Correlated Features"],
    )
