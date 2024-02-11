---
title: A Sankey Random Walk with Matplotlib
date: 2024-02-10 03:09:34
categories: [python,matplotlib,sankey-diagram]
tags: [python,sankey-diagram,statistics,visualization,matplotlib,random-walk]
math: true
mermaid: true
---

While looking into programmatically generating [Sankey diagrams](https://en.wikipedia.org/wiki/Sankey_diagram) based on the results of [discrete event simulations](https://en.wikipedia.org/wiki/Discrete-event_simulation) I made up a somewhat absurd programming exercise. Using [`matplotlib.sankey.Sankey`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey) you can draw a [random walk](https://en.wikipedia.org/wiki/Random_walk) as follows:

```python
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
import numpy as np

np.random.seed(2018)

sankey = Sankey()

for i in range(100):
    sankey.add(
        flows=[1, -1],
        orientations=np.random.randint(-1, 2, size=2).tolist(),
        prior=None if not i else i - 1,
        connect=None if not i else (1, 0),
        labels=None,
    )

sankey.finish()

plt.axis("off")

plt.tight_layout()

plt.savefig('sankey_random_walk.png', dpi=300, transparent=True)

plt.close()
```

Here is the plot:

![](/assets/images/sankey_random_walk.png)

It is kind of pretty in my opinion.


