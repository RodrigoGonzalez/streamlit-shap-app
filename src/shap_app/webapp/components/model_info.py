import streamlit as st


def model_info(model: object) -> None:
    """
    Display model information.

    This function displays the information of a given model object. It prints
    the last run time and the type of the model.

    Parameters
    ----------
    model : object
        The model object whose information is to be displayed.

    Returns
    -------
    None
    """
    st.text("Model last run: 2022-01-31 07:12")
    st.text(f"Model type: {type(model)}")
