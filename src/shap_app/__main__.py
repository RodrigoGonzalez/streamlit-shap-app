""" Entry point for the Streamlit SHAP App. """
import os

import typer

from shap_app import __version__

app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"Streamlit SHAP App version: {__version__}")
        raise typer.Exit()


@app.command()
def main(
    version: bool = typer.Option(
        None, "--version", callback=version_callback, help="Show version and exit."
    )
):
    """
    Runs the main application.

    This function starts the Streamlit SHAP App.
    """
    typer.echo("Starting Streamlit SHAP App...")
    os.system("poetry run streamlit run src/shap_app/app.py")


def cli():
    """
    Executes the command line interface.

    This function does not take any parameters.

    This function does not have any return type.
    """
    app()


if __name__ == "__main__":
    typer.run(main)
