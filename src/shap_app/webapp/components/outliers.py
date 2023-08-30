"""This module contains the components for the outliers' description."""
import numpy as np
import streamlit as st
from scipy.stats import mstats


def introduction_to_techniques_to_remove_outliers():
    """Introduce the techniques to remove outliers."""
    st.markdown(
        """
        #### Removing Outliers and Their Impact on Machine Learning Models

        Outliers are data points that deviate significantly from the rest of
        the data. They can have a considerable impact on machine learning
        models, especially those that are sensitive to the distribution of
        data, such as linear regression, k-means clustering, and principal
        component analysis (PCA). Outliers can skew the model's understanding
        of the underlying data distribution, leading to poor generalization and
        predictive performance.
        """
    )
    with st.expander("### Techniques for Removing Outliers"):
        st.markdown(
            """
            The following are some of the most common techniques for removing
            outliers, as well as their python implementations:

            #### Z-Score Method

            The Z-score is a measure of how far away a data point is from the mean
            in terms of standard deviations. Data points with a Z-score greater
            than a threshold (usually 2 or 3) are considered outliers.

            **Pros**:
            - Simple to understand and implement.
            - Works well if the data is normally distributed.

            **Cons**:
            - Not robust to skewed distributions.
            - Can remove too many data points if not carefully tuned.

            ```python
            import numpy as np
            def remove_outliers_z_score(data, threshold=3):
                z_scores = np.abs((data - np.mean(data)) / np.std(data))
                return data[z_scores < threshold]
            ```

            #### Tukey's Fences

            Tukey's Fences use the interquartile range (IQR) to define outliers.
            Data points outside `[Q1 - k*IQR, Q3 + k*IQR]` are considered outliers,
            where `k` is usually 1.5.

            **Pros**:
            - More robust to skewed distributions than the Z-score method.
            - Less sensitive to extreme values.

            **Cons**:
            - May still remove too many data points if k is not chosen carefully.
            - Assumes that the data is unimodal.

            ```python
            def remove_outliers_tukey(data, k=1.5):
                Q1, Q3 = np.percentile(data, [25, 75])
                IQR = Q3 - Q1
                return data[(data >= Q1 - k*IQR) & (data <= Q3 + k*IQR)]
            ```

            #### Robust Z-Score
            This method is similar to the Z-score method but uses the median and
            the Median Absolute Deviation (MAD) instead of the mean and standard
            deviation.

            **Pros**:
            - Robust to skewed and multimodal distributions.
            - Less sensitive to extreme values.

            **Cons**:
            - Computationally more intensive due to the calculation of the median and MAD.
            - May require a larger dataset for accurate results.

            ```python
            def remove_outliers_robust_z_score(data, threshold=3):
                median = np.median(data)
                mad = np.median(np.abs(data - median))
                robust_z_scores = np.abs((data - median) / mad)
                return data[robust_z_scores < threshold]
            ```

            #### Truncated Mean

            This method involves sorting the data and removing a certain percentage
            from both ends.

            **Pros**:
            - Simple and easy to implement.
            - Does not assume any specific distribution.

            **Cons**:
            - May remove too many or too few data points depending on the percentage chosen.
            - Not robust to multimodal distributions.

            ```python
            def remove_outliers_truncated_mean(data, percentage=10):
                lower = np.percentile(data, percentage)
                upper = np.percentile(data, 100 - percentage)
                return data[(data >= lower) & (data <= upper)]
            ```

            #### Winsorizing
            This method replaces the extreme values with certain percentiles rather
            than removing them.

            **Pros**:
            - Preserves the number of data points.
            - Can be applied to any distribution.

            **Cons**:
            - Alters the data, which may not be desirable in some cases.
            - May introduce bias if the limits are not set carefully.

            ```python
            from scipy.stats import mstats
            def winsorize_data(data, limits=(0.05, 0.05)):
                return mstats.winsorize(data, limits)
            ```

            ### Evaluation Criteria for Best Techniques

            1. **Data Distribution**:
                Some methods are better suited for normally distributed data
                (Z-score), while others are more robust (Tukey's Fences,
                Robust Z-Score).
            2. **Data Loss**: Methods like Winsorizing do not remove data but
                alter it, which might be preferable in cases where data is scarce.
            3. **Computational Complexity**: Some methods are computationally
                more intensive than others.

            ### When to Use Each Method

            - **Z-Score Method**: Use when your data is normally distributed
                and you can afford to lose some data points.
            - **Tukey's Fences**: Use when your data is unimodal but not
                necessarily normally distributed.
            - **Robust Z-Score**: Use when your data is skewed or multimodal
                and you need a robust method.
            - **Truncated Mean**: Use when you do not have any assumptions
                about the data distribution and need a simple method.
            - **Winsorizing**: Use when you cannot afford to lose any data
                points and are okay with altering the data.



            """
        )

    st.markdown(
        """
        The choice of outlier removal technique can significantly impact the
        performance of machine learning models. It's crucial to understand the
        nature of your data and the model you are using to make an informed
        decision. One possible improvement could be to combine multiple
        techniques or use ensemble methods for a more robust approach.
        """
    )


def remove_outliers_z_score(data: np.ndarray, threshold: float = 3.0) -> np.ndarray:
    """
    Remove outliers from the data using the Z-score method.

    The Z-score is a measure of how far away a data point is from the mean
    in terms of standard deviations. Data points with a Z-score greater
    than a threshold are considered outliers.

    Parameters
    ----------
    data : np.ndarray
        The input data from which to remove outliers.
    threshold : float, optional
        The Z-score threshold above which data points are considered outliers.
        The default is 3.0.

    Returns
    -------
    np.ndarray
        The data with outliers removed.
    """
    mean = np.mean(data)
    std_dev = np.std(data)
    z_scores = np.abs((data - mean) / std_dev)
    return data[z_scores < threshold]


def remove_outliers_tukey(data: np.ndarray, k: float = 1.5) -> np.ndarray:
    """
    Remove outliers from the data using Tukey's Fences method.

    Tukey's Fences use the interquartile range (IQR) to define outliers.
    Data points outside `[Q1 - k*IQR, Q3 + k*IQR]` are considered outliers.

    Parameters
    ----------
    data : np.ndarray
        The input data from which to remove outliers.
    k : float, optional
        The factor that determines the range outside of which data points are
        considered outliers. The default is 1.5.

    Returns
    -------
    np.ndarray
        The data with outliers removed.
    """
    Q1, Q3 = np.percentile(data, [25, 75])
    IQR = Q3 - Q1
    return data[(data >= Q1 - k * IQR) & (data <= Q3 + k * IQR)]


def remove_outliers_robust_z_score(data: np.ndarray, threshold: float = 3.0) -> np.ndarray:
    """
    Remove outliers from the data using the Robust Z-score method.

    This method comparable to the Z-score method but uses the median and
    the Median Absolute Deviation (MAD) instead of the mean and standard
    deviation.

    Parameters
    ----------
    data : np.ndarray
        The input data from which to remove outliers.
    threshold : float, optional
        The Z-score threshold above which data points are considered outliers.
        The default is 3.0.

    Returns
    -------
    np.ndarray
        The data with outliers removed.
    """
    median = np.median(data)
    mad = np.median(np.abs(data - median))
    robust_z_scores = np.abs((data - median) / mad)
    return data[robust_z_scores < threshold]


def remove_outliers_truncated_mean(data: np.ndarray, percentage: float = 10.0) -> np.ndarray:
    """
    Remove outliers from the data using the Truncated Mean method.

    This method involves sorting the data and removing a certain percentage
    from both ends.

    Parameters
    ----------
    data : np.ndarray
        The input data from which to remove outliers.
    percentage : float, optional
        The percentage of data points to remove from both ends of the data.
        The default is 10.0.

    Returns
    -------
    np.ndarray
        The data with outliers removed.
    """
    lower = np.percentile(data, percentage)
    upper = np.percentile(data, 100 - percentage)
    return data[(data >= lower) & (data <= upper)]


def winsorize_data(data: np.ndarray, limits: tuple = (0.05, 0.05)) -> np.ndarray:
    """
    Winsorize the data.

    This method replaces the extreme values with certain percentiles rather
    than removing them.

    Parameters
    ----------
    data : np.ndarray
        The input data to winsorize.
    limits : tuple, optional
        The percentage of data points at each end of the data to replace.
        The default is (0.05, 0.05).

    Returns
    -------
    np.ndarray
        The winsorized data.
    """
    return mstats.winsorize(data, limits)


def additional_resources_outlier_removal() -> None:
    """Provide additional resources."""
    towards = "https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba"
    analysis_factor = "https://www.theanalysisfactor.com/outliers-to-drop-or-not-to-drop/"
    st.markdown(
        f"""
        ### Additional Resources

        - [Ways to Detect and Remove the Outliers]({towards})
        - [Outlier Detection and Removal Techniques]({analysis_factor})
        """
    )
