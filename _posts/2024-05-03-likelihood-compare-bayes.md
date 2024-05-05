
## Introduction
I was asked to compare what goes on in SciPy's distributions to PyMC's probabilistic models.

## Conceptual Comparison

SciPy's and PyMC's distributions are based on similar, but distinct, concepts.

### SciPy

By default SciPy uses [maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation) (MLE). Although it also supports [method of moments](https://en.wikipedia.org/wiki/Method_of_moments_(statistics)), I will focus on MLE in comparison to probabilistic Bayesian inference.

A [likelihood](https://en.wikipedia.org/wiki/Likelihood_function) is a function of both an [realization of a random variable](https://en.wikipedia.org/wiki/Realization_(probability)) (also see [random variate](https://en.wikipedia.org/wiki/Random_variate)) and a parameter $\theta$.

Abstractly this is denoted as 

$$\mathcal{L}(x \mid \theta)$$

### PyMC

PyMC is a Bayesian [probabilistic programming](https://en.wikipedia.org/wiki/Probabilistic_programming) package. It starts with the notion of defining a mathematical model in code and then using Markov Chain Monte Carlo (MCMC) methods to sample from that mathematical model. It can also perform [variational Bayesian inference](https://en.wikipedia.org/wiki/Variational_Bayesian_methods).

The core mathematical notion in PyMC is Bayes' theorem $$\Pr [A \mid B] = \frac{\Pr [B \mid A] \Pr [A]}{\Pr [B]}.$ 

### Comparison

There are some comparisons that can be drawn between Bayesian inference and MLE.

Bayes' rule can be used by either Frequentists or Bayesians.

In a maximum likelihood approach is we do not have a [prior](https://en.wikipedia.org/wiki/Prior_probability) or a [base rate](https://en.wikipedia.org/wiki/Base_rate). But is there something equivalent? Sort of.

Maximum likelihood estimation from a Bayesian perspective is often equivalent to maximum *a posteriori* estimation with a uniform prior. When the parameter space is unbounded then MLE can be seen as a special case of  MAP where a uniform [improper prior](https://en.wikipedia.org/wiki/Prior_probability#Improper_priors) is being used.

## Conclusions

In practice Bayesian inference is not a replacement for MLE, nor is MLE well-suited for all problems. Rather it is complementary to know both approaches because there are tradeoffs between them that may be better suited to certain problems.

Therefore choosing between SciPy and PyMC
