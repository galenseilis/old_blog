---
title: Spearman Correlation
date: 
categories: [statistics,rank-based-statistics,spearman-correlation]
tags: [statistics,rank-based-statistics,spearman-correlation]
math: true
mermaid: true
---

 
I feel obliged to discuss how at least one non-parametric rank-based statistic is useful.

> **Quotation** (Galen Seilis)
[...] estimators such as Spearman's correlation tell us about comonotonicity of pairs of variables without the difficulties that come with modeling.

Dustin expressed that "comonotonicity" is a difficult term to pronounce, which is an attidue I am sympathetic to as someone who took an undergraduate course in metabolism. "Phosphoribosylformimino-5-aminoimidazole-4-carboxamide ribonucleotide isomerase", anyone? 

> The site [pronouncewiki](https://www.pronouncekiwi.com/Comonotonic) gives some examples.
{: .prompt-tip}

Dustin did not make any further comment on whether he agreed or disagreed that Spearman's rank correlation quantifies comonotonicity. I think the point I was making about comonotonicity is worth unpacking and emphasizing further.

Comonotonicity is a description of a pair (or collection) of variables which go up and down together. Similarly, antimonotonicity is a description a pair of variables in which one increasing implies that the other is decreasing, and vice versa. Well, these are informal descriptions anyway. For further reading on more precisely-defined notions of comonotonicity see [Puccetti & Scarsini 2009](https://www.parisschoolofeconomics.eu/IMG/pdf/MED090320-Scarsini.pdf), but I will continue here with a less precise and more intuitive exposition.

![](/assets/images/perm_grid.png)

All $4!=24$ possible arrangments of ranks for a bijection $\{1, 2, 3, 4\} \mapsto \{1, 2, 3, 4\}$. Yellow squares indicate a pair is a member of the relation, otherwise it is not a member of the relation.

# Code

```python
from itertools import permutations, product

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
