""" Example of using tabs in Streamlit app """
import streamlit as st

tab_input, tab_context, tab_model, tab_func, tab_code = st.tabs(
    ["💬 Messages", "🗒️ Notes", "⚙️ Options", "🛠️ Tools", "💻 View Code"]
)
with tab_input:
    st.write("Messages")
with tab_context:
    st.write("Notes")
with tab_model:
    st.write("Options")
with tab_func:
    st.write("Tools")
