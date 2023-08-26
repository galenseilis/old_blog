---
title: What Is A Useful Statistic?
date: 2023-08-26 00:50:15
categories: [statistics,useful-statistics]
tags: [statistics,rank-based-statistics,useful-statistics]
math: true
mermaid: true
---

This post is part of series of posts responding to the following video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qee6b7vl2O0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

> Quotation (Dustin Fife)
>
> In short I guess Galen and I agree on a lot of things but we just disagree on the uselessness of nonparametric statistics -- rank-based nonparametric statistics.

In my view every project involving statistics has goals and constraints. Goals are states in which we have something desirable. Constraints are additional criteria that are required in order to be successful.

I categorize goals into "acheivable" and "approachable". An achievable goal is a goal that... well, can be achieved. That is you can actually reach or obtain that desirable state of affairs. The second type of goal is an approachable goal, which is one in which we can get closer to the goal. Not all approachable goals are achievable, but it can still pay to be "less wrong" than before.

Contrainsts could be mathematical, like non-negativity constraints or (in)equality constraints on the mathematical problems of interest. Contraints could be technological, like the amount of computing resources available. They can also be people-oriented, like the available expertise on a team. Sometimes they are financial, like dealing with the costs of obtaining each measurement. Often there are temporal constraints, like the deadline in which the project must be complete.

A statistic is useful with respect to a given project if it helps achieve (or approaches when appropriate) the set of goals of the project while satisfying the constraints.

It is worth a little further emphasis that to me *useful* is not a synonym for optimal or uniquely best. There may be multiple statistics to choose from that are all useful, but perhaps only some or even none of them are optimal or uniquely best.

Another distinction is that *useful* is also not synonymous with Pareto efficient, which is a notion that according to some set of objectives (i.e. goals) that an option is among a set (called the *Pareto front*) which are non-dominated. For a more complete mathematical explanation of this notion see [Emmmerich & Deutz 2018](https://link.springer.com/article/10.1007/s11047-018-9685-y). While it may be non-intuitive, there are statistics which are useful but also not Pareto efficient.

In many cases the classic rank-based nonparametric have lost ground on being the current state of the art, but that is distinct from being useless for all contexts. Even the classic rank-based nonparametric statistics from the first half of the last century can be useful depending on the goals and constraints of the project. Since it depends on the project, I think [quantifiers](https://en.wikipedia.org/wiki/Quantifier_(logic)) can clarify a distinction about what I find plausible vs implausible.

- Option 1 (existence): There exists ($\exists$) a project in which rank-based nonparametric statistics are useful.
- Option 2 (universal): Rank-based nonparametric statistics are useful for any (i.e. all or $\forall$) projects.
- Option 3 (non-existence): There does not exist a project in which rank-based nonparametric statistics are useful.
- Option 4 (non-universal): Rank-based nonparametric statistics are not always useful for a project.

> Quantifiers help distinguish the strength of a claim being made into *some*, *all*, *always*, and *not always* buckets. Simple sentences can be readily misunderstood without them. Let's consider a really short example involving cows. 🐮
>
> ![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/CowPosture_20150612.jpg/1024px-CowPosture_20150612.jpg)
>
> We could start with a phrase like "cows eat grass" as a benign example, although claims about people, politics, religion and other subjects might make the case more poignantly. Just substitute "cows eat grass" with something more controversial. Anyway, we could argue over "cows eat grass". You might say that cows eat grass, and then I might counter with an example of a cow not eating grass (like the image above that isn't apparently eating grass at that moment). You might retort, "well yes, not *all* cows eat grass all of the time". 
>
> That's a short example, but I've seen arguments go on substantially longer when the participants seem completely unaware of such distinctions.
{: .prompt-tip}

I think options 1 and 4 are accurate, although Dustin and I may only agree on option 4 between the two of them. Option 4 can also rephrased as "there exists a proejct in which rank-based nonparametric statistics are not useful". Since Dustin said that he thinks rank-based nonparametric statistics are useless, I would infer that to mean that he thinks options 3 and 4 are correct. Although this is notwithstanding how we may disagree on the semantics of "useful". The only option that I don't think either Dustin or I would think is accurate is option 2. It seems quite unlikely to me that any technique is *always* useful, whether it is rank-based nonparametric statistics or anything else.

Overall I realize I think about the word "useful" in a way that might be unconventional, but hopefully this post provides a modicum of clarification on what I mean by it.
