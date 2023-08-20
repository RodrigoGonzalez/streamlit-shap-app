from pydantic import BaseModel


class DatasetCardConfig(BaseModel):
    """Dataset Card."""

    target: str
    features: list[str]
    features_to_rename: dict[str, str] | None = None
    numerical_features: list[str] | None = None
    binary_features: list[str] | None = None
    categorical_features: list[str] | None = None
    datetime_features: list[str] | None = None
    geospatial_features: list[str] | None = None
    text_features: list[str] | None = None
    features_to_drop: list[str] | None = None
    features_to_encode: list[str] | None = None
