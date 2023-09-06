---
title: The Ultimate Goal Of Research Is Not Parametric Models
date: 2023-09-05 18:00:15
categories: [statistics,nonparametric-statistics]
tags: [statistics,rank-based-statistics,nonparametric-statistics]
math: true
mermaid: true
---

This post is part of a series of posts responding to the following video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qee6b7vl2O0?si=H7GJP-r4PP440f1a" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In a paper Dustin published he said:

> Quotation (Dustin Fife)
>
> Arguably, the ultimate goal of research is to have precise mathematical parametric models, but often these nonparametric models are a necessary pit stop.

I guess it is *arguable*, but I don't think it is true. Mathematical modelling is an important part of many forms of research, but I think the ultimate goals of research are somewhat more vague than that. In my view research is supposed to do two things: 

1. help us learn about the world and
2. help us make the world a better place.

Having precise mathematical parametric models seems to me more like a means to these ends rather than an end in itself.

> As an aside, it looks like [I asked ChatGPT "Is the ultimate goal of research to have precise mathematical parametric models?"](https://galenseilis.github.io/posts/chatgpt-parametric-models-as-ultimate-goal/) and it came up with a pretty reasonable response to the isolated claim.
{: .prompt-tip}

Now I know from the context of the paper Dustin (probably) wasn't meaning this phrase as broadly as I took it. Instead I think he was trying to convince the reader that 

1. the development statistical models in many forms of academic research should be persued and 
2. precise parametric models are preferable to imprecise nonparametric models.

And even more specifically to the context within the paper ([Fife & D'Onofrio 2022](https://link.springer.com/article/10.3758/s13428-022-01901-9)), Dustin was advocating that pscyhology research adopt using random forest models for 
- nonparametric modelling
- interaction detection
- nonlinearity detection
- variable selection
- prediction
- classification and
- assessing parameters of Monte Carlo simulations

Dustin has a view of research involving statistics being broken down into stages including 
- (optionally data mining,) 
- exploratory data analysis, 
- rough confirmatory data analysis, and 
- confirmatory data analysis ([Fife & Rodgers 2019](https://psyarxiv.com/5vfq6/)). 

My understanding of his point of view is that random forests and other nonparametric procedures may be put to confirmatory tests, but they will rarely if ever be a 'fully mature' theory. (Correct if I am wrong.)

I find that the geometric properties of random forests are uncanny due to the various right-angle corners and box-like subspaces that they break the domain into. But I would tend to agree with Dustin that they are a useful workhorse for at least some disciplines, including potentially psychology for having somewhat-interpretable function approximators.

No argument from me that [*ceteris paribus*](https://en.wikipedia.org/wiki/Ceteris_paribus) it is preferable to have precise statistical models rather than imprecise statistical models.

In some sense statistics itself is grafted onto other subjects when we wish to account for uncertainty. And when we do that we will find that some things are true regardless of choice of parametric distribution. Linear algebra isn't statistical *per se* and has results that hold regardless of choice of distribution, but clearly we've come up with many linear models with differing parametric assumptions. 

In the case of non-parametric statistics they often come in two flavours: 

1. invariance with respect to distribution family and 
2. approximation of any distribution family.

For the first type I don't see there being a problem with something being true regardless of the choice of distribution. A classic example is the almost-sure uniformity of ranks on continuous random variables, but it is also fair to say that ranks of random variables are not entirely nonparametric as this invariance does not hold for all discrete variables. Descriptive statistics are also nonparametric as they do not make any assumptions about the family of distributions in the population, or even *if* there is a well-defined distribution for the population. Another one of my favourite nonparametric approaches is Pearlian causal inference which requires some assumptions (just not parametric assumptions).

For the second type of nonparametric statistics we are on the doorsteps of function approximation theory and functional analysis. Random variables are measureable functions of outcome spaces, and measureable functions are closed under composition. This means that for measureable functions $f$ and $g$ it always holds that $h = f \circ g$ is also a measureable function. And random variables themselves have derived probability measures that they get from the outcome space they are defined on. When we compute a measurable function of a random variable we are producing a new random variable with its own probability distribution on that outcome space. Thus there is a kind of relationship between probability distributions via [transformations of random variables](https://en.wikibooks.org/wiki/Probability/Transformation_of_Random_Variables). In some cases we find families of functions can transform random variables with one joint distribution to random variables with almost any other joint distribution. At this stage there are far too many function approximators that can do a pretty good job to itemize, but among them are polynomials, splines, support vector machines, Gaussian processes, Dirichlet processes, Fourier series, wavelet bases, random forests, and artificial neural networks (including modern architectures such as transformers). Really, the list goes on. [Bronstein *et al* 2021](https://arxiv.org/abs/2104.13478) have further speculated that the conditions for "universal" function approximation may be very mild.

Differential equations are a nice example where we have posited a model about how something changes without specifying how it is configured. So we can take a differential equation like the heat equation and model how heat works in a great variety of different systems. This is often done without statistics, but there is a growing literature on random differential equations and stochastic differential equations. Most differential equations are compatible with various infinite families of initial and boundary conditions, we end of with infinite options for different systems we could in principle model. In a statistical context the statistical parameters that describe the system may depend on these configurational aspects of the system, and thus we can quickly find ourselves recognizing that grafting statistics on to differential equations means that our hypothesized rate equations are nonparametric hypotheses about how the world works.

When we venture further into mathematical physics we encounter notions like the principle of stationary (often least) action. This involves a differential of the time integral of a functional (i.e. a function of functions) known as a Lagrangian, which involves a difference between the potential and kinetic energy functions of a system. When we bring something as modest as measurement error into our measurement these errors propogate to the energy functions and thereby the Lagrangian and furthermore the action. So the path that a particle will take according to some physics will be random. When the stationary path depends on statistical parameters that describe the system, we again return to the notion that the principle of stationary action when combined with statistics can give us a nonparametric principle for designing statistical models.

Dustin and I agree that we should be thinking about what we want out of our models, but I don't think we should put much weight on whether a methodology is nonparametric or not *per se*.
