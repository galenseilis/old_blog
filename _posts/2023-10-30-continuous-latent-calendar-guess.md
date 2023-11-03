---
title: Divergence of the Neutrosophic Differential Operator
date: 2023-10-24 00:51:15
categories: [math,neutrosophic-numbers]
tags: [math,neutrosophic-numbers,arithmetic,linear-algebra,linear-functional,differential-operator,vectors,vector-functions,divergence,calculus,multivariable-calculus]
math: true
mermaid: true
---


In a [recent post](https://galenseilis.github.io/posts/arithmetic-neutrosophic-numbers-vector-functions/) I introduced the following differential operator:

$$\vec \nabla \dot \star \vec v(x,y) \triangleq \begin{bmatrix} \frac{\partial}{\partial x} g(x,y) \\ \frac{\partial}{\partial x}h(x,y) + \frac{\partial}{\partial y}g(x,y) + \frac{\partial}{\partial y}h(x,y) \end{bmatrix}$$

It has a divergence of:

$$\nabla \cdot \left[ \vec \nabla \dot \star \vec v(x,y) \right] = \nabla \cdot \begin{bmatrix} \frac{\partial}{\partial x} g(x,y) \\ \frac{\partial}{\partial x}h(x,y) + \frac{\partial}{\partial y}g(x,y) + \frac{\partial}{\partial y}h(x,y) \end{bmatrix}$$
$$\nabla \cdot \left[ \vec \nabla \dot \star \vec v(x,y) \right] = \frac{\partial^2}{\partial x^2} g(x,y) + \frac{\partial^2}{\partial x \partial y} h(x,y) + \frac{\partial^2}{\partial y^2} g(x,y) + \frac{\partial^2}{\partial y^2} h(x,y)$$
