""" Configs module. """
from dotenv import load_dotenv

from shap_app.configs.settings import Settings

load_dotenv()

settings = Settings()


__all__ = ["settings"]
