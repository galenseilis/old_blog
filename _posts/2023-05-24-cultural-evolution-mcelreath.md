---
title: Notes On The Problem With Cultural Evolution
categories: [cultural-evolution]
tags: [richard-mcelreath,cultural-evolution]
math: true
mermaid: true
---


This post is about a fascinating talk about Richard McElreath. I've taken some notes below which focus on some of the general statistical and causal points which I think would transfer to other areas I am interested in.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ez3o3uWRSyY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- Bandwagon concept
  - [The Bandwagon (Shannon 1956)](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1056774)
  - They are systemic
  - Severity depends on the discipline
- Systemic Problems
  - Poor knowledge of and integration with theory
  - Methological sloppiness
  - Analytical ignorance
      - A lot of the data is observational and the wrong statistical tools are being used.
  - Exaggeration, evolutionary storytelling
    - [Observational equivalence](https://en.wikipedia.org/wiki/Observational_equivalence) is a problem for many evolutionary stories.
    - [Underdetermination](https://en.wikipedia.org/wiki/Underdetermination)
  - Symptoms of poor training, poor standards, betrayal of our students and the public
- Fraud is not the same thing as thing as systemic issues.
  - Individuals are not to blame for systemic issues, nor small teams of people.
    - People are trying to do their best (normally).
    - More rigorous thinking would be helpful.
  - Individuals can be guilty of fraud.
- Ignoring unmeasured confounds is a common problem.
- Sometimes little-to-no validation of the methodology.
- Issues occur with ignoring the relationship between estimate uncertainty and sample size.
- Measurements are not always valid.
- Considering time, or dynamics, is often not done.
  - Many studies are only cross-sectional.
- Experimental or data collection design is sometimes ignored.
- Sometimes definitions are inconsistent.
- Sometimes the measurements of model/theory performance are arbitrary.
- In many cases there is not a sensible null model, making various forms of null-hypothesis testing dubious in those cases.
  - Instead we should be developing generative models of how we think the phenomena works.
  - Should compare plausible models rather than null models.
- Some data sets are too noisy to make a useful inference from.
- PNAS is not a rigorously peer-reviewed journal even though it is a popular venue.
- The literature is not a pile of facts.
- Retraction should not be shameful, and not every paper which is retracted is due to fraud.
- Mistreatment of missing values is a concern for the validty of some studies.
  - E.g. replacing missing values by zero is not a usesful default.
  - The appropriate way to handle missing data depends on what causes it to go missing.
    - A causal model is needed to rigorously address missingness.
    - In some cases the causal relations imply that missingness *cannot* be accounted for rigorously.
- *Verschlimmbesserung* is when you try to improve something and you make it worse.
- Forecasting alone is not a substitute for causal inference.
- There is a difference between process error and observation error which is sometimes ignored.
  - E.g. A system of stochastic differential equations have their own process noise that must be accounted for when simulating the system. But then taking an observation/measurement itself can introduce noise that should be accounted for as well.
  - Observation error does not propogate whereas process error does.
- Akaike's information criterion and similar metrics do not account for any aspect of causality, so selecting models based on them does not generally give the best causal model even if it gives the most predictive model among a collection of models.
- Using principal components in a regression model reduces the interpretability of the model, and doesn't make any consideration of causality.
- Events that are thousands of years apart are less likely, if not never, to be the direct causal effect of something today. There should be some kind of mediator variable to represent intermediate effects.
  - Although I agree with that, isn't there are weird gaps argument we need to avoid? If I have X->Y and I change that to X->L->Y, what stops me from thinking there should be even more intermediates? My guess is additional latent variables might not be statistically identifiable but I should double check that.
- Data duplication can be a problem. Sometimes statistics are performed in way that ignores that the observations are statisitcally dependent with one another.
  - Mixed effects and stochastic processes such as Gaussian processes can allow for some forms of dependence.
  - Otherwise the statistical power can be massively inflated.
- Just having lots of data does not remedy many of the issues that come up in statistical and causal analysis.
- See [Acharya, Blackwell and Sen 2016](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/explaining-causal-findings-without-bias-detecting-and-assessing-direct-effects/D11BEB8666E913A0DCD7D0B9872F5D11) for a paper that strongly emphasizes addressing confounds.
- Sometimes we use tree models when the real phenomena is not a single tree in its abstract structure
  - e.g. biological evolution
    - i.e. incomplete lineage sorting
  - e.g. language trees
  - Coloring trees with properties that give invalid inferences for when traits evolved.
  - This doesn't make trees irrelevant. They can still be informative.
- Important to remember that some of our abstractions (e.g. trees or social networks) don't exist.
  - Actually, I don't agree with this. I think that they must exist in some sense. But sure, they're maps for a territory. They're models that do not capture everything about the phenomena we're interested in.
- Moto: Honest methods for modest questions
  - Sometimes we can be deincentivised for being honest.
- Simple 4-step plan for honest cultural evolutions sch...
  1. What are we trying to learn?
  2. What is the ideal data for doing so? PROVE WITH A NON-NULL MODEL, NOT RHETOTIC.
  3. What data do we have or can get?
  4. What causes the differences between (2) and (3)?
  5. [Optional] Is there a statistical way to use (2-4) to do (1)? VALIDATE WITH SYNTHETIC DATA.
