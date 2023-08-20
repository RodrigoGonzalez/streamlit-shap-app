""" Settings for the app. """
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the app"""

    TITLE: str = "Explainable AI"
    DESCRIPTION: str = "A simple app to demonstrate how SHAP values work"
    TRAINED_MODEL_DIRECTORY: str = "trained_models"
    DATASET_DIRECTORY: str = "datasets"

    # The following are used for data preprocessing and model training
    GLOBAL_RANDOM_SEED: int = 1234

    class Config:
        """
        Configuration for the Settings class.
        """

        case_sensitive = True
