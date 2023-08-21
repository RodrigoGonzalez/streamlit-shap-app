import pandas as pd
import pytest
from catboost import CatBoostRegressor

from shap_app.webapp.components.loaders import load_data
from shap_app.webapp.components.loaders import load_model


# Test cases for load_model
@pytest.mark.parametrize(
    "model_path, expected_type",
    [
        (
            "src/shap_app/trained_models/boston_housing/catboost_regressor_w_preprocessing.pkl",
            CatBoostRegressor,
        ),
        ("src/shap_app/trained_models/boston_housing/catboost_regressor.pkl", CatBoostRegressor),
        # Add more test cases as more models supported
    ],
)
def test_load_model(model_path, expected_type):
    model = load_model(model_path)
    assert isinstance(model, expected_type)


# Test cases for load_data
@pytest.mark.parametrize(
    "dataset, expected_type",
    [
        ("boston_housing", pd.DataFrame),
        ("california_housing", pd.DataFrame),
        ("src/shap_app/datasets/boston_housing/boston_housing.csv", pd.DataFrame),
        ("src/shap_app/datasets/california_housing/california_housing.csv", pd.DataFrame),
        # Add more test cases as more cases added
    ],
)
def test_load_data(dataset, expected_type):
    data = load_data(dataset)
    assert isinstance(data, expected_type)


def test_load_data__value_error():
    with pytest.raises(ValueError):
        load_data("non_existent_dataset")
