import os

import typer


def main():
    typer.echo("Starting Streamlit SHAP App...")
    os.system("streamlit run src/shap_app/app.py")


if __name__ == "__main__":
    typer.run(main)
