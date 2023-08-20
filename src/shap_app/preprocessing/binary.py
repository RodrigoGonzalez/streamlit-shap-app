import numpy as np
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
from sklearn.preprocessing import StandardScaler

default_get_feature_names_out = StandardScaler.get_feature_names_out


class BinaryEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, threshold: float = 0.5) -> None:
        self.threshold = threshold

    def fit(self, X: np.ndarray, y: np.ndarray | None = None) -> "BinaryEncoder":
        """No fitting necessary"""
        self._check_n_features(X, reset=True)
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        """Return a binary encoding of X"""
        return np.where(X >= self.threshold, 1, 0)

    def get_feature_names_out(self, input_features: list[str] | None = None) -> list[str]:
        """Return feature names for output features."""
        return StandardScaler.get_feature_names_out(  # type: ignore
            self, input_features=input_features
        )
