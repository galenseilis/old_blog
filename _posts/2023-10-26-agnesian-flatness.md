---
title: Agnesian Flatness
date: 2023-10-26 00:51:15
categories: [mathematics,calculus,agnesian-operator,agnesian-flatness]
tags: [mathematics,calculus,agnesian-operator,agnesian-flatness,operators,arithmetic-mean,geometric-mean,am-gm-inequality,agnesian,power-spectrum,spectral-flatness]
math: true
mermaid: true
---

Inspired by [spectral flatness](https://en.wikipedia.org/wiki/Spectral_flatness)as an application of the [inequality between the geometric mean and arithmetic mean](https://en.wikipedia.org/wiki/AM-GM_Inequality), I decided to define something analogous in terms of the Agnesian operator rather than magnitudes from the power spectrum. The Agnesian flatness of order $$k$$ for a collection of functions $$S$$ parametrized by $$t$$ where $$\|S\| = n$$ is given by

$$F_{t}^{k}[S] \triangleq\frac{\sqrt[n]{\prod_{j=1}^n \mathcal{A}_t^k [S]}}{\sum_{j=1}^n \mathcal{A}_t^k[\{ x_j(t) \}]}$$

where $\mathcal{A}_t^k$ denotes the Agnesian as defined in [Seilis 2022](https://doi.org/10.24124/2022/59312 ).
