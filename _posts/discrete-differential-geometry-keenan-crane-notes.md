

## What are some applications of differential geoemtry?

- [Geometry processing](https://en.wikipedia.org/wiki/Geometry_processing).
- Shape analysis.
- Representations in machine learning.
    - Computer vision
- Numerical simulation.
- Architecture and design.
    - Industrial design.
    - Fashion
- Discrete models of nature.
    - Computational biology
    - Computational mechanics
    - Medical imaging

> Often, under mild assumptions, having a function in the form $f(x) = 0$ implies a [manifold](https://en.wikipedia.org/wiki/Manifold) structure.
{: .prompt-tip }

## What is differential geometry (DG)?

- DF is a language for talking about local properties of shape.
    - e.g. How fast are we travelling along a curve?
    - e.g. How much does a surface bend at a point?
- DG also allows us to connect local notions of shape to global properties of shape.
    - i.e. "local-global" relationships, such as the curvature of a boundary being related to the number of topological holes in a manifold.
- DG is an integral part (pun intended) of geometry, physics, and statistics.
- DG has had a large impact on scientific and industrial development in the 20th century.

## What is discrete differential geometry (DDG)?

- DDG is a language for talking about local properties of shape.
- Certain notions of infinity, derivatives, and infinitesimals are not within its scope.
- Everything is expressed in terms of countably-many lengths and angles.
- Surprisingly little is lost in what can be said in DG when translated into DDG.
    - DDG faithfully captures many of the same notions as DG.
- DDG is becoming a modern language for geometric computing.
- DDG is having an increasing impact on science and technology in the 21st century.

## What is the grand vision for DDG?

The grand vision of DDG is to translate differential geometry into a language that is suitable for computation.

## How can notions from DG be translated into DDG?

A common strategy is taken to obtain discrete notions from continuous/smooth ones:
1. Write down several equivalent definitions in the smooth setting.
2. Apply each smooth definition to an object in the discrete setting.
    - i.e. take a notion like curvature of sphere and attempt to then describe the curvature of a polygon.
3. Determine which properties are captured by each resulting inequivalent discrete definition.

Often we encounter "no free lunch" scenarios in the sense that no single discrete definition captures all properties of its smooth counterpart. This is similar to the notion of a [no free lunch theorem](https://en.wikipedia.org/wiki/No_free_lunch_theorem) and the phrase "*[There ain't no such thing as a free lunch](https://en.wikipedia.org/wiki/No_such_thing_as_a_free_lunch)*". If our goal is to represent definitions of smooth structures with discrete structures, we will have to accept some amount of [Pareto efficiency](https://en.wikipedia.org/wiki/Pareto_efficiency).

## Example: Discrete curvature of plane curves

Let us consider a toy example involving the curvature of plane curves.

We must first consider what "curvature" is. In colloqial usage, it means how much something bends. 

Following the strategy outlined earlier, we will first review the smooth definition, and then try to translate the smooth notion to the discrete setting. What we'll find is that there are multiple notions of discrete curvature that are non-equivalent but each preserve different aspects of smooth curvature. 

When we have multiple notions with tradeoffs, we will have to choose which ones we wish to procede with based on the problem we're trying to address with DDG.

### Why do we care about curvature?
Let's take a step back for a moment. Why would we want to talk about curvature? Curvature describes how ordinary objects like rulers, textiles, and biological tissues bend. In image processing curvature can help with segmentation. In physical biochemistry we might be interested in supercoiling of macromolecules.

### What is a parametric curve?

In the smooth setting, a **parametrized curve** is a "nice" map $\gamma$ taking each point in an interval $[0,l]$ of the real line to some point in the plane $\mathbb{R^2}$, which is often denoted $\gamma : [0, l] \mapsto \mathbb{R}^2$. What "nice" usually means is that sufficient conditions on the type of [continuity](https://en.wikipedia.org/wiki/Continuous_function) and [smoothness](https://en.wikipedia.org/wiki/Smoothness) allow for what we're trying to accomplish. I won't delve into these cases unless their discussion is needed.

#### Example: Parametrization of a circle

A circle can be represented with a parametrization

$$\gamma : [0, 2 \pi ) \mapsto \mathbb{R}^2$$

$$s \mapsto (\cos (s), \sin (s) )$$

which has symmetric points such as $$\gamma (0) = \gamma (2 \pi) .$$

### What is a discrete curve?

A discrete curve is a [*piecewise linear* parametrized curve](https://en.wikipedia.org/wiki/Polygonal_chain). It is a sequence of vertices connected by straight line segments embedded in some ambient space.

Further it means that if the discrete curve is parametrized over an interval $[0, l]$ then there is an [interval partition](https://en.wikipedia.org/wiki/Partition_of_an_interval) where the boundaries of the subintervals are defined by the preimage of the discrete curve where there exists vertices.

#### Example of a discrete curve on the plane

Here is a simple example of a discrete curve on the plane parametrized over the interval $[0, 2]$:

$$\gamma (s) := \begin{cases} (s, 0) & 0 \leq s \leq 1 \\ 1 < s \leq 2 \end{cases}$$

### What is the tangent of a curve on the plane?

An informal description is that the tangent of a curve on the plane is a vector that just barely grazes the curve.

More formally, a unit tangent (or just tangent) of a parametrized curve is a map obtained by normalizing its first derivative in the following way:

$$T_{\gamma}(s) = \frac{\frac{d}{ds} \gamma}{\Vert \frac{d}{ds} \gamma (s) \Vert}$$

Notice that the derivative cannot be zero for the unit tangent vector to be defined. This is sometimes called a "regularity condition", and of curves it is called a "regular curve".

A common assumption to make is to take the curve to be arc-length parametrized, which simplifies the above to

$$T(s) := \frac{d}{ds} \gamma (s).$$

This does mean that if you are starting with a parametric curve that is not arc-length parametrized, then you'll need to arc-length parametrize it.

#### Example of computing the unit tangent of a circle

Suppose we have this parametrization of a circle:

$$\gamma : [0, 2 \pi ) \mapsto \mathbb{R}^2$$

$$s \mapsto (\cos s, \sin s).$$

First, we compute the derivative of the curve with respect to its parameter:

$$\frac{d}{ds} \gamma (s) = (- \sin s, \cos s)$$

Second, we will normalize the derivative of the curve. The normalization is just the norm (usually 2-norm) of the derivative itself:

$$\Vert \frac{d}{ds} \gamma (s) \Vert = \sqrt{\cos^2 s + \sin^2 s} = \sqrt{1} = 1.$$

Since 

$$T_{\gamma}(s) = \frac{1}{1} (- \sin s, \cos s) = (- \sin s, \cos s)$$

we have learned that our parametrization is already arc-length parametrized.

### What is a normal vector to a curve?

A vector is normal to a curve if it "sticks straight out" from the curve.

More formally, the unit normal (or just normal) can be expressed as a quarter-rotation $\mathcal{J}$ of the unit tangent in the counter-clockwise direction. This is denoted by:

$$N(s) := \mathcal{J}T(s)$$

where we can reprsent $\mathcal{J}$ as a [rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix).

This definition is almost the same as saying that the unit normal is any vector which is orthonogal to the tangent, but it actually specifies a specific vector rather than just any vector. Recall that for a planar curve there will be two opposite vectors that are orthogonal to the tangent vector at a point in a curve. If you go up into 3-dimensional ambient space, or higher, you will typically have an infinite number of normal vectors to a curve.

In coordinate form, this can be written:

$$(x,y) \overset{\mathcal{J}}{\mapsto} (-y, x)$$

#### Example: Computing the unit normal of a circle

Supposing our parametrization of a circle from earlier, and the unit tanget vector from both, we can write the unit tangent vector as:

$$N(s) = \mathcal{J}T(s) = (- \cos s, - \sin s).$$

The image of $N$ comprises a set of vectors that all point toward the center of the circle. Does this apply to [n-spheres](https://en.wikipedia.org/wiki/Sphere)?

Notice that would have been logically-consistent to adopt a different definition $N  = \mathcal{J}T$ which would have chosen the opposite set of vectors that point away from the center of the circle. What's more important is to pick one definition, or the other, of the unit tangent and apply it consistently.

### What is the curvature of a plane curve?

The curvature is an arc-length parametrized curve that can be expressed as the rate of change of the unit tangent. More explicitly we write this as

$$\kappa (s) \triangleq \langle N(s), \frac{d}{ds} T(s) \rangle$$

where $\langle\bullet,\bullet\rangle$ is an [inner product](https://en.wikipedia.org/wiki/Inner_product_space), which in this setting is the [dot product](https://en.wikipedia.org/wiki/Dot_product).

Knowing that the unit tangent vector is itself the first derivative of the curve, we can also write the curvature like this:

$$\kappa (s) = \langle N(s), \frac{d^2}{ds^2} \gamma (s) \rangle .$$

This leads to a key concept that curvature is closely-related to the second derivative. We can further, based on what we've defined so far, write the curvature like this:

$$\kappa (s) = \langle \mathcal{J}\frac{d}{ds} \gamma (s), \frac{d^2}{ds^2} \gamma (s) \rangle .$$


The reason we take this second derivative and multiply it by the unit normal vector is to preserve the sign of the derivative. If we instead took the norm of the second derivative we would lose this sign. What does the sign tell us? It tells us about orientation, especially in the sense of what direction the curve is turning toward.

### Directly translating the curvature of a planar curve to the discrete setting

We run into a couple of immediate issues if we try to directly apply the definition of curvature as we have developer it to a discrete curve. At the vertices of the discrete curve we find that the curvature is undefined (naively, we might say infinite), and between the vertices it is zero (which is not wrong but it also isn't interesting). Maybe further work at the vertices could lead to something useful in terms of [Dirac delta distributions](https://en.wikipedia.org/wiki/Dirac_delta_function), but in some sense that still wouldn't solve what we want to know. We want some description of curvature that is finite and interesting.

We need to think about when a discrete definition is "good".

### What makes a discrete definition "good"?

- It should satisfy at least some of the key properties or theorems that we have in the smooth setting.
  - e.g. $\int_{\partial U} k ds = 2 \pi (n+1)$
- There should be some convergence criteria so that the discrete case gets arbitrarily close to the smooth definition in its properties when we have finely-detailed discrete structures.
- Calculations with the discrete defintiion should be efficient to compute and/or helpful in solving equations.

### Playing the game of developing discrete curvature
- In the smooth setting there are several equivalent definitions of curvature.
  - Turning angle
  - Length variation
  - Steiner formula
  - Osculating circle
- The key idea here is to use these different notions of curvature in the smooth setting as starting ponts for defining quantities in the discrete setting.
- In general we cannot guarantee that all such starting points will be interesting/useful/coherent, but in this case all four of the notions listed above will lead to workable definitions of discrete curvature.

#### Turning angle as a discrete curvature

- Our initial definition of curvature as the *rate of change of the tangent in the noraml direction*.
  - $\kappa (s) = \langle N(s), \frac{d}{ds} \gamma (s) \rangle$
- We can equivalently measure the rate of change of the angle the tangent makes with the horizonal:
  - $\kappa (s) = \frac{d}{ds} \phi (s)$, where $\phi (s)$ is the angle from the horizontal (i.e. in ambient space) to the tangent vector.
  - This angle is not itself coordinate-free.
- This definition still requires a first derivative, so we still cannot directly calculate curvature from a discrete curve.
- We can consider the integral of the curvature along a line segment of a curve:
  - $\int_{a}^{b} \kappa (s) ds = \int_{a}^{b} \frac{d}{ds} \phi (s) ds = \phi (b) - \phi (a)$
    - This result is a consequence of the fundamental theorem of calculus.
- While we cannot compute derivatives in the discrete setting, we can compute differences in angles!
- Note that we get translation symmetries. If we translate two angles by the same amount, then their difference will be the same as if we had not translated them.
  - $(\phi_2 + \alpha ) - (\phi_2 + \alpha) = \phi_2 - \phi_1$

For three sequentially adjacent vertices in the discrete curve, their turning angle can be written as

$$\theta_i := \text{angle}(\gamma_i - \gamma_{i-1}, \gamma_{i+1} - \gamma_i).$$

Our turning angle defintion of discrete curvature at vertice $i$ is simply:

$$\kappa^A_i \triangleq \theta_i$$

Note that it is a common theme for discrete quantities to be integrated from the curve rather than pointwise values. Here we were considering the total change in the angle, rather than the derivative of the angle.

#### Length variation as a discrete curvature

The motivation for using the length variation as a starting pont for defining a discrete curvature is the following fact from the smooth setting:

The fastest way to decrease the length of a curve is to move it in the normal direction, with speed proportional to curvature.

To build intuition for this, consider a flat region of a curve. The normal motion is not changing with the length of the curve within this region. If you instead consider a curved region, like a circle, there is a change in length.

Formally, let us consider an mostly arbitrary change to the curve $\gamma$, which is given by the function 

$$\nu : [0,l] \mapsto \mathbb{R}^2$$

with

$$\nu(0) = \nu(l) = 0$$

as a constraint on change function. This is kind of like a [bump function](https://en.wikipedia.org/wiki/Bump_function), but we have not imposed the additional criteria of a bump function (such as smoothness).

We can write our changed curve like this

$$\gamma + \epsilon \nu$$

where $\epsilon \in \mathbb{R}_{>0}$. The parameter $\epsilon$ allows us to arbitrarily control how much $\nu$ is changing the arc length of the resulting curve in a smooth way:

$$\frac{d}{d \epsilon} \text{length}(\gamma + \epsilon \nu)$$
