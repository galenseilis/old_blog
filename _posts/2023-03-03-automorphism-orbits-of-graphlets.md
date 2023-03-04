---
title: Automorphism Orbits of Graphlets
date: 2023-03-03 23:13:12 -0800
categories: [math,graph-theory,graphlets,automorphism-orbits-of-graphlets]
tags: [math,graph-theory,graphlets,automorphism-orbits-of-graphlets,automorphism,isomorphism,graph,relation,binary-relation,sets,vertices,edges,subset,cartesian-product,networks,directed-graph,digraph,signed-graph,weighted-graph,simple-graph,functions,injective-functions,surjective-functions,bijections,graph-isomorphism,graph-automorphism,equivalence-relation,reflexive-relatoin,symmetric-relation,transitive-relation,equivalence-class,vertex-orbit-automorphism,permutation-group,]
math: true
mermaid: true
---

Back in May 2020 I release a video for the HackSeq event:

{% include embed/youtube.html id='vY1UkCPSKH8' %}

But I figure I could give some written description as well, which is what the rest of this blog post covers.

A [graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)) is a [2-tuple](https://en.wikipedia.org/wiki/Tuple) containing a [set](https://en.wikipedia.org/wiki/Set_(mathematics)) of [edges](https://mathworld.wolfram.com/GraphEdge.html) and a set of [vertices](https://en.wikipedia.org/wiki/Vertex_(graph_theory)), and the [set](https://mathworld.wolfram.com/Set.html) of [edges](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms#edge) is a [subset](https://en.wikipedia.org/wiki/Subset) of the [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) of the set of [vertices](https://mathworld.wolfram.com/GraphVertex.html) with itself. We can think the [vertices](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms#vertex) as 'things' and the set of edges as a [binary relation](https://en.wikipedia.org/wiki/Binary_relation) between them.

Sometimes graphs are called "[networks](https://en.wikipedia.org/wiki/Network_theory)" when either the vertices (often called "nodes" when discussing networks) or edges have additional attributes, however this usage is not universally accepted. Three common properties of graph edges are whether they are directed, signed, or weighted. In the case of directed edges, some sort of 'directionality' is associated with the edges, and we'd say that *(u,v)* and *(v,u)* are considered distinct for two vertices *u* and *v* from the graph. A graph with directed edges is called a [directed graph](https://en.wikipedia.org/wiki/Directed_graph) or a [digraph](https://mathworld.wolfram.com/DirectedGraph.html). In the case of signed edges, each edge is assigned a 'positive' or 'negative' value, and we call such a graph a [signed graph](https://en.wikipedia.org/wiki/Signed_graph). In the case of weighted edges, each edge is assigned a numerical value, and we call such a graph a [weighted graph](https://mathworld.wolfram.com/WeightedGraph.html). If a graph doesn't have directed, signed, or weighted edges and doesn't have multiple edges for any given pair of vertices, then it is called a [simple graph](https://mathworld.wolfram.com/SimpleGraph.html).

A [graphlet](https://en.wikipedia.org/wiki/Graphlets) is a specific type of graph, inheriting all the properties of graphs but also being a [weakly-connected](https://mathworld.wolfram.com/ConnectedGraph.html) [induced subgraph](https://en.wikipedia.org/wiki/Induced_subgraph). For a graph to be [subgraph](https://mathworld.wolfram.com/Subgraph.html), there exists another graph such that the subgraph's vertex set is a subset of the other graph's vertex set and the subgraph's edge set is a subset of the other graph's edge set. A subgraph being induced can be thought of procedurally, by first selecting any subset of the vertices and then also selecting all edges that connect those selected vertices. The property of weakly-connected can be considered for any graph, and means that there exists a path between any pair of vertices in the graph.

A function is [injective](https://mathworld.wolfram.com/Injection.html) if it satisfies that *f(x)=f(y)* implies that *x=y*.

![https://mathworld.wolfram.com/images/eps-gif/Injection_1000.gif](https://mathworld.wolfram.com/images/eps-gif/Injection_1000.gif)

A function is [surjective](https://mathworld.wolfram.com/Surjection.html) if it satisfies for any element *b* in the image that there exists an element *a* of the domain for which *b=f(a)*. 

![https://mathworld.wolfram.com/images/eps-gif/Surjection_1000.gif](https://mathworld.wolfram.com/images/eps-gif/Surjection_1000.gif)

A [bijection](https://en.wikipedia.org/wiki/Bijection) is a [function](https://en.wikipedia.org/wiki/Function_(mathematics)) that is both [injective (one-to-one)](https://en.wikipedia.org/wiki/Injective_function) and [surjective (onto)](https://en.wikipedia.org/wiki/Surjective_function) from one set to another (these two sets can be the same set).

![https://mathworld.wolfram.com/images/eps-gif/Bijection_1000.gif](https://mathworld.wolfram.com/images/eps-gif/Bijection_1000.gif)

A [graph isomorphism](https://en.wikipedia.org/wiki/Graph_isomorphism) is a [bijection](https://mathworld.wolfram.com/Bijection.html) *f* between two graphs (which can be the same graph in the case of graph automorphisms) such that any two vertices *u* and *v* in the first graph are adjacent *if-and-only-if* *f(u)* and *f(v)* are adjacent. 

![https://upload.wikimedia.org/wikipedia/commons/9/9a/Graph_isomorphism_a.svg](https://upload.wikimedia.org/wikipedia/commons/9/9a/Graph_isomorphism_a.svg) ![https://upload.wikimedia.org/wikipedia/commons/8/84/Graph_isomorphism_b.svg](https://upload.wikimedia.org/wikipedia/commons/8/84/Graph_isomorphism_b.svg)

A [graph automorphism](https://mathworld.wolfram.com/GraphAutomorphism.html) is a [graph isomorphism](https://en.wikipedia.org/wiki/Graph_isomorphism) where the domain graph and the image graph are the same graph.

![https://mathworld.wolfram.com/images/eps-gif/GraphAutomorphismGridGraph_1000.gif](https://mathworld.wolfram.com/images/eps-gif/GraphAutomorphismGridGraph_1000.gif)

An [equivalence relation](https://mathworld.wolfram.com/EquivalenceRelation.html) is a [binary relation](https://mathworld.wolfram.com/BinaryRelation.html) that is [reflexive](https://en.wikipedia.org/wiki/Reflexive_relation), [symmetric](https://en.wikipedia.org/wiki/Symmetric_relation), and [transitive](https://en.wikipedia.org/wiki/Transitive_relation). An [equivalence class](https://mathworld.wolfram.com/EquivalenceClass.html) is a subset of a set such that all members of the subset adhere to an [equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation). A [(vertex) orbit automorphism](http://www.cs.columbia.edu/~cs4203/files/GT-Lec2.pdf) is an [equivalence class](https://en.wikipedia.org/wiki/Equivalence_class) from the vertex set of a graph under the action of a [graph automorphism](https://en.wikipedia.org/wiki/Graph_automorphism). Multiple graph automorphisms are possible, and the set of all automorphisms with composition of permutations of the vertex set is called a [permutation group](http://vlsicad.eecs.umich.edu/BK/SAUCY/papers/Cameron2001.pdf).

Since graphlets are graphs, and orbit automorphisms can be found within graphs, we can find orbit automorphisms within graphlets. The idea behind enumeration of orbit automorphisms of graphlets is to count the number of times each vertex of a graph participates in each orbit automorphism of each graphlet from a set of graphlets. While each finite graph has a finite number of distinct (i.e. mutually non-isomorphic) graphlets, considering every conceivable graphlet would be computationally infeasible. Instead of considering all graphlets of a graph, a constraint is often imposed where graphlets containing only 2-3 vertices are considered.

Enumeration of orbit automorphisms of graphlets has been used to [characterize correlation networks of coexpression of genes](https://asonamdata.com/ASONAM2019_Proceedings/pdf/papers/105_0613_135.pdf), and [characterize the role of traders in the world trade network](https://www.nature.com/articles/srep35098). 
