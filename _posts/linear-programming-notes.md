Introduction to Linear Programming

Etymology of Linear Programming
- 1950s: Programming is a form of planning utilized by the British military.
- Better name: "planning with linear constraints"


> **Example**
>
> Transporting goods through a transportation network. Suppose you have a graph whose edges are locations and edges are transportation routes. The edges are weighted by the capacity, which provide constraints.

- The previous example may not have a unique optimal solution, but finding at least one optimal solution can be valuable.
- The previous example doens't include time, but sometimes travel times can be an important factor in optimal planning. I think this would involve adding more constraints and that the terms may be a function of time.
- The previous examples put bounds on the edges. Sometimes we would like to put bounds on the vertices in some sense.
    - For an edge $a$ we can consider the flow through that edge $x_a$ to have constraints $-3 \leq x_a \leq 3$ where $\pm 3$ is the capacity constraint.
- Inequality constraints can be converted to equality constraints.
- Equality constraints are allowed.

> **Example**
>
> Maximize $x_1 + x_2$ for $x_1, x_2 \in \mathbb{R}$ satisfying
> $x_1 \geq 0$
> $x_2 \geq 0$
> $-x_1 + x_2 \leq 1$
> $x_1 + 6x_2 \leq 15$
> $4x_1 -x_2 \leq 10$

```python
from scipy.optimize import linprog
```


> **Definition**
>
> The **objective** is the function to be optimized. 


- Not all constraints affect the feasible region of a problem.

# References
- [Linear Programming 2020](https://www.youtube.com/playlist?list=PLDndWhwv4Ujo10_a2T4R4Uqng1nduvfu1)
