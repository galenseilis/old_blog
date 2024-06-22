

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

### What is a param

In the smooth setting, a **parametrized curve** is a map taking each point in an interval $[0,l]$ of the real line to some point in the plane $\mathbb{R^2}$.
