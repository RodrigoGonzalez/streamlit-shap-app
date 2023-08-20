import streamlit as st

with st.echo():

    def add_two_numbers(x: int, y: int) -> int:
        """Adds two numbers together."""
        return x + y

    st.write(f"Total: {add_two_numbers(1, 2)}")
