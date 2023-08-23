# SHAP App
[![PyPI Package latest release](https://img.shields.io/pypi/v/shap-app.svg?style=flat-square)](https://pypi.org/project/shap-app/)
[![Supported versions](https://img.shields.io/pypi/pyversions/shap-app.svg?style=flat-square)](https://pypi.org/project/shap-app/)
[![code style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Introduction

This app demonstrates how to use the
[SHAP](https://shap.readthedocs.io/en/latest/index.html)
library to explain models employing the popular `streamlit`
framework for the application frontend. The application is
deployed and can be accessed at
[https://shap-app.streamlit.app/](https://shap-app.streamlit.app/).



<div style="display: flex; justify-content: space-between; align-items: center;">
  <div style="width: 45%;">
    <p>SHAP (SHapley Additive exPlanations) is a unified measure of feature
    importance that originates from game theory. It connects optimal credit
    allocation with local explanations using the classic Shapley values from
    game theory and their related extensions.

In the context of machine learning, SHAP values provide a measure for
    the contribution of each feature to the prediction for individual samples.
    They can help to interpret the output of any machine learning model.
    Essentially, Shapley values answer the question: What is the relative
    contribution of each feature value to the prediction?</p>

  </div>
  <div style="width: 45%;">
    <img src="assets/shap_header.svg" alt="SHAP" style="max-width: 100%; height: auto;" />
  </div>
</div>


## Installation

The package can be installed using `pip`:

```bash
pip install shap-app
```


## Development

### Clone Repository

```bash
git clone git@github.com:RodrigoGonzalez/streamlit-shap-app.git
```

### Poetry Installation

This project was created using poetry. To install poetry, run the following:

```bash
curl -sSL https://install.python-poetry.org | python -
```

On MacOS, you can also install poetry using Homebrew:

```bash
brew install poetry
```

**Verify Installation**: You can verify the installation by running:

```bash
poetry --version
```

### Project Dependencies

To install the dependencies, run the
following command:

```bash
make local
```

This generates a virtual environment and installs the
dependencies listed in the `pyproject.toml` file.

### Install Dependencies Using Pip

I have also included a setup.py file for those who prefer
to use pip. To install the dependencies, run the following
command:

```bash
pip install -r pip/requirements.txt
```

## Running Application

To run simply type:

```bash
shap-app
```

To see all the options, type (currently limited to only
running the application.)

```bash
shap-app --help
```

## The Interpretation of Machine Learning Models aka Explainable AI
A Vital Component for Ensuring Transparency and Trustworthiness

In a world increasingly driven by automated decision-making,
the capacity to comprehend and articulate the underlying
mechanisms of machine learning models is paramount. This
understanding, referred to as model interpretability,
enables critical insight into the actions and
justifications of algorithmic systems that profoundly
impact human lives.

### **Key Aspects of Interpretability**:

Interpretability plays a vital role,
enhancing understanding and communication.

1. **Model Debugging**:
    - Analytical Evaluation
    - What instigated this model's error?
    - What adjustments are necessary to enhance the model's performance?

2. **Human-AI Collaboration**:
    - Mutual Understanding
    - How can users interpret and place faith in the model's resolutions?

3. **Regulatory Compliance**:
    - Legal Assurance
    - Does the model adhere to statutory mandates and ethical guidelines?

### **Interpretability in the Model Lifecycle**:

The interpretability facet of the model training and
deploying pipeline instrumental during the "diagnosis"
phase of the model lifecycle workflow. AI Explainability
elucidates the model's predictions through
human-intelligible descriptions, offering multifaceted
insights into model behavior:

-   **Global Explanations**: E.g., What variables shape
    the comprehensive conduct of a loan allocation model?

-   **Local Explanations**: E.g., What rationale led to
    the approval or denial of a specific customer's loan
    application?

Observation of model explanations for subgroups of data
points is invaluable, particularly when assessing fairness
in predictions for specific demographic classifications,
for example.

### **Specific Applications of Interpretability**:

The interpretability component leverages the SHAP
(SHapley Additive exPlanations) package, a robust tool
that facilitates the analytical understanding of model
behavior, providing insights into feature importance and
contributions to individual predictions

Utilize interpretability to:

-   Ascertain the reliability of AI system predictions by
    recognizing significant factors.

-   Strategize model debugging by first comprehending its
    functionality and discerning between legitimate relationships
    and misleading associations.

-   Detect potential biases by analyzing the basis of
    predictions on sensitive or highly correlated attributes.

-   Foster user confidence through local explanations
    that explain decision outcomes.

-   Execute regulatory audits to authenticate models
    and supervise the influence of model determinations on human
    interests.

The nuanced task of model interpretation extends beyond mere
technical necessity; it fosters transparency,
accountability, and trust in AI systems. Embracing
interpretability ensures that decisions derived from
artificial intelligence are not only proficient but
principled, aligning with both legal obligations and
ethical values.


## Summary of Project



### Motivation

In the dynamic field of machine learning, understanding and
explaining model predictions is vital for understanding and
being able to take actionable insights from model predictions.
This project focuses on Shapley values, a concept from game
theory, that can be used to interpret complex models.

The primary goal of this project is to provide an intuitive
introduction to Shapley values as well as how to use the
[SHAP](https://shap.readthedocs.io/en/latest/index.html)
library. Shapley values provide a robust understanding of how
each feature individually contributes to a prediction, making
complex models easier to understand.

Streamlit is utilized to create an interactive interface for
visualizing SHAP (SHapley Additive exPlanations) prediction
explanations, making the technical concepts easier to comprehend.

The project also highlights the real-world utility of
prediction explanations, demonstrating that it's not merely a
theoretical concept but a valuable tool for informed decision-making.
Additionally, SHAP's potential for providing a
consistent feature importance measure across various models
and versatility in handling diverse datasets is demonstrated.

### Datasets

### Tools and Methods Used

1.  **Python**: The project is implemented in Python, a popular language for
    data science due to its readability and vast ecosystem of scientific libraries.
    https://www.python.org/

2.  **SHAP**: SHAP (SHapley Additive exPlanations) is a game theoretic approach
    to explain the output of any machine learning model. It connects optimal
    credit allocation with local explanations using the classic Shapley values
    from game theory and their related extensions.
    https://shap.readthedocs.io/en/latest/index.html

3.  **Streamlit**: Streamlit is an open-source Python library that makes it easy to
    create and share beautiful, custom web apps for machine learning and data science.
    In this project, Streamlit is used to create an interactive web application to
    visualize the SHAP values.
    https://streamlit.io/

4.  **Pandas**: Pandas is a software library written for the Python programming
    language for data manipulation and analysis. In particular, it offers
    data structures and operations for manipulating numerical tables and time series.
    https://pandas.pydata.org/

5.  **Numpy**: Numpy is a library for the Python programming language, adding support
    for large, multidimensional arrays and matrices, along with a large collection
    of high-level mathematical functions to operate on these arrays.
    https://numpy.org/

6.  **Scikit-learn**: Scikit-learn is a free software machine learning library
    for the Python programming language. It features various classification,
    regression and clustering algorithms.
    https://scikit-learn.org/stable/

7.  **Matplotlib**: Matplotlib is a plotting library for the Python programming
    language and its numerical mathematics extension NumPy. It provides an
    object-oriented API for embedding plots into applications.
    https://matplotlib.org/

The project follows a structured approach starting from data exploration, data
cleaning, feature engineering, model building, and finally model explanation
using SHAP values. The codebase is modular and follows good software engineering
practices.

## Project Takeaways

In writing this app, the motivation was to explore and use
streamlit and the SHAP library. Streamlit for building web
applications, and SHAP for understanding decision-making
within models. The following section will outline key
takeaways from working with these tools.

### Streamlit

Streamlit is an excellent open source library for creating web applications
that showcase machine learning and data science projects. It's easy to use,
the documentation is excellent, and it integrates well with the open source
libraries used in this project. However, it may not be the best choice for
scalable or enterprise-level applications. Streamlit lacks some of the
more advanced customizations available in other web development frameworks,
but my biggest concerns for using outside smaller projects and prototyping
are that state management can be challenging and performance will be an
issue for very large datasets or highly complex applications. A problem I ran
into was that testing Streamlit apps can be challenging, as it's not a typical
Python library.

Overall, I think Streamlit is a great tool to have at your disposal, and
the problem it solves, getting something up and running quickly, is what it
excels at.

### SHAP Package

In this project, I used the
[SHAP (SHapley Additive exPlanations)](https://shap.readthedocs.io/en/latest/index.html)
library to interpret complex machine learning models.

The experience with SHAP in the project revealed a few
advantages. The interpretability it provided turned
previously black-box models into useful explanations,
making it easy to understand the relative contributions of
each feature. Its compatibility with various machine
learning models and good integration with `streamlit`
allowed for interactive visualizations. Moreover,
SHAP's ability to uncover the influence of each feature
through easy to generate plots, is especially useful for
explaining predictions to non-technical stakeholders.

However, the implementation was not without challenges.
SHAP's computational intensity, especially with larger
datasets and complex models, required careful optimization.
While SHAP values were insightful, interpreting them can
still be challenging, especially for non-technical audiences.
The beautiful visualizations, although informative, can
become overwhelming when dealing with a large number of
features, but feature selection techniques and careful
design can be utilized to keep the user experience
interesting.


Using the SHAP package was overwhelmingly positive, with
the pros far outweighing the cons. It's easy to see that
this library can be used to bridge the gap between machine
learning experts and other stakeholders. Any challenges
using the package can be dealt with, with careful
consideration and planning, and a thorough understanding
of the dataset.


## Relevant Literature and Links

Many of the ideas implemented in this repository were first detailed in the
following blog posts, papers, and tutorials:

1. [A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874)
2. [Consistent Individualized Feature Attribution for Tree Ensembles](https://arxiv.org/abs/1802.03888)
3. [Explainable AI for Trees: From Local Explanations to Global Understanding](https://arxiv.org/abs/1905.04610)
4. [Fairness-aware Explainable AI: A Decision-Making Perspective](https://arxiv.org/abs/2006.11458)
5. [Interpretable Machine Learning: Definitions, Methods, and Applications](https://arxiv.org/abs/1901.04592)
6. [SHAP-Sp: A Data-efficient Algorithm for Model Interpretation](https://arxiv.org/abs/2002.03222)
7. [On the Robustness of Interpretability Methods](https://arxiv.org/abs/2001.07538)
8. [Towards Accurate Model Interpretability by Training Interpretable Models](https://arxiv.org/abs/2006.16234)
9. [Understanding Black-box Predictions via Influence Functions](https://arxiv.org/abs/1703.04730)
10. [From Local Explanations to Global Understanding with Explainable AI for Trees](https://arxiv.org/abs/1905.04610)
11. [GitHub - slundberg/shap](https://github.com/slundberg/shap)
12. [Interpretable Machine Learning with SHAP](https://christophm.github.io/interpretable-ml-book/shap.html)
13. [Understanding SHAP Values](https://towardsdatascience.com/understanding-shap-values-1c1b7a0e57b7)
14. [Kaggle - Machine Learning Explainability](https://www.kaggle.com/learn/machine-learning-explainability)
15. [SHAP Values Explained Exactly How You Wished Someone Explained to You](https://medium.com/towards-data-science/shap-explained-the-way-i-wish-someone-explained-it-to-me-ab81cc69ef30)
16. [Interpreting complex models with SHAP values](https://medium.com/@gabrieltseng/interpreting-complex-models-with-shap-values-1c187db6ec83)
17. [Shapley Values Wikipedia Page](https://en.wikipedia.org/wiki/Shapley_value)


## SHAP App Limitations

-   This plugin is currently only compatible with Python 3.10+
-   Full documentation is not yet available
-   Does not support user defined datasets and packages yet.


## Contributing

Issues and pull requests are welcome.

## License

All code in this repository is released under the [MIT License](LICENSE).
