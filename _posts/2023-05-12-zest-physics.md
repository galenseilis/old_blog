---
title: Adding A Little Zest To Physics
date: 2023-05-12 7:53:00 -0800
categories: [physics,zest-physics]
tags: [zest-physics]
math: true
mermaid: true
---

This early stages of the post began when I [answered a question](https://stats.stackexchange.com/questions/533577/what-is-the-difference-between-the-dot-product-and-the-element-by-element-multip/533578#533578) on stats.se aobut the difference between the dot product and the element-wise multiplication. While I had certaintly used and thought about these notions before that post, I had not paid such close attention to how they are different.

The kinetic energy of a classic object is given by 

$$E_K \triangleq \frac{m}{2} \vert| \frac{\partial s(t)}{\partial t} \vert|_2^2$$

where $m$ is the object's mass and $s(t)$ is the position vector as a function of time $t$.

There is a related concept to kinetic energy I will introduce in this post: zest. The notion of zest came about for me when I was considering the relation

$$\vec x \cdot \vec y = \left( \vec x \odot \vec y \right) \cdot \vec 1$$

where $\vec x, \vec y \in \mathbb{R}^n$, $\cdot$ is the dot product, and $\odot$ is the Hadamard product. 

In the kinetic energy the 

$$\vert| \frac{\partial s(t)}{\partial t} \vert|_2^2$$

factor can be equivalently written 

$$\frac{\partial s(t)}{\partial t} \cdot \frac{\partial s(t)}{\partial t}.$$ 

By the correspondence between dot products and projected Hadamard products we can also write this as $$\left( \frac{\partial s(t)}{\partial t} \odot \frac{\partial s(t)}{\partial t} \right) \cdot \vec 1.$$

# A Correspondence

# Zest

The next step to defining the zest of this object is to simply drop the dot product with $\vec 1$, defining the zest to be

$$\vec z \triangleq \frac{m}{2} \left( \frac{\partial s(t)}{\partial t} \odot \frac{\partial s(t)}{\partial t} \right)$$

This components of the zest are bounded due to the Cauchy Scharwz in equality.

# Apparent Energy

$$\left(O A \vec z \right) \vec 1$$

# Cross Zest


This components of the cross zest are bounded due to the Cauchy Scharwz in equality.
# Multizest

$$\vec z \triangleq \frac{1}{2^n} \sqrt{\prod_{i=1}^n m_i} \bigodot_{i=1}^n \frac{\partial \vec s_i(t)}{\partial t}$$

The components of the multizest vector are bounded due to the generalized Holder inequality for sums.

# Relation tO Array Functions

Notice that 
