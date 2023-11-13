---
title: A Permutative Generalization of the Cross Product Is Just the Cross Product
date: 2023-11-12 01:51:15
categories: [mathematics,linear-algebra,cross-product]
tags: [mathematics,linear-algebra,cross-product,python,python-programming,computer-programming,signature,permutation,permutation-signature,real-numbers,hadamard-product,elementwise-product,generalization,determinant,orthogonal-matrices,orthogonality,itertools,sympy,vectors,dimension,rotation-matrices,orthonormal-matrices,dot-product,sine,cosine,wedge-product,multilinear-algebra,curl]
math: true
mermaid: true
---

## Introduction

The goal of this post is to present a minimal description of a generalization of the cross product between two vectors.

The cross product for vectors $\vec a, \vec b \in \mathbb{R}^3$ is given by

$$\vec a \times \vec b = \begin{bmatrix} a_2b_3 - a_3b_2 \\ a_3b_1 - a_1b_3 \\ a_1b_2 - a_2b_1 \end{bmatrix}.$$

## The Generalization
The approach I took to this generalization is to start with the cross product and re-express it in terms of other operations:

$$\begin{align} \vec a \times \vec b =& \begin{bmatrix} a_2b_3 - a_3b_2 \\ a_3b_1 - a_1b_3 \\ a_1b_2 - a_2b_1 \end{bmatrix} \\ =& \begin{bmatrix} a_2b_3\\ a_3b_1 \\ a_1b_2 \end{bmatrix} - \begin{bmatrix} a_3b_2 \\  a_1b_3 \\  a_2b_1 \end{bmatrix} \\ =& \begin{bmatrix} a_2\\ a_3 \\ a_1 \end{bmatrix} \odot \begin{bmatrix} b_3\\ b_1 \\ b_2 \end{bmatrix} - \begin{bmatrix} a_3 \\  a_1 \\  a_2 \end{bmatrix} \odot \begin{bmatrix} b_2 \\  b_3 \\  b_1 \end{bmatrix} \\ =& \begin{bmatrix} 0 & 1 & 0\\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} a_1\\ a_2 \\ a_3 \end{bmatrix} \odot \begin{bmatrix} 0 & 0 & 1\\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} b_1\\ b_2 \\ b_3 \end{bmatrix} - \begin{bmatrix} 0 & 0 & 1\\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} a_1 \\  a_2 \\  a_3 \end{bmatrix} \odot \begin{bmatrix} 0 & 1 & 0\\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} b_1 \\  b_2 \\  b_3 \end{bmatrix} \\ =& \begin{bmatrix} 0 & 1 & 0\\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} a_1\\ a_2 \\ a_3 \end{bmatrix} \odot \begin{bmatrix} 0 & 1 & 0\\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}^T \begin{bmatrix} b_1\\ b_2 \\ b_3 \end{bmatrix} - \begin{bmatrix} 0 & 1 & 0\\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}^T \begin{bmatrix} a_1 \\  a_2 \\  a_3 \end{bmatrix} \odot \begin{bmatrix} 0 & 1 & 0\\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} b_1 \\  b_2 \\  b_3 \end{bmatrix}  \end{align}$$

The $\odot$ operator is the [Hadamard product](https://stats.stackexchange.com/questions/533577/what-is-the-difference-between-the-dot-product-and-the-element-by-element-multip/533578#533578). So the above expansion of the cross product is pretty busy, especially with all the matrices and operators. Notice that we're actually using a single permutation matrix and its transpose. We can readily generalize from this particular $3 \times 3$ permutation matrix to $n \times n$ permutation matrices acting on $\vec a, \vec b \in \mathbb{R}^n$ producing what I'll term the *permutive cross-product*. This cross product, $\times_P : \mathbb{R}^n \times \mathbb{R}^n \mapsto \mathbb{R}^n$ is defined as follows:

$$\vec a \times_P \vec b \triangleq P \vec a \odot P^T\vec b - P^T \vec a \odot P \vec b$$

For a given dimension $n$, there are $n!$ permutations to choose from to construct permutation matrices $P$. While we have achieved a generalization of the cross product, perhaps we would like to find special cases of it that are more natural to the original cross product.

### Signatures
For example, the permutation matrix 

$$\begin{bmatrix} 0 & 1 & 0\\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}$$

used above to obtain the ordinary cross product represents an even permutation. For any permutation matrix $P_{\sigma}$ representing permutation $\sigma$ we know that 

$$\text{sign} \left( \det (P_{\sigma}) \right) = \text{sgn}(\sigma)$$

where $\text{sign}$ on the left-hand-side is the [sign function](https://en.wikipedia.org/wiki/Sign_function) and the $\text{sgn}$ on the right-hand-side (RHS) is the [permutation signature](https://en.wikipedia.org/wiki/Parity_of_a_permutation). It is regrettable that these functions have the same name so I dropped an "i" in the RHS just to make them distinct for our denotation. When $\text{sgn}(\sigma) = 1$ the permutation is even, and when $\text{sgn}(\sigma) = -1$ it is an odd permutation. The permutation matrix for the ordinary cross product is even, and we can rely on the property that 

$$\det (A) = \det (A^T)$$
for any matrix $A$ to know that the transpose is also an even permutation. So if you wanted to, you could restrict yourself to even permutations if you wanted to.

If you wanted to match your generalization even more closely with the original cross product, you could further restrict your permutation to have exactly two inversions. That is the permutation signature satisfies the equality

$$\text{sgn}(\sigma) = (-1)^{N(\sigma)}$$
where $N(\sigma)$ is the number of [inversions](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics))in $\sigma$. The permutation matrix for the ordinary cross product has exactly two inversions. But to me this feels too restrictive since it means we can only flip the order in two components, which is not really a restriction that I care about.

### Orthogonality
A more interesting property, to me, is that the cross product gives a vector which is orthogonal to either of the input vectors.  Using the following Python code I searched over all permutation matrices in 3D that where orthogonal to the original vectors **and** were not the zero vector. (The zero vector is not particularly interesting here and is orthogonal to all vectors in $\mathbb{R}^n$.)

```python
import itertools

import sympy as sp

dim = 3

a = sp.Matrix([sp.Symbol(f'a{i+1}') for i in range(dim)])
b = sp.Matrix([sp.Symbol(f'b{i+1}') for i in range(dim)])
zero_vec = sp.Matrix([[0]]*dim)

for perm in itertools.permutations(range(dim)):
    P = sp.eye(dim)[perm,:]

    cross = (P * a).multiply_elementwise(P.T * b) -\
            (P.T * a).multiply_elementwise(P * b)

    if cross.dot(a).simplify() == 0 and cross.dot(b).simplify() == 0 and cross != zero_vec:
        print(sp.latex(cross))
```

We obtain only two non-trivial vectors:

$$\left[\begin{matrix}a_{2} b_{3} - a_{3} b_{2}\\- a_{1} b_{3} + a_{3} b_{1}\\a_{1} b_{2} - a_{2} b_{1}\end{matrix}\right]$$$$\left[\begin{matrix}- a_{2} b_{3} + a_{3} b_{2}\\a_{1} b_{3} - a_{3} b_{1}\\- a_{1} b_{2} + a_{2} b_{1}\end{matrix}\right]$$
One of these is the original cross product as we introduced it, and the other is just a reflection of it obtained by multiplying by negative one. This just indicates that there are two directions an orthogonal vector could point. So nothing really new is found from our generalization when we search in 3D. Let's go to 4D.

Using the same code as above, except we assign $dim=4$, we find the following vectors are non-trivial examples of the generalization:

$$\left[\begin{matrix}0\\a_{3} b_{4} - a_{4} b_{3}\\- a_{2} b_{4} + a_{4} b_{2}\\a_{2} b_{3} - a_{3} b_{2}\end{matrix}\right]$$

$$\left[\begin{matrix}0\\- a_{3} b_{4} + a_{4} b_{3}\\a_{2} b_{4} - a_{4} b_{2}\\- a_{2} b_{3} + a_{3} b_{2}\end{matrix}\right]
$$

$$\left[\begin{matrix}a_{2} b_{3} - a_{3} b_{2}\\- a_{1} b_{3} + a_{3} b_{1}\\a_{1} b_{2} - a_{2} b_{1}\\0\end{matrix}\right]
$$

$$\left[\begin{matrix}a_{2} b_{4} - a_{4} b_{2}\\- a_{1} b_{4} + a_{4} b_{1}\\0\\a_{1} b_{2} - a_{2} b_{1}\end{matrix}\right]
$$

$$\left[\begin{matrix}- a_{2} b_{3} + a_{3} b_{2}\\a_{1} b_{3} - a_{3} b_{1}\\- a_{1} b_{2} + a_{2} b_{1}\\0\end{matrix}\right]
$$

$$\left[\begin{matrix}a_{3} b_{4} - a_{4} b_{3}\\0\\- a_{1} b_{4} + a_{4} b_{1}\\a_{1} b_{3} - a_{3} b_{1}\end{matrix}\right]
$$

$$\left[\begin{matrix}- a_{2} b_{4} + a_{4} b_{2}\\a_{1} b_{4} - a_{4} b_{1}\\0\\- a_{1} b_{2} + a_{2} b_{1}\end{matrix}\right]
$$

$$\left[\begin{matrix}- a_{3} b_{4} + a_{4} b_{3}\\0\\a_{1} b_{4} - a_{4} b_{1}\\- a_{1} b_{3} + a_{3} b_{1}\end{matrix}\right]
$$

Look at that, we found 8 cross products in 4D! But notice that they are not so different than the two we found in 3D. You'll see that 4 of them are just the ordinary cross product for certain choices of variables, which is embedded in 4D where one of the components is always zero. The remaining four are again just reflections that point in the opposite direction.

So not only did we find a generalization of the cross product for n-dimensional space, but we also learned that the generalization really just provides either trivial examples, examples that are just the ordinary cross product embedded in higher dimensions or their reflections. Personally, I'm satisfied with this generalization because it helped me better understand that there are limited options for what one might mean by a non-trivial vector being orthogonal to two other vectors (or likewise the plane that they span but I did not discuss that).

But let's get perverse by generalizing further (just for fun).

## Getting Perverse

Let's taking a further generalization from what we have seen so far. The operator

$$\vec a \times_P \vec b \triangleq P \vec a \odot P^T\vec b - P^T \vec a \odot P \vec b$$

gives us a generalization of the cross product using a given permutation matrix $P$. Let's see if we find anything new if we generalize to

$$P_1 \vec a \odot  P_2 \vec b - P_3 \vec a \odot P_4 \vec b$$

where $P_1,P_2,P_3,P_4$ are independent choices of permutation matrices. Yup, we're going to try a lot of permutation matrices. Here is some updated code to look through all these possible permutation matrices:

```python
import itertools

import pandas as pd
import sympy as sp
from sympy import latex

dim = 3

a = sp.Matrix([sp.Symbol(f'a{i+1}') for i in range(dim)])
b = sp.Matrix([sp.Symbol(f'b{i+1}') for i in range(dim)])
zero_vec = sp.Matrix([[0]]*dim)

results = []

for perm1 in itertools.permutations(range(dim)):
    for perm2 in itertools.permutations(range(dim)):
        for perm3 in itertools.permutations(range(dim)):
            for perm4 in itertools.permutations(range(dim)):
                P1 = sp.eye(dim)[perm1,:]
                P2 = sp.eye(dim)[perm2,:]
                P3 = sp.eye(dim)[perm3,:]
                P4 = sp.eye(dim)[perm4,:]

                cross = (P1 * a).multiply_elementwise(P2 * b) -\
                        (P3 * a).multiply_elementwise(P4 * b)


                if cross.dot(a).simplify() == 0 and cross.dot(b).simplify() == 0 and cross != zero_vec:
                    results.append(
                        [
                            f'${latex(P1)}$',
                            f'${latex(P2)}$',
                            f'${latex(P3)}$',
                            f'${latex(P4)}$',
                            f'${latex(cross)}$',
                            f'${latex(cross.dot(a).simplify())}$',
                            f'${latex(cross.dot(b).simplify())}$'
                            ]
                        )

result_markdown = pd.DataFrame(
							   results, 
							   columns=['P1', 'P2', 'P3', 'P4', 'cross', 'cross_dot_a', 'cross_dot_b']
							   ).to_markdown()

print(result_markdown)
```

And here are the results.

|    | P1                                                                       | P2                                                                       | P3                                                                       | P4                                                                       | cross                                                                                                                        | cross_dot_a   | cross_dot_b   |
|---:|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|:--------------|:--------------|
|  0 | $\left[\begin{matrix}0 & 1 & 0 \\ 0 & 0 & 1\\1 & 0 & 0\end{matrix}\right]$ | $\left[\begin{matrix}0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0\end{matrix}\right]$ | $\left[\begin{matrix}0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0\end{matrix}\right]$ | $\left[\begin{matrix}0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0\end{matrix}\right]$ | $\left[\begin{matrix}a_{2} b_{3} - a_{3} b_{2} \\ - a_{1} b_{3} + a_{3} b_{1} \\ a_{1} b_{2} - a_{2} b_{1}\end{matrix}\right]$   | $0$           | $0$           |
|  1 | $\left[\begin{matrix}0 & 0 & 1\\ 1 & 0 & 0\\ 0 & 1 & 0\end{matrix}\right]$ | $\left[\begin{matrix}0 & 1 & 0\\ 0 & 0 & 1\\ 1 & 0 & 0\end{matrix}\right]$ | $\left[\begin{matrix}0 & 1 & 0\\ 0 & 0 & 1\\ 1 & 0 & 0\end{matrix}\right]$ | $\left[\begin{matrix}0 & 0 & 1\\ 1 & 0 & 0\\ 0 & 1 & 0\end{matrix}\right]$ | $\left[\begin{matrix}- a_{2} b_{3} + a_{3} b_{2}\\ a_{1} b_{3} - a_{3} b_{1}\\ - a_{1} b_{2} + a_{2} b_{1}\end{matrix}\right]$ | $0$           | $0$           |

That's right. Opening up to a wider pool of permutation matrices did not add any new cross products. If anything actually using only one permutation matrix (and its transpose) substantially reduces the size of the search space. And if we were smart and not lazy then we could further take advantage of the reflections by not enumerating them. There are $(4!)^4=331776$ arrangements of permutations if you have the patience to search through them. 

One could imagine exploring 

$$O_1 \vec a \odot  O_2 \vec b - O_3 \vec a \odot O_4 \vec b$$
where $O_1, O_2, O_3, O_4$ are orthogonal matrices... but that's not going to happen. A more limited case would be to look at [rotation matrices](https://en.wikipedia.org/wiki/Rotation_matrix) which are orthonormal (meaning their transpose is equal to their inverse):

$$\begin{bmatrix} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} \odot \begin{bmatrix} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}^T \begin{bmatrix} b_1 \\ b_2 \end{bmatrix} - \begin{bmatrix} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}^T \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} \odot \begin{bmatrix} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} b_1 \\ b_2 \end{bmatrix}$$
Evaluating this case gives us:

$$\left(a_{1} b_{2} - a_{2} b_{1}\right) \sin\left(2 t \right) \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$
which is not in general orthogonal to the original vectors.

There are 3 rotation matrices in 3D which can be composed together as linear transformations. I'll leave it to the reader to evaluate those cases. One can further consider [$n$-dimensional rotations](https://en.wikipedia.org/wiki/N-sphere#Spherical_volume_and_area_elements) via a Jacobian matrix, but I will also leave that subject alone in this post.

## Concluding Thoughts

While there are [known generalizations](https://en.wikipedia.org/wiki/Cross_product#Generalizations)of the cross product, which I would like to learn more about at some point, I thought I would give it a shot on my own. Actually, the [multilinear approach](https://en.wikipedia.org/wiki/Cross_product#Multilinear_algebra)looks quite comprehensible as a sort of determinant:

$$\bigwedge_{i=0}^{n-1}\vec v_i = \det \left(
\begin{bmatrix}
v_1^1 & \cdots & v_1^n \\ 
\vdots & \ddots & \vdots \\
v_{n-1}^1 & \cdots & v_{n-1}^n \\
\vec e_1 & \cdots & \vec e_n
\end{bmatrix} \right)
$$

But let's not dig further than that in this post.

What I came up with in this post is basically a way of getting any of the possible combinations of cross products embedded in $n \geq 3$ dimensions and their reflections. A cross product will only ever utilize up to three components in these higher dimensional cases. There others are discarded. It was also a reminder to me that the zero vector is orthogonal to all vectors including to itself. Much of what I have explored holds immediately for the [curl](https://en.wikipedia.org/wiki/Curl_(mathematics))as well.
