""" Example of using option_menu in Streamlit app """
import streamlit as st
from streamlit_option_menu import option_menu

selected2 = option_menu(
    None,
    ["Home", "Upload", "Tasks", "Settings"],
    icons=["house", "cloud-upload", "list-task", "gear"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
if selected2 == "Home":
    st.write("Home")
elif selected2 == "Upload":
    st.write("Upload")
elif selected2 == "Tasks":
    st.write("Tasks")
elif selected2 == "Settings":
    st.write("Settings")
