import streamlit as st


def model_info(model: object) -> None:
    """Display model information"""
    st.text("Model last run: 2022-01-31 07:12")
    st.text(f"Model type: {type(model)}")
