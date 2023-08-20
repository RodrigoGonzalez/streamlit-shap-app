"""Project introduction component"""
import streamlit as st


def dataset_introduction(data_source: str = "boston_housing") -> None:
    """Display dataset introduction"""
    if data_source == "boston_housing":
        boston_housing_dataset_introduction()
    elif data_source == "california_housing":
        california_housing_dataset_introduction()
    else:
        raise ValueError(f"Dataset {data_source} not found.")

    example = (
        "https://shap.readthedocs.io/en/latest/example_notebooks/tabular_examples/"
        "tree_based_models/Catboost%20tutorial.html"
    )
    st.markdown(
        f"""
        Adapted from [catboost example]({example}) in
        [SHAP Package Documentation](https://shap.readthedocs.io/en/latest/index.html)
        """
    )


def boston_housing_dataset_introduction() -> None:
    """Display dataset introduction"""
    st.markdown("## Boston House Price Predictions")
    st.markdown(
        """
        The Boston Housing dataset is a renowned dataset in the field of
        machine learning, often used for regression tasks. It contains 506
        entries, each representing a census tract in the Boston area, with 13
        features and a target variable. The features include a variety of
        information about the area, such as the per capita crime rate (CRIM),
        the proportion of residential land zoned for lots over 25,000 sq.ft.
        (ZN), the proportion of non-retail business acres per town (INDUS),
        and a binary variable indicating whether the tract borders the Charles
        River (CHAS). It also includes environmental data like nitric oxide
        concentration (NOX), and housing information like the average number
        of rooms per dwelling (RM), the proportion of homes built before 1940
        (AGE), and the median value of owner-occupied homes (MEDV). Other
        features provide information about the location's accessibility,
        such as weighted distances to five Boston employment centers (DIS),
        an index of accessibility to radial highways (RAD), and the full-value
        property-tax rate per $10,000 (TAX). The dataset also includes the
        pupil-teacher ratio by town (PTRATIO), the proportion of people of
        African American descent (B), and the percentage of the population
        considered lower status (LSTAT).

        ### Limitations

        However, the Boston Housing dataset has several limitations. First,
        it's quite old; the data was collected in 1978, and housing markets
        have changed significantly since then. Second, the dataset is
        relatively small, with only 506 entries, which can limit the complexity
        of the models that can be trained on it. Third, the 'B' feature,
        which represents the proportion of people of African American descent,
        is calculated in a way that may not accurately reflect the racial
        demographics of the area. Finally, the dataset lacks features that
        could be important in predicting house prices, such as the size of the
        house in square feet, the number of bathrooms, or the presence of
        amenities like a garage or swimming pool.

        ### Ethical Considerations

        Using the Boston Housing dataset also raises several ethical
        considerations. The 'B' feature, in particular, can be problematic.
        Using race as a predictor variable in a housing price model could
        perpetuate existing racial biases in housing prices, and it raises
        questions about the fairness and legality of such a practice.
        Furthermore, the 'LSTAT' feature, which represents the percentage of
        the population considered lower status, could also reinforce
        socioeconomic biases. Therefore, it's crucial to consider these
        ethical implications when using the Boston Housing dataset, and to
        handle these sensitive features with care.

        However, for the purposes of this project, the Boston Housing dataset
        is still a useful tool for exploring explainable AI. It's a relatively
        simple dataset, which makes it easy to understand and interpret the
        results of the models trained on it. Furthermore, the dataset contains
        a variety of features, which allows for the exploration of different
        types of models, such as linear regression, decision trees, and
        ensemble methods. Finally, the dataset contains a mix of numerical and
        categorical/binary features, which allows for the exploration of
        different types of feature transformations.
        """
    )


def california_housing_dataset_introduction() -> None:
    """Display dataset introduction"""
    st.markdown("## California Housing Prices")
