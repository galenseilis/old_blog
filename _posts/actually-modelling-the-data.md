---
title: Actually Modelling the Data
date: 2023-03-02 12:00:00
categories: [statistics,statistical-modelling]
tags: [expression-tree,computation-graph,statistics,modelling,differential-equations,t-test,histogram,boxplot,welch-t-test,random-variable,measurable-function,outcome-space,probability-space,functions,transformations,data-transformations,relation,binary-relation,domain,codomain,normality,ordinary-least-squares,gauss-markov-theorem,estimation,parameters,general-linear-model,multiple-linear-regression,assumptions,function-composition,generalized-linear-models,linear-mixed-effects,mixed-effects,structural-equation-models,nonlinear-regression,generalized-linear-mixed-models,nonlinear-mixed-effects-models,empirical-induction,problem-of-induction,regression,regression-analysis,estimators,lorenz-system,bayesian,boostrap,p-values,curves,computer-algebra-system,normal-distribution,differentials,ordinary-differential-equations,stochastic-processes,stochastic-calculus,stochastic-differential-equations,ito-calculus,stratonovich-integral,derivatives,python]
math: true
---

# Introduction

This post is about comparing and contrasting my view of what a statistical model is with how Dustin Fife views statistical models. One of the keystones of Dustin's perspective is that we should actually model the data rather than transformations the data.

> A [keystone](https://en.wikipedia.org/wiki/Keystone_(architecture)) is a term from architecture for a force-balancing stone at the top of an archway. Without it, the archway would collapse.
>
> ![](https://upload.wikimedia.org/wikipedia/commons/0/02/L-Karniesbogen_%28keystone%29.png)
>
> A similar notion is that of a [keystone species](https://en.wikipedia.org/wiki/Keystone_species) in community ecology.
{: .prompt-tip}

I want to challenge this keystone in this post, and suggest a different keystone. That is, I want to explain why I find the phrase "actually modelling the data" unhelpful in my thinking, and how other ways of thinking can take its place.

# What are Models?

Dustin has already said a bunch of things about modelling. I've embedded videos where he describes models, and put quotes below them that are relevant. Go ahead and watch the videos if you have time, otherwise these quotes are a sampling of his opinions.

{% include embed/youtube.html id='guJ0wTxiky4' %}
> **Quotation** (Dustin Fife)
>
> If you're a modeler, robustifying taints your data and the "model" you fit isn't really a model anyone, because it's trying to fit data that do not represent reality.

> **Quotation** (Dustin Fife)
>
> So if you are a model[er] your primary concern is to find a model that accurately represents your data.

> **Quotation** (Dustin Fife)
>
> A model is a simplification of reality, and it retains the essential features [and] it ignores the non-essentials. I'm borrowing that definition from Joe Rogers.

{% include embed/youtube.html id='t2URzeyrDx4' %}
> **Quotation** (Dustin Fife)
>
> A model is a representation of reality. Its going to retain the "essential features" of reality while ignoring the non-essentials.

And I myself have echoed a similar sentiment in a comment on one of his videos:
> **Quotation** (Galen Seilis)
>
> I generally agree that modelling the data is preferable as it demonstrates a more complete understanding of the data generating process, but I don't think it is always practical.

Unfortunately, Galen today disagrees with Galen from over a year ago (and with Dustin). But I will clarify further what that disagreement is and where I think some agreement can be recovered.

We are almost certainly modelling on the data if we are dealing with ideas about anything, but I also think that we can show more or less comprehensive demonstrations that we understand the data generating process.

# What are Transformations?

Relevant to this discussion is Dustin's distinction between "model" and "transformation". This section explores the latter, which I will tie back into modelling later in this post.


{% include embed/youtube.html id='bHmyMlZ0ODg' %}
> **Quotation** (Dustin Fife)
>
> So all of these are just transforming your data into ranks. So its just sorting the people in terms of highest score to lowest score and then analyzing the sorted data. I don't like that idea because you have all the disadvantages of transformations. So you lose the original scale of the variable, and you're not actually modelling the data. You're modelling the ranks of the data. You should model the data.

In my view, a *transformation* is just another word for a function. A function $f : \Omega \mapsto \Omega^{\prime}$ is a binary relation $f \subseteq \Omega \times \Omega^{\prime}$ which is right-unique and left-total.
> One can construct similar relations that are left-unique and right-total. Such maps can themselves be mapped back to functions as we have considered here using a permutation on the elements of the relation. Alternatively you could define respective "left" and "right" functions. We won't rely on any of that here.
{: .prompt-info}

A binary relation $f$ being right-unique means that for all $\omega \in \Omega$ and for all $\omega^{\prime}, \tau \in \Omega^{\prime}$ it holds that $(\omega, \omega^{\prime}) \in f \land (\omega, \tau) \in f \implies \omega^{\prime} = \tau$. A binary relation $f$ being left-total means that for all $\omega \in \Omega$ there exists $\omega^{\prime} \in \Omega^{\prime}$ such that $(\omega, \omega^{\prime}) \in f$. Plainly, a function is a way of pairing every element in one set (called the domain) to only one element of another set (called the *codomain*). An example of a non-injective function is shown below:

![File:Function color example 3.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Function_color_example_3.svg/953px-Function_color_example_3.svg.png)

> In this visualization of a function it is non-injective because it pairs both the red triangle and the red square to the red blurred disc. In this example the mapping is "colour-preserving".
{: .prompt-info}

Generically we transform variables such that `<blah blah blah>`. What is `<blah blah blah>`? Well, anything you want. I don't mean this in a glib or flippant way. I mean that whenever we apply a transformation we should be getting something for it. In a statistical modelling frame, we are often looking to make descriptions, inferences, or predictions after or *via* some transformation. This is similar to Dustin's view.

> **Quotation** (Dustin Fife)
> Know what transformations are. It's basically we are applying some mathematical function like the log, or the square root, or the square to our data to make it look more normal.

If normality is important to what you are doing, then transformations *might* be a sensible approach. My only caution here is that you really can use transformations for other things than obtaining a normal distribution. I'm not convinced that normality is usually important to research goals (i.e. does your research question really involve normality *per se*?), but rather that the analyst is trying to satisfy the assumptions of [ordinary least squares](https://en.wikipedia.org/wiki/Ordinary_least_squares) estimation in order to obtain an unbiased and minimum variance (see [Gauss-Markov theorem](https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem)) estimate of their regression parameters.

Transformations are not only for preparing variables to satisfy the assumptions of a general linear model. Indeed, transformations are how we construct the notion of general linear models! We can see this in the following example of a multiple linear regression equation:

$$f(X,Z; \vec{\beta}) \triangleq \underbrace{\underbrace{\underbrace{\underbrace{\beta_1 X}_{\text{Scale }X} + \underbrace{\beta_2 Z}_{\text{Scale } Z}}_{\text{Sum}} + \beta_0}_{\text{Translate by } \beta_0} + \epsilon}_{\text{Sum}}$$

Within the above equation I have underbraced multiple transformations of the random variables. The way I have pointed them out is not unique. I could have focused on linear combinations and their relation to linear transformations, for example. A fairly general way to look at the non-uniqueness is to thing of an expression tree or computation graph which has a partial order on the operations. Here is an example of an expression tree for the linear regression above.

![](/assets/images/linear_regression_expression_tree.png)

The main point of this example is that transformations are often part of our models. What is the `<blah blah blah>` here? Why should we care about $f(X,Z;\vec \beta)$? Often we are motivated by also having a third variable $Y$ so that `<blah blah blah>` is to achieve $Y \approx f(X,Z; \vec{\beta})$ by choosing $\vec{\beta}$ in an optimal way.

In showing that models like a multiple linear regression can be shown to be compositions of transformations I have relied on the inference that most readers will agree that a multiple linear regression is a model in some sense. We may not all agree on what is a model, however. For example, is a test statistic a model? In the next section I will share what I think constitutes a fairly general criterion which I think is sufficient for something to be a statistical model.

Dustin makes a distinction between transforming the data and modelling the data. In contrast, I don't think there is much difference. Every transform that we apply to our data set has a corresponding change to the random variables that represent the data. It is models the whole way along.

# A General Statistical Model

One of the lexical barriers that exists between Dustin and I pertains to what we call a "model". Vaguely, a model is anything that we use to represent another thing. In particular we are interested in "statistical models" in this context. This motivated me to think on what I would call a model, and most especially near the edge cases where it is harder to decide if something is a model or not.

> **Quotation** (as cited in [Sundberg 1994](https://www.sciencedirect.com/science/article/abs/pii/0169743993E00412?via\%3Dihub))
	Most real-life statistical problems have one or more nonstandard features. There are no routine statistical questions, only questionable statistical routines.
>  > This quote is attributed to J.M. Hammersley in a footnote of Sundberg 1994. It is also attributed to D.R. Cox [here](https://stats.stackexchange.com/a/737/69508) where I found the same link to Sundberg's paper.
> {: .prompt-info}

The most fundamental example I can think of in statistics is the notion of a random variable on a probability space. [Random variables](https://en.wikipedia.org/wiki/Random_variable) are [measurable functions](https://en.wikipedia.org/wiki/Measurable_function) of the [outcome space](https://en.wikipedia.org/wiki/Sample_space) of a [probability space](https://en.wikipedia.org/wiki/Probability_space), and are perhaps the most common and elementary statistical models that we use to represent data with. A random variable $X$ has some probability distribution $F_X$ associated with it.

Simply declaring a random variable to represent a variable in our data set is usually only the beginning what we can consider. Often we calculate functions of random variables, called "statistics". Functions of random variables are themselves random variables. So given a function $g$ and a random variable $X$ it holds that $g(X)$ is also a random variable. This still holds for compositions of functions. If I have a sequence of functions $g_1, \cdots, g_k$ and a random variable $X$, then $(g_k \circ g_{k-1} \circ \cdots g_2 \circ g_1) (X)$ is also a random variable. In my view, all random variables are statistical models if they are intended to represent something.

> This view is not restricted to random scalars. We could likewise think about random vectors, random matrices, random tensors, random graphs, random hypergraphs, random simplicial complexes, ..., random "things". The requirements of a random variable do not even include numbers, nor do mathematical functions have to even consider numbers. There is a lot more generality than some, perhaps Dustin or perhaps not, may realize.
{: .prompt-tip}

In contrast to using random variables (as formally or as informally as required), I am unsure what Dustin means by a "model". From watching many of his videos I believe he considers [general linear models](https://en.wikipedia.org/wiki/General_linear_model), [generalized linear models](https://en.wikipedia.org/wiki/Generalized_linear_model), [(linear) effects models](https://en.wikipedia.org/wiki/Mixed_model), and [structural equation models](https://en.wikipedia.org/wiki/Structural_equation_modeling), and at least some (unspecified) [nonlinear regression](https://en.wikipedia.org/wiki/Nonlinear_regression) models to be models. I suspect further combinations thereof such as [generalized linear mixed models](https://en.wikipedia.org/wiki/Generalized_linear_mixed_model) and [nonlinear mixed effects models](https://en.wikipedia.org/wiki/Nonlinear_mixed-effects_model) probably qualify as well. Attempting an empirical induction (which may suffer from the [problem of induction](https://en.wikipedia.org/wiki/Problem_of_induction)), I infer that any [regression analysis](https://en.wikipedia.org/wiki/Regression_analysis) has sufficient conditions for being a model in Dustin's view, but I will leave that speculation for Dustin to correct. I agree that these are all models, but what remains is unclear to me is whether we agree on that conclusion for the same reasons.

# Your Parameter Estimators are Models and Transformations

Taking this notion of random variables being sufficient for having a statistical model, I want to [stress test](https://en.wikipedia.org/wiki/Stress_testing) your intuitions.

# Some Models are More Expressive Than Others
Let us consider an example to explain how some models capture more about a data generating process than others. Suppose we have a random variable $X$ and that we have seen that $X$ seems to vary over time. We collect measurements of $X$ at two time points and plot them as histograms

![Dynamics Histogram](/assets/images/dynamics_hist.png)

At this juncture of having two groups of measurements of $X$ corresponding to two timepoints, we might consider inferring how different the values of $X_{0.1}$ are from the values of $X_{0.2}$. Maybe you decide that these distributions appear approximately normal but with non-equal variances so you perform a [Welch's t-test](https://en.wikipedia.org/wiki/Welch\%27s_t-test). Maybe you decide you can model the distributions of $X_{0.1}$ and $X_{0.2}$ and derive the sampling distribution of $\frac{\bar X_{0.2} - \bar X_{0.1}}{S_{\Delta \bar X}}$ under those distribution assumptions.

> Many data analysts take their confidence level $\alpha \in (0,1)$ to be an arbitrary number such as 0.05, 0.01, or 0.005. I don't recommend this practice, although it is beyond the scope of this post to address why. 
{: .prompt-warning}

Or maybe you just perform a non-parametric bootstrap. Maybe you goes with a Bayesian approach with some choice of priors and then procede in sampling posterior values of $\frac{\bar X_{0.2} - \bar X_{0.1}}{S_{\Delta \bar X}}$. Whatever of these approach we go with, or others, we're pretty limited *prima facie* with what we can do with a data set like this. One of the main takeaways of this analysis is that $X$ seems to have net-increased between the time points.

Now let's suppose we collect a third time point to make open up more types of analysis. We examine the data as boxplots shown in the next plot. If you're from an earlier generation of statisticians you might think about setting up one of various choices of analysis of variance. And again, you might get concerned about equality of variances and do something like derive sampling distributions or bootstrap. Or even estimate the posterior of the F-scores. If you're from a later generation of statisticians you might look at this from a linear model perspective and again consider various choices about the model. Whatever you do here, you can model a richer description with these three time points in comparison to when we had measurements at only two. You get a sense that $X$ seems to increase and then decrease, which is more complicated than the two-group analysis could show us

![Dynamics Boxplot](/assets/images/dynamics_box.png)


Digging further into the matter, you discover there are two other variables $Y$ and $Z$ that seem to covary with $X$! Fortunately your grad student collected paired measurements $(X,Y,Z)$ for the three time points and plot them as a scatter.


![Dynamics Boxplot](/assets/images/dynamics_3D_scatter.png)

Confused by the unusual collection of scatter, you finally do that literature review you should have done months ago and discover that there is a curve that should explain your data. You mention this to your grad student, and they tell you they already know and immediately send you a plot of the best-fitting curve.

![Dynamics Boxplot](/assets/images/dynamics_3D_all.png)


What I didn't tell you at the start of this example is how the data was generated. After all, with real data we usually don't know it. The data was generated with the following system of differential equations

$$\frac{d}{d t} X{\left(t \right)} = \sigma \left(- X{\left(t \right)} + Y{\left(t \right)}\right)$$

$$\frac{d}{d t} Y{\left(t \right)} = \left(\rho - Z{\left(t \right)}\right) X{\left(t \right)} - Y{\left(t \right)}$$

$$\frac{d}{d t} Z{\left(t \right)} = \beta X{\left(t \right)} Y{\left(t \right)} Z{\left(t \right)}$$

where $\sigma = 10$, $\rho = 28$, $\beta = \frac{8}{3}$.

> This system is similar the [Lorenz system](https://en.wikipedia.org/wiki/Lorenz_system) in three variables. I simply replaced $\frac{d}{d t} Z{\left(t \right)} = X{\left(t \right)} Y{\left(t \right)} - \beta Z{\left(t \right)}$ with $\frac{d}{d t} Z{\left(t \right)} = \beta X{\left(t \right)} Y{\left(t \right)} Z{\left(t \right)}$. 
{: .prompt-info}

> I noticed that SymPy (a computer algebra system) grumbled about not finding a closed form solution for this system of equation. This is why I have not provided an exact solution, but rather just shared the rate equations with you.
{: .prompt-info}

All of the randomness in this simulation originated from normally-distributed initial conditions $$[X_0, Y_0, Z_0]^T \sim \mathcal{N}\left(\vec 1_3, \frac{1}{20} I_{3 \times 3} \right)$$. Because the initial conditions are random variables, so are the future states when we attempt to measure the system.

> Note that we are only considering ordinary differential equations in which we have taken our derivatives with respect to a deterministic variables (time). If you want to consider differentials of [stochastic processes](https://en.wikipedia.org/wiki/Stochastic_process) you should look further to the tools of [stochastic calculus](https://en.wikipedia.org/wiki/Stochastic_calculus) and [stochstic differential equations](https://en.wikipedia.org/wiki/Stochastic_differential_equation). See the [Itô calculus](https://en.wikipedia.org/wiki/It%C3%B4_calculus) and [Stratonovich integral](https://en.wikipedia.org/wiki/Stratonovich_integral) for a flavour of how such generalization is achieved in theory. Throwing derivatives around willy-nilly can result in sadness.
{: .prompt-warning}


# Conclusions

The main issues that prevent me from adopting Dustin's view about "actually modelling the data" are as follows:

1. I'm still not sufficiently clear about what Dustin means by "modelling the data", which is why I have stuck to *what I understand* that phrase to mean in this post.
2. Considering a "model" to be using one thing (e.g. a symbolic representation such as a word or a function) to represent another thing (e.g. a phenomena like that taller people are heavier [*caeteris paribus*](https://en.wikipedia.org/wiki/Ceteris_paribus)) is something we're pretty much always doing. Representating things is what human language and mathematics are grounded upon to begin with, so it isn't clear to me what is added by saying "actually modelling the data".
3. The way I think about statistical models is both general and clear (e.g. mathematically unambiguous), and can be used and discussed by theoreticians and practitioners alike.

# Code

In case you wish to tinker with some of the plots I've generated above, here is the requisite code.

```python
'''
This script constructs the expression tree for a multiple linear
regression as shown earlier in this post.
'''
import numpy as np
import sympy as sp
from graphviz import Source

vec_beta = np.array([sp.Symbol(f'\\beta_{i}') for i in range(3)])

vec_var = np.array([1, sp.Symbol('X'), sp.Symbol('Z')])

f = vec_beta @ vec_var + sp.Symbol('\\epsilon')

g = Source(
    sp.dotprint(f),
    filename='linear_model_expression_tree.gv'
    )

g.view()
```

```python
'''
This script simulates a system of ordinary differential
equations and saves the results to a file.
'''
import numpy as np
import pandas as pd
from scipy.integrate import odeint

# Dynamical system definition
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0
t = np.arange(0.0, 0.5, 0.001)


def f(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, beta * x * y * z

# Generate random paths at selected timepoints
times = np.array((0.1, 0.2, 0.3)).reshape(-1, 1)
data = {}
for i in range(100):
    print(i)
    state0 = np.random.normal(1, 0.05, size=3)

    states = odeint(f, state0, t)
    select_states = states[(t==0.1)|(t==0.2)|(t==0.3)]
    data[i] = np.concatenate((times, select_states), axis=1)

    
data = np.concatenate(tuple(data.values()))

df = pd.DataFrame(data, columns=['Time', 'X', 'Y', 'Z'])
df.to_csv('select_dynamics_data.csv', index=False)

# Generate mean path at many timepoints
states0 = (1,)*3
states = odeint(f, state0, t)

data = np.concatenate((t.reshape(-1,1), states), axis=1)
df = pd.DataFrame(data, columns=['Time', 'X', 'Y', 'Z'])
df.to_csv('all_dynamics_data.csv', index=False)
```

```python
'''
This script loads the data generated in the previous script
and plots it.
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('select_dynamics_data.csv')
all_df = pd.read_csv('all_dynamics_data.csv')

# Histogram
for time, dfi in df.groupby('Time'):
    if time in (0.1, 0.2):
        plt.hist(dfi.X, label=f'Time={time}')
    else:
        continue
plt.xlabel('X')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.savefig('dynamics_hist.png', dpi=300, transparent=True)
plt.close()

# Box Plot
sns.boxplot(data=df, x='Time', y='X', hue='Time', dodge=False)
plt.tight_layout()
plt.savefig('dynamics_box.png', dpi=300, transparent=True)
plt.close()

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for time, dfi in df.groupby('Time'):
    ax.scatter(*dfi[['X', 'Y', 'Z']].to_numpy().T, label=f'Time={time}')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.tight_layout()
plt.savefig('dynamics_3D_scatter.png', dpi=300, transparent=True)

ax.plot(*all_df[['X', 'Y', 'Z']].to_numpy().T, color='k')
plt.savefig('dynamics_3D_all.png', dpi=300, transparent=True)
plt.close()
```


# Citation
```latex
@MISC {Seilis20230216,
    TITLE = {Actually Modelling the Data},
    AUTHOR = {Galen Seilis (https://galenseilis.github.io/about/)},
    HOWPUBLISHED = {Galen's Blog},
    NOTE = {URL:https://galenseilis.github.io/posts/actually-modelling-the-data/ (version: 2023-02-16)},
    EPRINT = {https://galenseilis.github.io/posts/actually-modelling-the-data/},
    URL = {https://galenseilis.github.io/posts/actually-modelling-the-data/}
}
```
