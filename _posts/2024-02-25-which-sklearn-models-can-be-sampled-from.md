---
title: Which Scikit-Learn Models Have Built-In Uncertainty Quantification?
date: 2024-02-25 04:49:15
authors: [galen]
categories: [data-science,machine-learning,python,scikit-learn]
tags: [data-science,machine-learning,python,scikit-learn,probability,sampling,distribution,prediction,mixture-distribution,gaussian-mixture-model,bayesian-gaussian-mixture,gaussian-process,adaboost,bagging,bernoulli-distribution,negative-binomial-distribution,categorical-distribution,decision-trees,naive-bayes,kernel-density-estimation,multilayer-perceptron,logistic-regression,support-vector-machine,uncertainty-quantification,statistics]
math: true
mermaid: true
image:
	path: /assets/images/32a319ff-8dfb-447d-a840-cd81e169ca67.jpg
	alt: Machine Learning with Scikit-Learn
---

Uncertainty quantification is a valuable thing to have when modelling noisy data. We need to make decisions and it can make a huge difference having estimates of the worst probable outcome for our planning.  Many of the machine learning methodologies have ignored probabilistic inferences and have rather focused on the conditional expectation. But there are a growing number of exceptions. While there are dedicated modules for predicting probabilities, I wanted to see what was available in Scikit-Learn as "low hanging fruit".

There are three methods that a SKLearn estimator can have that seem relevant: `sample`, `sample_y`, and `predict_proba`. The `sample` method allows for values to be sampled from some internal probability distribution. Here is an example using `sklearn.mixture.BayesianGaussianMixture`.

```python
import numpy as np
from sklearn.mixture import BayesianGaussianMixture
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [12, 4], [10, 7]])
bgm = BayesianGaussianMixture(n_components=2, random_state=42).fit(X)
sampled_X, sampled_labels = bgm.sample(10_000)
```

The above example returns both a data array and labels representing which statistical subpopulation the sample came from in the mixture distribution.

The `sample_y` is currently only held by the `GaussianProcessRegressor`. It works the same way as `sample` in theory; it samples from the probability distribution. I suspect the name is different because it is considered a regressor by SKLearn whereas other classes with `sample` are not.

The `predict_proba` is held by many of the estimators. When it is implemented it returns an estimated probability for each class, which differs from the `predict` method which would return the class label with the greatest estimated probability. This allows us to sample from a multinomial distribution to obtain samples with those probabilties. Here is a short example:

```python
import numpy as np
rng = np.random.RandomState(2018)
X = rng.randint(5, size=(6, 100))
Y = np.array([1, 2, 3, 4, 4, 5])
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
clf.fit(X, Y)
prob_first_entry = clf.predict_proba(X)[0]
first_row_sample = rng.multinomial(1, prob_first_entry, size=10_000)
```

Since the probabilities are themselves estimates, they should have uncertainty. Yup, your estimated probabilities themselves should have probability distributions (sometimes called metadistributions). This means that sampling from such probabilities may actually underestimate the quantifiable uncertainty. Still, it is better than no uncertainty quantification at all.


I developed and ran a Python script which allows us to easily check what estimators (thanks to `sklearn.utils.all_estimators`) have these methods. 


| Model Class                    | `sample`   | `sample_y`   | `predict_proba`   |
|:-------------------------------|:-----------|:-------------|:------------------|
| AdaBoostClassifier             | False      | False        | True              |
| BaggingClassifier              | False      | False        | True              |
| BayesianGaussianMixture        | True       | False        | True              |
| BernoulliNB                    | False      | False        | True              |
| CalibratedClassifierCV         | False      | False        | True              |
| CategoricalNB                  | False      | False        | True              |
| ClassifierChain                | False      | False        | True              |
| ComplementNB                   | False      | False        | True              |
| DecisionTreeClassifier         | False      | False        | True              |
| DummyClassifier                | False      | False        | True              |
| ExtraTreeClassifier            | False      | False        | True              |
| ExtraTreesClassifier           | False      | False        | True              |
| GaussianMixture                | True       | False        | True              |
| GaussianNB                     | False      | False        | True              |
| GaussianProcessClassifier      | False      | False        | True              |
| GaussianProcessRegressor       | False      | True         | False             |
| GradientBoostingClassifier     | False      | False        | True              |
| GridSearchCV                   | False      | False        | True              |
| HistGradientBoostingClassifier | False      | False        | True              |
| KNeighborsClassifier           | False      | False        | True              |
| KernelDensity                  | True       | False        | False             |
| LabelPropagation               | False      | False        | True              |
| LabelSpreading                 | False      | False        | True              |
| LinearDiscriminantAnalysis     | False      | False        | True              |
| LogisticRegression             | False      | False        | True              |
| LogisticRegressionCV           | False      | False        | True              |
| MLPClassifier                  | False      | False        | True              |
| MultiOutputClassifier          | False      | False        | True              |
| MultinomialNB                  | False      | False        | True              |
| NuSVC                          | False      | False        | True              |
| OneVsRestClassifier            | False      | False        | True              |
| Pipeline                       | False      | False        | True              |
| QuadraticDiscriminantAnalysis  | False      | False        | True              |
| RFE                            | False      | False        | True              |
| RFECV                          | False      | False        | True              |
| RadiusNeighborsClassifier      | False      | False        | True              |
| RandomForestClassifier         | False      | False        | True              |
| RandomizedSearchCV             | False      | False        | True              |
| SGDClassifier                  | False      | False        | True              |
| SVC                            | False      | False        | True              |
| SelfTrainingClassifier         | False      | False        | True              |
| StackingClassifier             | False      | False        | True              |
| VotingClassifier               | False      | False        | True              |


A concern I have about this table is that not all of the classes should have working implementations of the methods of interest. For example, `Pipeline`, `MultiOutputClassifier`, and similar ensembling classes should not have any logic built-in on how to compute probabilities or samples. Rather, such methods will call an underlying estimator if it exists and has the relevant method. So the table is a little bit misleading, but a good starting point.

The above table was generated with this Python script:

```python
import pandas as pd
import inspect
from sklearn.utils import all_estimators

def get_models_with_methods():
    models_with_methods = []

    # Get all estimators from sklearn
    estimators = all_estimators()

    for name, EstimatorClass in estimators:
        # Check if EstimatorClass is a class
        if inspect.isclass(EstimatorClass):
            has_sample = 'sample' in dir(EstimatorClass)
            has_sample_y = 'sample_y' in dir(EstimatorClass)
            has_predict_proba = 'predict_proba' in dir(EstimatorClass)
            if has_sample or has_sample_y or has_predict_proba:
                models_with_methods.append((name, has_sample, has_sample_y, has_predict_proba))

    return models_with_methods

if __name__ == "__main__":
    models_with_methods = get_models_with_methods()
    df = pd.DataFrame(models_with_methods, columns=['Model Class', '`sample`', '`sample_y`', '`predict_proba`'])
    print(df.to_markdown(index=False))
```
