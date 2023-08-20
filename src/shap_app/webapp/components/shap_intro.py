""" Shapley Values Intro Component """

import streamlit as st

from shap_app.webapp.images import render_svg


def main_shap_description() -> None:
    """
    Main description of SHAP.

    This function provides a detailed introduction to SHAP (SHapley Additive
    exPlanations), a unified measure of feature importance that comes from game
    theory. It explains the concept of SHAP, its properties, how SHAP values
    are calculated, and the advantages of using SHAP values. It also discusses
    the challenges of working with transformed features and provides strategies
    to overcome these challenges.

    Returns
    -------
    None
    """
    summary, shap_image = st.columns(2)
    with summary:
        st.markdown(
            """
            SHAP (SHapley Additive exPlanations) is a unified measure of
            feature importance that comes from game theory. It connects optimal
            credit allocation with local explanations using the classic Shapley
            values from game theory and their related extensions.

            In the context of machine learning, SHAP values provide a measure
            for the contribution of each feature to the prediction for
            individual samples. They can help to interpret the output of any
            machine learning model. Mainly, Shapley values answers the question:
            What is the relative contribution of each feature value
            to the prediction?

            Tree SHAP ([arXiv paper](https://arxiv.org/abs/1802.03888)) allows for
            the exact computation of SHAP values for tree ensemble methods. For more
            information, see below or check out the
            [SHAP documentation](https://shap.readthedocs.io/en/latest/index.html).
            """
        )
    with shap_image:
        with open("assets/shap_header.svg") as f:
            lines = f.readlines()
            line_string = "".join(lines)

        render_svg(line_string)
        st.markdown("")
        st.markdown(
            "SHAP Header Image from [SHAP Repository](https://github.com/slundberg/shap#readme)"
        )

    with st.expander("Various properties of SHAP values"):
        st.markdown(
            """
            **Additive Feature Attribution Methods**

            SHAP is based on the concept of a unified measure
            of feature importance that allocates the change in prediction to each feature when going
            from the base value (average prediction over the training dataset) to the current
            output.
            The sum of SHAP values for all features plus the base value is equal to the prediction
            for the given instance.

            **Consistency**

            When the value of a feature changes, its SHAP value also changes. If a feature value
            causes an increase in the predicted outcome, the SHAP value of that feature should
            also increase.

            **Local Accuracy**

            For any individual prediction, the sum of the SHAP values plus the base
            value should equal the output of the model.

            **Global Interpretability**

            The average of the SHAP values for a feature over many samples gives a measure
            of the global importance of that feature.

            **Individual Interpretability**

            For each individual prediction, the SHAP values explain how much each feature
            contributes to moving the prediction from the base value.
            """
        )

    with st.expander("A technical explanation of how SHAP values are calculated"):
        st.markdown(
            """
            The **SHAP** package takes a given model as an input, then does the
            following for a given feature $F$:

            1. Create the set of all possible feature combinations (called coalitions)
            2. Calculate the average model prediction
            3. For each coalition, calculate the difference between the model's
               prediction without $F$ and the average prediction.
            4. For each coalition, calculate the difference between the model's
               prediction with $F$ and the average prediction.
            5. For each coalition, calculate how much $F$ changed the model's
               prediction from the average (i.e., step 4 - step 3) -
               this is the marginal contribution of $F$.
            6. Shapley value = the average of all the values calculated in step 5
               (i.e., the average of $F$'s marginal contributions)
            """
        )
        st.markdown(
            """
            From
            [Shapley Values Intro](https://www.h2o.ai/blog/shapley-values-a-gentle-introduction/)
            by Adam Murphy at H2O.ai
            """
        )

    st.markdown(
        """
        #### Advantages of SHAP Values

        SHAP values have the advantage of being fairly distributed among the features.


        They are based on Shapley values, a concept from cooperative game theory used to
        fairly distribute the 'payout' among the players depending on their contribution to
        the game. In the context of machine learning, the 'game' is the prediction task,
        the 'players' are the features, and the 'payout' is the prediction.

        SHAP provides a powerful tool for understanding model behavior and debugging
        model predictions, as it allows for detailed insights on a per-sample basis.
        It's applicable to any model but is computationally intensive, especially for
        complex models.
        """
    )

    with st.expander("Challenges Working With Transformed Features"):
        st.markdown(
            """
            Converting the explanations back to the original data can be
            challenging, especially if complex transformations were applied
            to the data before training the model. The SHAP values are
            calculated based on the transformed features, and reversing this
            process is not straightforward.

            However, there are a few strategies you can use:

            1. Inverse Transformation: If your transformations are invertible
               (like scaling or normalization), you can apply the inverse
               transformation to the SHAP values. However, this approach
               doesn't work for non-invertible transformations like
               one-hot encoding.

            2. Aggregate SHAP Values: If you used one-hot encoding, you can
               aggregate the SHAP values of the one-hot encoded features
               back to the original categorical feature. This gives you a
               single SHAP value for each instance of the categorical feature.

            3. Use SHAP Interaction Values: SHAP also provides interaction
               values, which can give you more detailed insights into how
               features interact to affect the model output. This can be
               useful if you transformed interaction terms in your
               original data.

            4. Model Interpretation on Original Features: If possible,
               consider training a simpler, interpretable model (like a
               linear model or decision tree) on the original features, and
               use this model to interpret the feature importance. This
               won't give you the exact same results as the complex model,
               but it can provide a good approximation.

            Remember, the goal of using SHAP is to understand how the features
            contribute to the model output. If the transformed features are too
             difficult to interpret, it might be worth considering simpler
             transformations or models that are easier to interpret.
            """
        )

    st.markdown("---")
