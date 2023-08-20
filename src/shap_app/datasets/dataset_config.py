from pydantic import BaseModel


class DatasetCardConfig(BaseModel):
    """
    DatasetCardConfig class.

    This class is a Pydantic model that represents the configuration of a
    dataset card. It contains the target variable, features, and other
    optional parameters that can be used to customize the dataset card.

    Attributes
    ----------
    target : str
        The target variable in the dataset.
    features : list[str]
        The list of features in the dataset.
    features_to_rename : dict[str, str], optional
        A dictionary mapping old feature names to new ones.
    numerical_features : list[str], optional
        The list of numerical features in the dataset.
    binary_features : list[str], optional
        The list of binary features in the dataset.
    categorical_features : list[str], optional
        The list of categorical features in the dataset.
    datetime_features : list[str], optional
        The list of datetime features in the dataset.
    geospatial_features : list[str], optional
        The list of geospatial features in the dataset.
    text_features : list[str], optional
        The list of text features in the dataset.
    features_to_drop : list[str], optional
        The list of features to drop from the dataset.
    features_to_encode : list[str], optional
        The list of features to encode in the dataset.
    """

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
