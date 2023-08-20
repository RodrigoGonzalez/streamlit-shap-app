import json

import streamlit as st
import toml
from streamlit_option_menu import option_menu

from shap_app.main import MAIN_DIR

st.set_page_config(
    page_title="JSON to TOML file converter",
    page_icon="😎",
)


with st.sidebar:
    selected = option_menu(
        "Choose conversion",
        ["JSON to TOML", "Converter #02 (TBC)", "Converter #03 (TBC)"],
        icons=["gear"],
        # menu_icon="bookmark-fill",
        menu_icon="robot",
        default_index=0,
    )

if selected == "JSON to TOML":
    st.image(f"{MAIN_DIR}/logo.gif", width=200)

    st.title("JSON to TOML file converter")

    st.write(
        """

            """
    )

    st.write(
        "Some 3rd party tools (e.g. Firestore) export secrets as a JSON file, "
        "but secrets in Streamlit Cloud expect a TOML. You can convert your "
        "JSON files to TOML and export them with this simple tool! 🎈\n"
    )

    st.write(
        """

        """
    )
    json_file = st.file_uploader("UPLOAD JSON FILE")

    # st.info(
    #     f"""
    #     👆 Upload a .wav file. Or try a sample:
    #     [Wav sample 01](https://github.com/CharlyWargnier/CSVHub/blob/main/
    #     Wave_files_demos/Welcome.wav?raw=true)
    #     """
    # )

    st.info(
        "👆 Upload your json file. Or try a [sample]"
        "(https://github.com/CharlyWargnier/CSVs/blob/master/more_samples/"
        "firestore-key-sample.json?raw=true).\n"
    )

    if json_file is not None:
        json_text = json_file.read()

        st.write("JSON CONTENT")
        st.code(json.loads(json_text))

        toml_content = toml.dumps(json.loads(json_text))
        st.write("TOML FILE CONTENT")
        st.code(toml_content)
        toml_file_name = json_file.name.replace(".json", ".toml")
        st.download_button("DOWNLOAD TOML FILE", data=toml_content, file_name=toml_file_name)
elif selected == "Converter #02 (TBC)":
    st.title("Page 2")
elif selected == "Converter #03 (TBC)":
    st.title("Options")
