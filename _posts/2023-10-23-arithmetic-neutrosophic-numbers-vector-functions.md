---
title: Arithmetic of Neutrosophic Numbers as Vector Functions
date: 2023-10-23 00:51:15
categories: [math,neutrosophic-numbers]
tags: [math,neutrosophic-numbers,arithmetic,linear-algebra,linear-functional,differential-operator,vectors,vector-functions]
math: true
mermaid: true
---

In this post I map the arithmetic of neutrosophic numbers to vector functions and then aimlessly wander.

## Neutrosophic Scalar Addition

For neutrosophic numbers $(a+bI)$ and $(c+dI)$, their sum is given by:

$$(a+bI) + (c+dI) = (a+c)+(b+d)I$$

which mapped to vectors gives us the familiar

$$\begin{bmatrix} a \\ b \end{bmatrix} + \begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} a + c \\ b + d \end{bmatrix}$$

which isn't novel. Onto multiplication!

## Neutrosophic Scalar Multiplication

$$(a+bI)(c+dI) = (ac + adI +bcI + bdI) = ac + (ad +bc + bd)I$$

$$\begin{bmatrix} a \\ b \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} ac \\ ad + bc + bd \end{bmatrix}$$

Let's take a look at plugging in the basis vectors on the left-hand-side:

$$\begin{bmatrix} 1 \\ 0 \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} c \\ d \end{bmatrix}$$

$$\begin{bmatrix} 0 \\ 1 \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} 0 \\ c + d \end{bmatrix}$$

This implies that these expressions are related by a matrix multiplication:

$$\begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix} \left( \begin{bmatrix} 1 \\ 0 \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix} \right) = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix}$$

And we also obtain the additive identity:

$$\begin{bmatrix} 1 \\ 1 \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix} + \begin{bmatrix} 0 \\ 1 \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix}c \\ c + 2d \end{bmatrix}$$

These identities can be combined to obtain this further identity:

$$\begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix} \left( \begin{bmatrix} 1 \\ 1 \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix} \right) = 2 \begin{bmatrix} 0 \\ 1 \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix} = 2 \begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix} \left( \begin{bmatrix} 1 \\ 0 \end{bmatrix} \dot \star \begin{bmatrix} c \\ d \end{bmatrix} \right)$$

And now let's go through the basis vectors going on the right-hand-side:

$$\begin{bmatrix} a \\ b \end{bmatrix} \dot \star \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} a \\ b \end{bmatrix}$$

$$\begin{bmatrix} a \\ b \end{bmatrix} \dot \star \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ a + b \end{bmatrix}$$

It should be clear from the symbolic form that *mutatis mutandis* we obtain similar identities as above.

## A Differential Operator

Now let's talk about differential operators. Let

$$\begin{align} a := \frac{\partial}{\partial x} \\ b := \frac{\partial}{\partial y} \\ c:= g(x,y) \\ d := h(x,y) \end{align}$$

and further write

$$\vec \nabla \triangleq \begin{bmatrix} \frac{\partial}{\partial x} \\ \frac{\partial}{\partial y} \end{bmatrix}$$

and 

$$\vec v (x,y) := \begin{bmatrix} g(x,y) \\ h(x,y) \end{bmatrix}.$$

$$\vec \nabla \dot \star \vec v(x,y) = \begin{bmatrix} \frac{\partial}{\partial x} g(x,y) \\ \frac{\partial}{\partial x}h(x,y) + \frac{\partial}{\partial y}g(x,y) + \frac{\partial}{\partial y}h(x,y) \end{bmatrix}$$

Taking

$$\vec \nabla^{\odot k} \triangleq \bigodot_{j=1}^k \vec \nabla$$

there is no reason to stop at the first derivative either:

$$\vec \nabla^{\odot k} \dot \star \vec v(x,y) = \begin{bmatrix} \frac{\partial^k}{\partial x^k} g(x,y) \\ \frac{\partial^k}{\partial x^k}h(x,y) + \frac{\partial^k}{\partial y^k}g(x,y) + \frac{\partial^k}{\partial y^k}h(x,y) \end{bmatrix}$$

I noticed that 

$$\left[ \vec \nabla^{\odot k} h(x,y) = \vec 0 \right] \implies \left[ \vec \nabla^{\odot k} g(x,y) = \vec \nabla^{\odot k} \dot \star \vec v(x,y) \right]$$

and that

$$\left[ \vec \nabla^{\odot k} g(x,y) = \vec 0 \right] \implies \left[ \begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix} \vec \nabla^{\odot k} h(x,y) = \vec \nabla^{\odot k} \dot \star \vec v(x,y) \right].$$

We similarly obtain the bizarre relation:

$$\left[ \vec \nabla^{\odot 2} g(x,y) =\vec 0  \right] \implies \left[ \begin{bmatrix} \alpha \\ 1 \end{bmatrix} \cdot \left( \begin{bmatrix} 0 & 0 \\ 1 & 1 \end{bmatrix} \vec \nabla^{\odot 2} h(x,y) \right) = \vec \nabla^2 h(x,y) \right]$$

for any scalar $\alpha$.

More generally

$$\left[ \vec \nabla^{\odot k} g(x,y) =\vec 0  \right] \implies \left[ \begin{bmatrix} \alpha \\ 1 \end{bmatrix} \cdot \left( \begin{bmatrix} 0 & 0 & \ldots & 0 \\ 1 & 1 & \ldots & 1 \end{bmatrix} \vec \nabla^{\odot k} h(x,y) \right) = \vec 1 \cdot \vec \nabla^{\odot k} h(x,y) \right]$$

for any scalar $\alpha$.
