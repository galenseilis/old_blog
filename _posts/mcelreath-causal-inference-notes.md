This post constitutes my notes on Richard McElreath's [*Causal Inference: Science Before Statistics* presentation](https://www.youtube.com/watch?v=KNPYUVmY3NM).

## Introduction

### Horoscopes
- Statistical models are in some sense "vague".
- Models can be accurate without being correct.
- The data themselves do not contain information about causes.
- It is not possible to reliably learn causes from data alone.

### Bayes vs Frequentism
- The debate over Bayesian inference and frequentist inference is irrelevant to the problem of causal inference.
- Causal inference is more than learning an association.
	- Correlation does not imply causation.
	- Causation does not imply correlation.
- There are two key concepts for causal inference:
	- Causal inference is prediction of the outcomes of interventions.
	- Causal inference is a form of missing data imputation.

### Causal Prediction
- Knowing a cause means being able to predict the consequences of an intervention.
	- i.e. *What if I do **this***?

### Causal Imputation
- Knowing a cause means being able to construct unobserved counterfactual outcomes.
	- i.e. *What if I had done something else*?

### Experiments are No Refuge
The answers to the following questions depend on the causal assumptions that we make:
	- Why do experiments work?
	- When do experiments work?
	- Should you test for balance?
	- What if treatment were imperfect?
	- Should you control for anything?
	- Should you control for everything?

### Description is No Refuge
- Descriptive research requires causal inference.
	- To do more than describe a sample, you need causal assuptions.
	- Sampling bias, stratified sampling, post-stratification, missing data, and measurement error come into understanding descriptions.
		- Causal assumptions are needed to make sense of descriptions.
- We should not compare samples but rather we should compare populations.

## Causal Salad
- Machine learning models do not reliably account for causality.
- See [Goodfellow *et al* 20214](https://arxiv.org/abs/1412.6572) for examples of how neural networks can be susceptible to overfitting.

### Causal Salad
- Causal salad is any unprincipled approach to developing models that ends up being haphazard or incorrect from a causal perspective.
- Causal salad may come from any of the following practices:
	- Adding all the available variables into a regression model.
	- Pretend that there is no confounding.
	- Pretent that there is no measurement error.
	- Pretent that the type of missingness of data is of no concern (or is always missing completely at random (MCAR)).
	- Pretend that model performance comparison functions will pick the scientifically correct model.
		- e.g. Akaike's information criterion
		- e.g. mean squared error
		- e.g. Kullbach-Leibler divergence
		- e.g. p-values

### Multiverse Analysis
- Multiverse analysis is performing all analyses across the whole set of alternatively processed data sets corresponding to a large set of **reasonable** scenarios.
- Multiverse analysis will usually show that models are sensitive to the choice of model structure and data processing.
- Conditions that make a scenario "reasonable" are causal, but often this goes unstated.
- Multiverse analysis does not prevent causal salad.
- See [Steegen *et al* 2016](https://journals.sagepub.com/doi/10.1177/1745691616658637) for some introduction to multiverse analysis.

### No Causes In; No Causes Out
- Purportedly Nancy Cartwright in *Nature's Capacities and Their Measurement* coined the phrase, "*No causes in; no causes out*".
- Statistical models alone are insufficient for scientific models beacause they do not contain causal information.
- Regression models do not distinguish causes from confounds.
- p-values are not causal statements.
- AIC and similar model comparison functions are helpful for identifying purely predictive models, but will give no guarantees about preserving causality.

