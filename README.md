# Streamlit SHAP App

## Introduction

This app demonstrates how to use the [SHAP](https://shap.readthedocs.io/en/latest/index.html)
library to explain models.

## Summary

### Motivation
The general details of the machine learning project should be included in the
first part of your post. This will help potential employers understand what
you’re trying to achieve and why it’s important.

### Datasets

### Tools and Methods Used
You should include a short list of tools you used for this project and any
methods or processes you followed. This gives readers a better idea of how you
built your project and why you chose those particular tools.

## Running Code

```bash
streamlit run src/shap_app/app.py
```

### Installation

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

## Results
Highlight the results you got from your model or system and why you think this
happened. Were there any outliers or anomalies in your data that affected the
results? Can you explain why these occurred, even if they weren’t expected?

## Takeaways
Finally, you’ll want to leave the readers with some takeaways. Did anything
surprising happen during this process that changed how you think about machine
learning at large? Did any personal growth occur as a result of working on
this project?

## Relevant Literature and Links
Many of the ideas implemented in this repository were first detailed in the following papers:

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


## Contributing

Issues and pull requests are welcome.

## License

All code in this repository is released under [MIT](LICENSE).
