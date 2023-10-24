---
title: Arithmetic of Complex Numbers as Vector Functions
date: 2023-10-23 00:50:15
categories: [math,complex-numbers]
tags: [math,complex-numbers,arithmetic,linear-algebra,linear-functional,differential-operator,vectors,vector-functions]
math: true
mermaid: true
---

The basic arithmetic operations on complex numbers can be represented as vector functions.

## Complex Addition

Suppose we have complex numbers $(a+bi)$ and $(c+bi)$ where $a,b,c,d \in \mathbb{R}$ and $i \triangleq \sqrt{-1}$. The sum of these complex numbers can be written as $(a + bi) + (c + di) = (a+c)+(b+d)i$. This can easily be written as 

$$\begin{bmatrix} a \\ b \end{bmatrix} + \begin{bmatrix} c \\ d \end{bmatrix} = \begin{bmatrix} a + c \\ b + d \end{bmatrix}$$

This is a pretty standard way to express vector addition so I will move on to scalar multiplication of complex numbers.

## Complex Multiplication

The complex scalar multiplication can be written this way:

$$(a + bi) (c + di) = ac - bd +(ad + bc)i$$

And if we invent a notation $\dot \times : \mathbb{R}^2 \times \mathbb{R}^2 \mapsto \mathbb{R}^2$ we can define it element-wise on vectors using the following relation:

$$\begin{bmatrix}a \\ b \end{bmatrix} \dot \times \begin{bmatrix}c \\ d \end{bmatrix} \triangleq \begin{bmatrix}ac-bd \\ ad+bc \end{bmatrix}$$

We can also make some equivocation with this being a function of a matrix provided that we make some choices:

$$\psi: \mathbb{R}^{2 \times 2} \mapsto \mathbb{R}^2$$

Or just as a function of quadruples:

$$\phi : \mathbb{R}^4 \mapsto \mathbb{R}^2$$

Clearly bijections abound. But let's consider what this special type of vector multiplication does to basis vectors.

First let's consider basis vectors on the right-hand-side:

$$\begin{bmatrix}a \\ b \end{bmatrix} \dot \times \begin{bmatrix}1 \\ 0 \end{bmatrix} = \begin{bmatrix}a \\ b \end{bmatrix}$$

$$\begin{bmatrix}a \\ b \end{bmatrix} \dot \times \begin{bmatrix}0 \\ 1 \end{bmatrix} = \begin{bmatrix}-b \\ a \end{bmatrix}$$

It appears that 

$$\begin{bmatrix}a \\ b \end{bmatrix} \dot \times \begin{bmatrix}1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix}a \\ b \end{bmatrix}$$

and 

$$\begin{bmatrix}a \\ b \end{bmatrix} \dot \times \begin{bmatrix}0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix}a \\ b \end{bmatrix}$$

implying

$$\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \left(\begin{bmatrix}a \\ b \end{bmatrix} \dot \times \begin{bmatrix}1 \\ 0 \end{bmatrix} \right) = \begin{bmatrix}a \\ b \end{bmatrix} \dot \times \begin{bmatrix}0 \\ 1 \end{bmatrix}.$$

This means that the two transformed basis vectors are the same up to a rotation of 90 degrees counter-clockwise on the standard Cartesian plane. This should surprise no one who has studied either linear algebra or complex analysis or algebra.


Now let's put the basis vectors on the left-hand-side.

$$\begin{bmatrix}a \\ b \end{bmatrix} \dot \times \begin{bmatrix}c \\ d \end{bmatrix} \triangleq \begin{bmatrix}ac-bd \\ ad+bc \end{bmatrix}$$

$$\begin{bmatrix}1 \\ 0 \end{bmatrix} \dot \times \begin{bmatrix}c \\ d \end{bmatrix} \triangleq \begin{bmatrix}c \\ d \end{bmatrix}$$

$$\begin{bmatrix}0 \\ 1 \end{bmatrix} \dot \times \begin{bmatrix}c \\ d \end{bmatrix} \triangleq \begin{bmatrix}b \\ c \end{bmatrix}$$

We can also write the product as a linear combination:

$$\begin{bmatrix}a \\ b \end{bmatrix} \dot \times \begin{bmatrix}c \\ d \end{bmatrix} = \begin{bmatrix}ac-bd \\ ad+bc \end{bmatrix} = \begin{bmatrix}ac \\ ad \end{bmatrix} + \begin{bmatrix}-bd \\ bc \end{bmatrix} = a\begin{bmatrix}c \\ d \end{bmatrix} + b\begin{bmatrix}-d \\ c \end{bmatrix}$$

## A Differential Operator

This vector function inspires a similar abuse of notation to other operators in calculus.

Making the following assignments:

$$\begin{align} a := \frac{\partial}{\partial x} \\ b := \frac{\partial}{\partial y} \\ c:= g(x,y) \\ d:= h(x,y) \end{align}$$

where 

$$\vec \nabla := \begin{bmatrix} \frac{\partial}{\partial x} \\ \frac{\partial}{\partial y} \end{bmatrix}$$

and 

$$\vec v (x,y) := \begin{bmatrix} g(x,y) \\ h(x,y) \end{bmatrix}.$$

We can see how this constructs a differential operator on vector fields:

$$\vec \nabla \dot \times \vec v (x,y) = \frac{\partial}{\partial x} \begin{bmatrix} g(x,y) \\ h(x,y) \end{bmatrix} + \frac{\partial}{\partial y} \begin{bmatrix} -h(x,y) \\ g(x,y) \end{bmatrix}$$

Taking

$$\vec \nabla^{\odot k} \triangleq \bigodot_{j=1}^k \vec \nabla$$

there is no reason to stop at the first derivative either:

$$\vec \nabla^{\odot k} \dot \times \vec v (x,y) = \frac{\partial^k}{\partial x^k} \begin{bmatrix} g(x,y) \\ h(x,y) \end{bmatrix} + \frac{\partial^k}{\partial y^k} \begin{bmatrix} -h(x,y) \\ g(x,y) \end{bmatrix}.$$

It should also be apparent that 

$$\vec \nabla^{\odot k} \dot \times \left[ \alpha \vec v (x,y) \right] = \alpha \left[ \vec \nabla^{\odot k} \dot \times \vec v (x,y) \right]$$

due to the linearity of derivatives.

Likewise the linearity of derivatives implies the distribution:

$$\vec \nabla^{\odot k} \dot \times  \left[ \vec v (x,y) + \vec u (x,y) \right] = \vec \nabla^{\odot k} \dot \times  \vec v (x,y) + \vec \nabla^{\odot k} \dot \times  \vec u (x,y).$$

We can immediately generalize to linear combinations of functions:

$$\vec \nabla^{\odot k} \dot \times  \left[ \sum_{i=1}^n \alpha_i \vec v_i (x,y) \right] = \sum_{i=1}^n \alpha_i \vec \nabla^{\odot k} \dot \times  \vec v (x,y).$$

And of course we can consider the "infinite dimensional" (i.e. integral) case:

$$\vec \nabla^{\odot k} \dot \times  \left[ \underbrace{\int_{\Omega} \ldots \int_{\Omega}}_{k} \vec v (x,y)\   d(¯\_(ツ)_/¯) \right]$$

So yeah, I'm not sure the integral case is well-defined until we **choose** what we are integrated with respect to, denoted d(¯\_(ツ)_/¯).
