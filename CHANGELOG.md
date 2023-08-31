# Changelog

<!--next-version-placeholder-->

## v0.5.0 (2023-08-31)

### Feat

- **correlated-features**: add additional charts that further display feature information (#50)

### Refactor

- **eda-components**: save figures to decrease loading time (#51)
- **eda-charts**: refactor eda charts into their own modules, add outliers section (#49)
- **eda-correlations**: refactor larger functions into smaller units (#48)
- **main-app**: fix some formatting issues in the app (#47)

## v0.4.0 (2023-08-29)

### Feat

- **main-app**: add bivariate and univariate analysis (#44)
- **main-application**: add a contents directory (#43)
- **main-app**: add project intro and images (#42)

## v0.3.7 (2023-08-23)

### Fix

- **shap-app**: the feature impact charts were not rendering properly (#40)

## v0.3.6 (2023-08-23)

### Fix

- **shap-app**: update matplotlib backend (#37)

## v0.3.5 (2023-08-23)

### Fix

- **main-app**: update image rendering to automatically resize (#35)

## v0.3.4 (2023-08-23)

### Fix

- **pyproject**: seaborn was missing for some reason (#33)
- **pyproject**: installation issues on streamlit (#32)

### Refactor

- **requirements**: move requirements file to directory pip (#31)

## v0.3.3 (2023-08-22)

### Fix

- **pyproject**: add images used to distribution (#28)

## v0.3.2 (2023-08-22)

### Fix

- **pyproject**: add readme, licence, changelog to package (#26)

## v0.3.1 (2023-08-22)

### Fix

- **shap-app**: Fix main command for CLI (#24)

## v0.3.0 (2023-08-22)

### Feat

- **shap-app**: add cli commands (#17)

## v0.2.0 (2023-08-21)

### Feat

- **main**: add cli and entry point to package (#16)
- **loaders**: add additionally functionality to loaders (#13)
- **loaders**: update load_data function to also accept paths, and add more contents to readme (#12)

### Refactor

- **shap components**: refactor to use dynamic sizes for all figures (#14)
- **datasets**: update docstrings and add run streamlit app comma… (#11)
- **components**: refactor docstrings and simplify functions where possib (#10)
- **webapp**: implement number of bins determined by the size of the dataset, and update docstrings (#9)
- **catboost**: remove catboost training info, that can stay local (#8)
- **catboost**: remove catboost training info, that can stay local (#7)

## v0.1.0 (2023-08-20)

### Feat

- **initial-commit**: moving from personal project folder into its own repository
