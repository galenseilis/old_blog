---
title: Spearman Correlation Quantifies Comonotonicity
date: 2023-03-10 20:50:15
categories: [statistics,rank-based-statistics,spearman-correlation]
tags: [statistics,rank-based-statistics,spearman-correlation]
math: true
mermaid: true
---

This post is part of a collection of posts responding to various aspects of the following video:

{% include embed/youtube.html id='qee6b7vl2O0' %}

In this video Dustin quotes me:

> **Quotation** (Galen Seilis)
But the short versoin of my own opinion is that the rank transform preserves monotonicity, and estimators such as Spearman's correlation tell us about comonotonicity of pairs of variables without the difficulties that come with modeling.

Dustin agreed with me that *the rank transform preserves monotonicity*, and by that we meant that ranks are order-preserving on the elements of a sample, but Dustin did not make any further comment on whether he agreed or disagreed that Spearman's rank correlation quantifies comonotonicity. I think the point I was making about comonotonicity is worth unpacking and emphasizing further.

Comonotonicity is a description of a pair (or collection) of variables which go up and down together. Similarly, antimonotonicity is a description a pair of variables in which one increasing implies that the other is decreasing, and vice versa. Well, these are informal descriptions anyway. For further reading on more precisely-defined notions of comonotonicity see [Puccetti & Scarsini 2009](https://www.parisschoolofeconomics.eu/IMG/pdf/MED090320-Scarsini.pdf), but I will continue here with a less precise and more intuitive exposition.

Suppse you have four continuous random variables $\{X_1, \ldots, X_4 \}$ representing an IID sample. You take a sample, you see four numbers, and you rank them. Since there is zero probability of tied ranks, you see that the ranks are always turn out to be a permutation of $(1,2,3,4)$. Here they are tabulated:

|   $\operatorname{rank}(X_1)$ |   $\operatorname{rank}(X_2)$ |   $\operatorname{rank}(X_3)$ |   $\operatorname{rank}(X_4)$ |
|-----------------------------:|-----------------------------:|-----------------------------:|-----------------------------:|
|                            1 |                            2 |                            3 |                            4 |
|                            1 |                            2 |                            4 |                            3 |
|                            1 |                            3 |                            2 |                            4 |
|                            1 |                            3 |                            4 |                            2 |
|                            1 |                            4 |                            2 |                            3 |
|                            1 |                            4 |                            3 |                            2 |
|                            2 |                            1 |                            3 |                            4 |
|                            2 |                            1 |                            4 |                            3 |
|                            2 |                            3 |                            1 |                            4 |
|                            2 |                            3 |                            4 |                            1 |
|                            2 |                            4 |                            1 |                            3 |
|                            2 |                            4 |                            3 |                            1 |
|                            3 |                            1 |                            2 |                            4 |
|                            3 |                            1 |                            4 |                            2 |
|                            3 |                            2 |                            1 |                            4 |
|                            3 |                            2 |                            4 |                            1 |
|                            3 |                            4 |                            1 |                            2 |
|                            3 |                            4 |                            2 |                            1 |
|                            4 |                            1 |                            2 |                            3 |
|                            4 |                            1 |                            3 |                            2 |
|                            4 |                            2 |                            1 |                            3 |
|                            4 |                            2 |                            3 |                            1 |
|                            4 |                            3 |                            1 |                            2 |
|                            4 |                            3 |                            2 |                            1 |


If you're interested in tinkering, the above table is generated by the following code.

```python
from itertools import permutations

import pandas as pd

perms = list(permutations(range(1,5)))
cols = [f'$\\operatorname{{rank}}(X_{i})$' for i in range(1,5)]
df = pd.DataFrame(data=perms, columns=cols)
print(df.to_markdown(index=False))
```

Now what if you actually have paired samples of such continuous random variables $\{(X_1, Y_1), \ldots, (X_1, Y_1) \}$? As before each rank of an element of the sample gets a score in $\{ 1, \ldots, 4 \}$ but now there are various ways that these integers get paired together. This rank space is like a checker board. There are $4!=24$ possible arrangments of ranks for a bijection $\{1, 2, 3, 4\} \mapsto \{1, 2, 3, 4\}$. In the following visualization I show yellow squares indicating a pair is a member of the relation, i.e. function, and otherwise it is not a member of the relation. Or more plainly, this is a visualization of all of the samples that could (almost-surely) be realized.

![](/assets/images/perm_grid.png)

If you would like to tinker with the figure, here is the source.

```python
from itertools import permutations

import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import pearsonr
corr = lambda x,y: pearsonr(x,y)[0]

fig, axes = plt.subplots(6,4)
axes = axes.flatten()

x = list(range(1,5))
perms = permutations(x)
for k, y in enumerate(perms):
    img = np.zeros((4,4))
    for i,j in zip(x,y):
        img[i-1,j-1] = 1
    axes[k].imshow(img, origin='lower')
    axes[k].axis('off')
    
axes = axes.reshape((6,4))
plt.tight_layout()
plt.savefig("perm_grid.png", bbox_inches='tight', dpi=300, transparent=True)
plt.close()
```

