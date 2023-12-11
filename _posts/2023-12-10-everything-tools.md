---
title: Developing Everything Tools
date: 2023-12-10 12:51:15
categories: [software, software-frameworks]
tags: [software, software-frameworks, software-development, software-bloat, programming-complexity, abstraction, reusability]
math: true
mermaid: true
---

I have been thinking about development software archicture and reading from [Architecture Patterns with Python](https://www.oreilly.com/library/view/architecture-patterns-with/9781492052197/) and thinking about what goes wrong with programming larger programs and what to do about it.

There is something enticing about abstraction and generalization. As a mathematics nerd it is certainly appealing to find such abstractions, but there is a well-known tendency for highly-abstracted software to come with its own challenges. Building ever-more general programs often inadvertantly leads to [programming complexity](https://en.wikipedia.org/wiki/Programming_complexity) and [software bloat](https://en.wikipedia.org/wiki/Software_bloat).

A humorous example of software bloat is given in the form of [Zawinski's Law](https://en.wikipedia.org/wiki/Jamie_Zawinski#Zawinski's_Law):

> Every program attempts to expand until it can read mail. Those programs which cannot so expand are replaced by ones which can.

A recent YouTube video made some claims that resonate with me:

<iframe width="560" height="315" src="https://www.youtube.com/embed/OXq7NAPxLVU?si=hykYCCRlxFqQUjse" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

> I would say that building a product and having someone attempt to abstract the product to be able to fit every need possible, and as new needs and unforseen challenges arise, you more a design that was not designed with that in mind to fit it in. And you do that over years. And what ends up happening is it becomes an untenable mess.
>
> It's one of my big problems with reusability and abstraction. People really do attempt to make everything possible. And when I use these everything-possible abtractions you necessarily you necessarily have to shoe-horn in use cases which just often lead to really wonky items.
>
> I do agree that frameworks need more specialization; less everything. 

Specialization is somewhat under-rated. What does it provide? 

Sometimes performance, which might be key for certain systems. If you don't need to check and handle various possibilities related to a system's state or input then your program can readily move onto other things. 

But for me one of the major selling points is [practical expressivity](https://en.wikipedia.org/wiki/Expressive_power_(computer_science)#Information_description): the concision and ease in which an idea is expressed. Programming tools which are practically expressive often cohere with [DDD](https://en.wikipedia.org/wiki/Domain-driven_design), allowing us to easily translate business problems into code.

The other notion of expressivity, the darker twin of practical expressivity, is theoretical expressivity. Theoretical expressivity can be useful for proving various results about what a system can do, but to make it a goal is a swift fall into the [Turing tarpit](https://en.wikipedia.org/wiki/Turing_tarpit):

> Beware of the Turing tar-pit in which everything is possible but nothing of interest is easy. -- [AP](https://en.wikipedia.org/wiki/Alan_Perlis), [EoP](https://en.wikipedia.org/wiki/Epigrams_on_Programming)

The appeal of maximal abstraction to a programmer is like the siren's calling the sailors into the ocean to be drowned.

![](https://upload.wikimedia.org/wikipedia/commons/a/a3/Draper_Herbert_James_Ulysses_and_the_Sirens.jpg)

Although it has its own shortcomings, there is an appeal to these [summarized Unix philosophy principles](https://en.wikipedia.org/wiki/Unix_philosophy#Origin) as a partial treatment for the disease of unbounded abstraction:

- Write programs that do one thing and do it well.
- Write programs to work together.
- Write programs to handle text streams, because that is a universal interface.


But there doesn't seem to be a magical answer for software development. Vaguely, we need programming tools to be general enough but not too general; abstract but not too abstract. A balance must always be struck. But what is clear to me is that "we need a tool that does everything", an everything tool, is always a bad tool in practice no matter how beautiful it may be in theory.
