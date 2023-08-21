# Streamlit SHAP App

## Introduction

This app demonstrates how to use the
[SHAP](https://shap.readthedocs.io/en/latest/index.html)
library to explain models.

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

This project was created using poetry. To install the dependencies, run the
following command:

```bash
poetry env use 3.10
poetry install
```

I have also included a setup.py file for those who prefer to use pip. To install
the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Running Application

```bash
streamlit run src/shap_app/app.py
```

## Summary

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


## Results
Highlight the results you got from your model or system and why you think this
happened. Were there any outliers or anomalies in your data that affected the
results? Can you explain why these occurred, even if they weren’t expected?

## Takeaways

Finally, you’ll want to leave the readers with some takeaways. Did anything
surprising happen during this process that changed how you think about machine
learning at large? Did any personal growth occur as a result of working on
this project? What would you do differently next time?

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



## Relevant Literature and Links

Many of the ideas implemented in this repository were first detailed in the
following articles, papers, and tutorials:

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
15. [Medium - SHAP in Practice](https://medium.com/@gabrieltseng/interpreting-complex-models-with-shap-values-1c187db6ec83)
16. [Azure Machine Learning Interpretability](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability)
17. [Shapley Values Wikipedia Page](https://en.wikipedia.org/wiki/Shapley_value)


## Contributing

Issues and pull requests are welcome.

## License

All code in this repository is released under [MIT](LICENSE).
