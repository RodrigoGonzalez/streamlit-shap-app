# Datasets to use in the Application

## Introduction

This directory contains datasets that are used in the application.

## Adding a new dataset

To add a new dataset, follow these steps:

1. Create a new directory for the dataset in this directory.
2. Add a README.md file to the new directory. Include the following information:
    - Title
    - Description
    - Source
    - License
    - Citation
3. Add the dataset to the new directory in a supported format (e.g. .csv, .tgz)
4. Add a .gitignore file to the new directory. If the dataset file exceed 500
   KB, add to the .gitignore file in this directory.
5. Add the dataset to the `datasets` section of the `pyproject.toml` file.
6. Add the dataset to the `datasets` section of the `README.md` file.
