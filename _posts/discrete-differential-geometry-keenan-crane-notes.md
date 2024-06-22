

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

This definition is almost the same as saying that the unit normal is any vector which is orthonogal to the tangent, but it actually specifies a specific vector rather than just any vector. Recall that for a planar curve there will be two opposite vectors that are orthogonal to the tangent vector at a point in a curve.

In coordinate form, this can be written:

$$(x,y) \overset{\mathcal{J}}{\mapsto} (-y, x)$$
