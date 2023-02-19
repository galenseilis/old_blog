---
title: Equivalence Between Rank-Based Statistics and Non-Rank-Based Statistics
date: 2023-02-16 12:00:0
categories: [statistics,rank-based-statistics]
tags: [statistics,rank-based-statistics,nonparametric-statistics,rank-based-nonparametric-statistics,equivalence,t-test,ANOVA,regression,mixed-models,logical-equivalence,equivalence-relation,isomorphism,adjunction,heuristic,history,mann-whitney-u-test,kruskall-wallis-test,invariance,ranking,ranks,monotonicity,monotonic-function,assumptions,independence,convergence,rate-of-convergence,normality,normal-distribution,commutativity,equivariance,partition,statistical-independence,symmetry]
math: true
---

This post was prompted by a quote which I have put below the following video I got it from.

{% include embed/youtube.html id='qee6b7vl2O0' %}

> **Quotation** (Dustin Fife)
>
> Every time I can think of that you would have a convergence issue there is no rank-based equivalent for that. `[...]` as far as I know there are no rank-based nonparametric tests for mixed models. The original rank-based procedures are modelled after t-tests, ANOVAs, and regressions. `[...]` I don't think there's ever a situation where you're going to have a convergence issue because its a complex model where there's actually going to be a rank-based equivalent for that model.


I recently read [False Equivalence: The Problem with Unreasonable Comparisons](https://effectiviology.com/false-equivalence/) that left me with a sense that equivalence (according to the author, Itamar Shatz) is a subjective opinion about what can and cannot be compared. Maybe such an approach to thinking about equivalence is valuable, but frankly I prefer the tools provided by logic and mathematics. Ideas like [logical equivalence](https://en.wikipedia.org/wiki/Logical_equivalence), [equivalence relations](https://en.wikipedia.org/wiki/Equivalence_relation), [isomorphism](https://en.wikipedia.org/wiki/Isomorphism), and [adjunction](https://en.wikipedia.org/wiki/Adjoint_functors) allows us to consider different notions of "sameness" between things.

I cannot carfully consider this point about equivalence without clarification on what Dustin meant by "equivalent". It is true that at least some of the popularizers of rank-based non-parametric tests explicitly had the intention of using them as a heuristic in lieu of parametric tests such of t-tests or ANOVA. A very plain example of this comes from Frank Wilcoxon's Individual Comparisons by Ranking Methods.

> **Quotation** ([Frank Wilcoxon 1945](https://www.jstor.org/stable/3001968?origin=JSTOR-pdf))]
>
> The comparison of two treatments generally falls into one of the following two categories: (a) we may have a number of replications for each of the two treatments, which are unpaired, or (b) we may have a number of paired comparisons leading to a series of differences, some of which may be positive and some negative. `[...]`
> 
> The object of the present paper is to indicate the possiblity of using ranking methods, that is, methods in which scores 1, 2, 3, ... $n$ are substituted for the actual numerical data, in order to obtain a rapid approximate idea of the significance of the differences in experiments of this kind.

This is not to say that everyone involved in developed rank-based statistics and tests emphasized using rank-based non-parametric statistics as an approximate substitute for common non-rank-based procedures. Reading through [*On a Test of Whether One of Two Random Variables is Stochastically Larger than the Other*](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-18/issue-1/On-a-Test-of-Whether-one-of-Two-Random-Variables/10.1214/aoms/1177730491.full) by Mann and Whitney (1947), they spoke of testing for a stochastic dominance relation without any mention of testing differences in group means. They claimed that the U statistic they discuss, under some assumptions such as independence of replicates, will converge to a normally-distributed random variable. For finite samples, the only kind we really deal with, the result is an approximation that depends on the sample size (and the rate of convergence).

How closely do t-tests and ANOVA resemble some of these rank-based procedures? Let's consider some examples for compare and contrast, beginning with the Mann-Whitney $U$ statistic and unpaired t-statistic. A statistical test requires one or more statistics **and** a decision rule (i.e. a test procedure). Here I will stick to studying the statistics rather than the tests, but I recommend [@Glen\_b}'s post](https://stats.stackexchange.com/a/76080/69508) comparing the acceptance region of an ANOVA vs Kruskal-Wallis.
	
One way to study statistics is to study how they compose with other functions. While it can feel a little backward at first, an effective way to go about this is to understand what a function **doesn't** quantify. For functions $f: \Omega \mapsto \Omega^{\prime}$ and $g: \Omega \mapsto \Omega^{\prime}$ we can define $g$ to be an \textit{invariant} of $f$ if the equality $(f \circ g)(\omega) = f(\omega)$ for all $\omega \in \Omega$.

> Often $g$ is taken to be a [group action](https://en.wikipedia.org/wiki/Group_action) on the domain $\Omega$, but I think this is more specific than needed here. While it has a bent toward applications of mathematical symmetry in deep learning, which may be outside some reader's interests, I like how [Bronstein *et al* 2021](https://arxiv.org/abs/2104.13478) introduce the history and mathematical notions around this subject.
{: .prompt-info}



Because a rank transform preserves little more than the order of the input, we can understand that $(\operatorname{rank} \circ g)(X) = \operatorname{rank}(X)$ for any monotonic function $g$. If it helps, think about this counterfactually with an example. It happens that positive scaling and global translations are monotonic functions. Taking our $g(X):=X+c$, we know that $\operatorname{rank}(X+c) = \operatorname{rank}(X)$ for any $c \in \mathbb{R}$. We can ask, if the data had all been different by $c$, would the ranks be different? The answer is no! There are some similar concepts to invariance that I will briefly mention but not explore here as they are less obviously applicable. Instead of considering the equality $(f \circ g)(\omega) = f(\omega)$ we might instead find $(f \circ g)(\omega) = (g \circ f)(\omega)$, which is called \textit{equivariance}. This is a kind of [commutativity](https://en.wikipedia.org/wiki/Commutative_property) of function composition between $f$ and $g$. But we don't have to stop at equality relations. A notion of subinvariance defined by satisfying $(f \circ g)(\omega) \leq f(\omega)$. I'll leave it to the reader to explore other possibilities, and return to the topic of comparing rank-based non-parameter statistics with common non-rank-based parametric statistics.

> As an exercise, pick a function you are familiar with and look for an invariant.
{: .prompt-tip}

Not everything about a function can be neatly studied in terms of invariance, equivariance, or other similar concepts. It can help to do numerical calculations and plot the results to study how a function works. Let's go beyond ranks themselves to comparing the unpaired Student's t score against the Mann-Whitney U score (but again, not the tests). While the ranks of a collection of variables alone were invariant to translations, the Mann-Whitney U score involves a partition of the data in which the score may or may not change when a translation of the data is considered. Figure \ref{fig:tvsu} illustrates such a comparison.
	
	\begin{figure}[H]
		\centering
		\begin{tabular}{cc}
		(a) & (b) \\
		\includegraphics[scale=0.4]{U_vs_alpha.pdf} & \includegraphics[scale=0.4]{t_vs_alpha.pdf} \\
		(c) & (d) \\
		\includegraphics[scale=0.4]{U_vs_t.pdf} & \includegraphics[scale=0.4]{randomize_u_vs_t.pdf}
		\end{tabular}
		\caption{Visual comparision of how the Mann-Whitney U statistic and unpaired t-score respond to translations $\alpha$. (a) U score vs $\alpha$. (b) t score vs $\alpha$. U score vs t score ($\alpha$ is implicit). (d) Resampled U scores and t scores drawn ($N=10^4$) from where $X_1 \sim \mathcal{N}(0, 1)$ and $X_2 \sim \mathcal{N}(4, 1)$ and without any further translations. }
		\label{fig:tvsu}
	\end{figure}
	
	Panel (a) of Figure \ref{fig:tvsu} looks like a s-shaped curve, although it technically isn't a curve in the usual mathematical sense because the U score is not a smooth function of the translations.\footnote{The plot gives an appearance of smoothness due to the large sample size and choice of underlying density.} What is salient is that translating one of the groups by $\alpha$ doesn't changes the U score over some interval, but further translations either in the negative or positive direction eventually flatten out. This lack of sensitivity at the extremes may be a feature or a bug depending on what one wants to quantify.\\
	
	Contrast this to how the t-score responds linearly (and continuously) to translations as shown in panel (b) of Figure \ref{fig:tvsu}. A translation of one of the groups of variables will always have a proportional change in the t-score, entailing a kind of unbounded behaviour of the t-score for limiting cases of $\alpha$.\\
	
	A natural next-step is to plot the U scores against the t-scores, as shown in panel (c) of Figure \ref{fig:tvsu}. We again seee a s-shaped relation, which could give a false impression that the U score is simply a function of the t-score. Recall that we have plotted these statistics having been parameterized by a translation $\alpha$, and that most reasons why datasets differ is not due to something a simple or clean as a translation. The more complicated situation is exemplified by panel (d) which there is an average different of 4, but the sampled statistics are not simply differing by a translation in one of the groups. It is however clear that these statistics are not statistically independent from one another, and that roughly an increase in the t-score would correspond to an increase in the U score.
	
	\begin{figure}[H]
		\centering
		\begin{tabular}{c}
		(a)\\
		\includegraphics[scale=0.8]{anova_translation_surface} \\
		(b) \\
		\includegraphics[scale=0.8]{kruskall_translation_surface} \\
		\end{tabular}
		\caption{Each plot is calculated from the same underlying data set of sample size $m=10^3$. (a) ANOVA F statistic over translations of two variables.}
	\end{figure}
	
	Some rank-based statistics are selective to violations of order in a way that some non-rank-based statistics are not. A statistic like the Mann-Whitney U is sensitive to every violation of order between elements of two groups whereas an unpaired t-score can ``average-out" violations of order. This likewise appears consistent with the comparison of a one-way ANOVA F score vs a one-way Kruskal-Wallace ANOVA score. The classic ANOVA F appears to a convex bowl over the translations whereas the KS ANOVA has ``canals" which report to us that certain combinations of translations.
