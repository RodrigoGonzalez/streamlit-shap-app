""" Session state for the webapp. """
import streamlit as st

SESSION_DEFAULTS = {
    "model_name": "gpt2",
    "temperature": 0.9,
    "max_tokens": 100,
}


def initialize_session_state() -> None:
    """Initialize the session state for the webapp."""

    for k, v in SESSION_DEFAULTS.items():
        if k not in st.session_state:
            st.session_state[k] = v
