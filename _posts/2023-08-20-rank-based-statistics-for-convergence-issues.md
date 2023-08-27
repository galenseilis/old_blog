---
title: Rank-Based Statistics For Convergence Issues
date: 2023-08-19 02:50:15
categories: [statistics,rank-based-statistics]
tags: [statistics,mixed-effects,rank-based-statistics,convergence,model-fitting,monte-carlo-markov-chain,gradient-descent,numerical-underflow,numerical-overflow]
math: true
mermaid: true
---


This post is a response to a particular claim made in the following video:

{% include embed/youtube.html id='qee6b7vl2O0' %}

> I think what Galen is talking about here is convergence issues. If not, please correct me, Galen.

I was not alluding to convergence issus, although I think this is a reasonable interperation of my words. Perhaps I'll address what I actually meant in another post.

> I don't have time to go into convergence issues, but long story short sometimes the algorithms that are used to estimate models are really really complicated and the computer just can't find a solution.

I essentially agree with this, although I'll caution that "complicated" can be a few distinct things that may not align with some intuitive notions of complexity.

> So, in the presence of convergence issues, is it a good idea to use rank-based nonparametric statistcs? I still don't think so two reasons.

I think I can offer a point of agreement here that it is not necessarily a good idea to use rank-based nonparametric statistics just because convergence issues with some model are present. However, depending on context I still believe it *may* be a good idea.

> Every time that I can think of that you would have a convergence issue there is no rank-based equivalent for that.

Is this an [availability heuristic](https://en.wikipedia.org/wiki/Availability_heuristic)? I'm not sure.

But even if it isn't I wouldn't take it to mean more than an empirical induction, which is subject to the [problem of induction](https://en.wikipedia.org/wiki/Problem_of_induction). That's okay. Most of what we understand or believe is based on what we've observed to be the case so far.

I cannot think of an example either, but I have the opposite notion that there probably is such a case. This is just an intuitive judgement I have about the kinds of things that tend to be true in computation and mathematics.

> So maybe your doing a mixed model for example. As far as I know, and I could totally be wrong here cause this isn't my area of expertise, but as far as I know there are no nonparametric tests for mixed models.

That surprises me. It is relatively easy to start with a function on ranks that contains parameters and substitute in a mixed effect for one or more of the parameters. With some further assumptions, such as those to fullfill a central limit theorem, a test procedure can be developed.

> So again, I could totally be wrong here, but I don't think there's ever a sitution where you're going to have a convergence issue, because its a complex model, where there's actually going to be a rank-based equivalent for that model.

The notion that there is an equivalence between certain rank-based nonparametric statistics and non-rank-based parametric statistics is considered in my post [*Wilcoxon's heuristic*](https://galenseilis.github.io/posts/wilcoxons-heuristic/). But my terse response is that we don't need a procedure that is equivalent in order for it to be useful.

> And second, and maybe more importantly, you can fix convergence issues. Not always, but often, if not most of the time.

Yeah, my experience is that convergence issues can usually be dealt with using one or more techniques.

> If you have a serious convergence issue that means you're probably misunderstanding the model and you're asking it to do something that doesn't make sense. 

This is pretty much the [folklore theorem of statistical computing](https://statmodeling.stat.columbia.edu/2008/05/13/the_folk_theore/), which I agree with as a heuristic. Andrew Gelman, I forget where, has a fun example of falling exponentials which is not statistically identifiable even when it is the correctly specified model. I don't think it was convergence issues *per se*, but just not recovering the right parameters which was the problem in that case. Anyway, the fundamental theorem of statistical computing, while not a theorem, is a good reminder to double check that your model is correctly specified.

> But assuming your model is actually properly specified, and it makes sense, convergence issues are... I want to say they're rare. But mixed models - I've been doing a lot of mixed models lately, and they're actually not that rare. You do have a lot of convergence issues, but they're not issues that are going to break the analysis entirely. It still estimates something. Its just less trustworthy.

This will depend on context, but sometimes the fitted result really is broken entirely. The main examples come from when there is numerical underflow or numerical overflow in some part of the calculations. I don't trust estimates like `NaN` or $\pm \infty$. Sometimes I don't trust when it spits out a number close to zero either. I have not seen this with linear models, but I have certaintly seen it with non-linear models.

But I do think that Dustin is right about what tends to happen. Often the results are not eggregiously wrong when you get a warning that the result did not converge. It always makes sense to double check that the resulting model isn't telling you implausible or nonsensical things, but this is especially so with models that didn't *sample smooth as butter* (as Richard McElreath, an anthropologist, likes to say when a MCMC has few/no divergences).

> But even then if you really care about convergence you could always do a Bayesian model. And with Bayesian models you still might have convergence issues but in my experience they're a lot easier to deal with than they are with a linear mixed model.

Yes, you can train Baysian models. Yes, you can still run into convergence issues. And yes they can often be addressed by variety of techniques including (but not limited to) adjusting priors or reparametrization. But I am perplexed by the comparison of a Bayesian model against a linear mixed model. They're not mutually exclusive classes of models. I can design a Bayesian model with or without mixed effects, and in either case the model may or may not be a linear model. 

There is a lateral move here, which is to use ranks on the trace plots of Monte Carlo simulations rather than a part of a regression model (presumably being fit using Monte Carlo methods). The following is a lecture by Richard McElreath introducing a handful of Monte Carlo methods, but he also coins the term "*trank plot*" as an abbreviation of trace rank plots developed in [Vehtari *et al* 2019](https://arxiv.org/abs/1903.08008). [Säilynoja *et al* 2021](https://arxiv.org/abs/2103.10522) similarly developed graphical methods using rank-based statistics to evaluate traces.

<iframe width="560" height="315" src="https://www.youtube.com/embed/rZk2FqX2XnY?si=egtIfUIbh7YpY1Wx&amp;start=3359" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

It is in part the scale and translation invariance of ranks, along with being order-preserving on a given sample, that make them suitable for identifying certain problems in trace plots. 

My overall opinion about Dustin's discussion about convergence issues is that (1) we generally agree that they happen and (2) sometimes we can do things about them and (3) there is not a known case of where convergence issues in training a model are improved by rank-transforming a data set. The rest of it I was a little perplexed about what to take away. But I did stumble on some modern applications of rank-based statistics in studying traces, so I am grateful for being prompted to think on this subject.
