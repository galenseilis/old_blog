---
title: Curling Up to A Function and Its Lags
date: 2023-03-19 16:56:00 -0800
categories: [math,calculus]
tags: [math,calculus]
math: true
mermaid: true
---

Suppose we have a $C^1$-smooth function $f : \mathbb{R} \mapsto \mathbb{R}$. We can consider $f(t+ \tau)$ and $f(t+\theta)$ to be translations, or lags, or the function. From these three functions we can define

$$\vec u (t, \tau, \theta) \triangleq \begin{bmatrix}
    f(t) \\
    f(t+\tau) \\
    f(t + \theta) 
\end{bmatrix}$$

to be a vector function. This vector field over $\mathbb{R}^3$ describes the function and pairs of lags in "time" $t$.

Defining $\vec v = [t, \tau, \theta]^T$ we can compute the curl

$$\nabla_{\vec v} \times \vec u (t, \tau, \theta) = \begin{bmatrix}
    \frac{\partial f(t + \theta)}{\partial \tau} - \frac{\partial f(t + \tau)}{\partial \theta} \\
    \frac{\partial f(t)}{\partial \theta} - \frac{\partial f(t + \theta)}{\partial t} \\
    \frac{\partial f(t + \tau)}{\partial t} - \frac{\partial f(t)}{\partial \tau} \\
\end{bmatrix}$$

which simplifies to 

$$\nabla_{\vec v} \times \vec u (t, \tau, \theta) = \begin{bmatrix}
    0 \\
   - \frac{\partial f(t + \theta)}{\partial t} \\
    \frac{\partial f(t + \tau)}{\partial t} \\
\end{bmatrix}.$$

A similar approach is to constructa curl-like operator that is only with respect to time. First we can define a vector of the partial derivatives with respect to time (repeated):

$$\frac{\partial}{\partial \vec t} \triangleq = \left[ \frac{\partial}{\partial t} \cdots  \frac{\partial}{\partial t} \right]^T.$$

Now we can use the cross-product with this operator in a curl-like way:

$$\frac{\partial}{\partial \vec t} \times \vec u (t, \tau, \theta) \begin{bmatrix}
    \frac{\partial f(t + \theta)}{\partial t} - \frac{\partial f(t + \tau)}{\partial t} \\
    \frac{\partial f(t)}{\partial t} - \frac{\partial f(t + \theta)}{\partial t} \\
    \frac{\partial f(t + \tau)}{\partial t} - \frac{\partial f(t)}{\partial t} \\
\end{bmatrix}$$
