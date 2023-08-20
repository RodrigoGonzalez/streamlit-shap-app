""" CatBoostRegressor model for Boston Housing dataset. """
import pickle
from pathlib import Path

import numpy as np
from catboost import CatBoostRegressor
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import StandardScaler

from shap_app.configs import settings
from shap_app.datasets.boston_housing.loader import load_boston_housing_train_test
from shap_app.datasets.dataset_config import DatasetCardConfig
from shap_app.main import MAIN_DIR
from shap_app.pipelines.pipeline_utils import fetch_dataset_card
from shap_app.preprocessing.binary import BinaryEncoder

# Example adapted from:
# https://shap.readthedocs.io/en/latest/example_notebooks/tabular_examples/tree_based_models/Catboost%20tutorial.html

# load dataset
train, test = load_boston_housing_train_test(test_ratio=0.2)
columns = train.columns
X, y = train[columns.drop("TARGET")].values, train["TARGET"].values
df_X_train, df_y_train = train[columns.drop("TARGET")], train["TARGET"]
df_X_test, df_y_test = test[columns.drop("TARGET")], test["TARGET"]

card = fetch_dataset_card()

# Feature engineering
dataset_config = DatasetCardConfig(**card.data)


std_pipeline = Pipeline(
    [
        ("impute", SimpleImputer(strategy="median")),
        ("standardize", StandardScaler()),
    ]
)
binary_encoding_pipeline = make_pipeline(
    SimpleImputer(strategy="most_frequent"),
    BinaryEncoder(threshold=24.0),
)
binary_pipeline = make_pipeline(
    SimpleImputer(strategy="most_frequent"),
)

log_pipeline = make_pipeline(
    SimpleImputer(strategy="median"),
    FunctionTransformer(np.log, feature_names_out="one-to-one"),
    StandardScaler(),
)

LOG_FEATURES = [
    "CRIM",
    "INDUS",
    "AGE",
    "DIS",
    "TAX",
    "PTRATIO",
    "B",
    "LSTAT",
]

STD_FEATURES = [
    "ZN",
    "NOX",
    "RM",
]

BINARY_FEATURES = ["CHAS", "RAD"]


preprocessing = ColumnTransformer(
    [
        ("log", log_pipeline, LOG_FEATURES),
        ("std", std_pipeline, STD_FEATURES),
        ("binary_encoding", binary_encoding_pipeline, ["RAD"]),
        ("binary", binary_pipeline, dataset_config.binary_features),
    ]
)

train_transformed = preprocessing.fit_transform(df_X_train)
test_transformed = preprocessing.transform(df_X_test)
preprocessing.get_feature_names_out()

# Model Training Pipeline
model = CatBoostRegressor(
    iterations=300, learning_rate=0.1, random_seed=settings.GLOBAL_RANDOM_SEED
)
model.fit(X, y, verbose=False, plot=False)

# save "final" model as .pkl to give to client
model_path = Path(
    f"{MAIN_DIR}/{settings.TRAINED_MODEL_DIRECTORY}/boston_housing/"
    f"catboost_regressor_w_preprocessing.pkl"
)
pickle.dump(model, open(model_path, "wb"))
