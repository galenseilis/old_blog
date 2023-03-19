 
I've been trying to come up with a useful default for a sine wave.

Suppose I have the following incomplete model 

$S_t = \alpha \sin \left( 2 \pi (\phi t - \beta) \right) + \gamma + \epsilon$

and I would like to select priors for $\alpha, \beta, \gamma, \epsilon$. 

I want to assume that 
- $\alpha \geq 0$ and $\alpha \in \mathbb{R}$, 
- $\phi \geq 0$ and $\phi \in \mathbb{R}$, 
- $\beta \in [0, 1]$  and $\beta \in \mathbb{R}$, 
- $\gamma \in \mathbb{R}$,
- and $\epsilon \in \mathbb{R}$ and $\mathbb{E}[\epsilon] =0$.

Here is my thinking so far.

Allowing $\alpha = 0$ and $\phi = 0$ would allow me to put exponential priors on them. I've found that exponential priors were useful defaults in Bayesian CP-decomposition. Maybe this is due to the exponential distribution being the maximum entropy distribution with fixed finite mean on real non-negative support.

I'm tempted to put a beta distribution on $\beta$, but I'm not entirely satisfied with the shapes. Choosing something like $\beta \sim \operatorname{Beta}(2,2)$ would suggest a prior belief that zero phase shift is extremely unlikely, which in some cases could be right. But a uniform distribution also feels tempting here since I really don't have any preferences on the phase shift.

The parameter $\gamma$ is essentially an intercept, which is intended to vertically place the sine wave. Since I am imagining that the model is just meant to model a sine wave with some stationary noise, that the vertical position of the wave should be constant in the population, it makes sense to pick a normal distribution. A normal distribution is the maximum entropy distribution over the reals with fixed mean and variance. Taking a large standard deviation and mean zero might be a useful default without knowing anything further about the problem.

The parameter $\epsilon$ I am thinking would also be normally-distributed, representing IID measurement error. A normal distribution with mean zero makes sense to me here.
 
