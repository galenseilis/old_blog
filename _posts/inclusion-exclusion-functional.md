---
title: The Inclusion-Exclusion Functional
date: 2023-03-03 20:38:46 -0800
categories: [math,funtions,functionals]
tags: [math,funtions,functionals,inclusion-exlusion-principle,inclusion-exclusion-functional]
math: true
mermaid: true
---

The [inclusion-excusion principle](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle) is theoerm pertaining to measures on sets. For a measure $\mu$ we can consider the meaure of the union of a collection of sets $\{ A_1, \ldots, A_n \}$ to be the following function of the intersections:


$$\mu \left( \bigcup_{i=1}^n A_i \right) = \sum_{i=1}^n \mu \left( A_i \right) - \sum_{1 \leq i < j \leq n} \mu \left(A_i \cap A_j \right) + \sum_{1 \leq i < j < k \leq n} \mu \left( A_i \cap A_j \cap A_k \right) - \cdots + (-1)^{n+1} \mu \left( A_1 \cap \ldots \cap A_n \right)$$

Now I stress that the above is a **theorem**. The left is provably equal to the right due to measures being disjoint additive. What I want to share is a generalization of the right-hand-side of this equation which is achieved by wholesale replacing certain operations with others. We replace the measure $\mu$ with a generic muliary function $f$ and the sets with arbitrary operands $x_1, \ldots, x_n$. And instead of adding/subtracting, we replace the addition symbols with a binary operator $\oplus$ with an inverse $\ominus$.

$$\phi_f \left( x_1 \right) = f(x_1)$$

$$\phi_f \left( x_1, x_2 \right) = \left[ f(x_1) \oplus f(x_2) \right] \ominus f(x_1, x_2)$$

$$\phi_f \left( x_1, x_2, x_3 \right) = \left( \left[ \left\{ \left( \left[ f(x_1) \oplus f(x_2) \right] \oplus f(x_3) \right) \ominus f(x_1,x_2) \right\} \ominus f(x_1,x_3) \right] \ominus f(x_2, x_3) \right) \oplus f(x_1, x_2, x_3)$$

The general form $\phi_f \left( x_1, \ldots , x_n \right)$ is not associative in general, nor does it necessarily hold that 

$$\phi_f \left( x_1, \ldots , x_n \right) = \phi_f \left( x_{\sigma (1)}, \ldots , x_{\sigma (n)} \right)$$

for all permutations $\sigma$.

# Examples

## Addition

$$\phi_f \left( x_1 \right) = f(x_1)$$

$$\phi_f \left( x_1, x_2 \right) =  f(x_1) + f(x_2) - f(x_1, x_2)$$

$$\phi_f \left( x_1, x_2, x_3 \right) =  f(x_1) + f(x_2) + f(x_3)  - f(x_1,x_2)  - f(x_1,x_3)  - f(x_2, x_3)  + f(x_1, x_2, x_3)$$

## Subtraction

$$\phi_f \left( x_1 \right) = f(x_1)$$

$$\phi_f \left( x_1, x_2 \right) =  f(x_1) - f(x_2) + f(x_1, x_2)$$

$$\phi_f \left( x_1, x_2, x_3 \right) = f(x_1) - f(x_2)  - f(x_3)  + f(x_1,x_2) + f(x_1,x_3) + f(x_2, x_3) - f(x_1, x_2, x_3)$$

## Multiplication

$$\phi_f \left( x_1 \right) = f(x_1)$$

$$\phi_f \left( x_1, x_2 \right) = \frac{f(x_1) f(x_2)}{f(x_1, x_2)}$$

$$\phi_f \left( x_1, x_2, x_3 \right) = \frac{f(x_1) f(x_2) f(x_3) f(x_1, x_2, x_3)}{f(x_1,x_2)  f(x_1,x_3) f(x_2, x_3)}$$

## Division

$$\phi_f \left( x_1 \right) = f(x_1)$$

$$\phi_f \left( x_1, x_2 \right) =  \frac{f(x_1) f(x_1, x_2) }{f(x_2)}$$

$$\phi_f \left( x_1, x_2, x_3 \right) = \frac{f(x_1)f(x_1,x_2)  f(x_1,x_3)  f(x_2, x_3)}{f(x_2) f(x_3) f(x_1, x_2, x_3)}$$

## Exponentiation

With exponentiation $a^b$ we have a choice to make in how we map it to $a \oplus b$. One assignment is $a \oplus b := a^b$, and the other is $a \oplus b := b^a$. Let us start with $a \oplus b := a^b$ and $a \ominus b := \log_a b$:

$$\phi_f \left( x_1 \right) = f(x_1)$$

$$\phi_f \left( x_1, x_2 \right) =  \log_{f(x_1)^{f(x_2)}} \left( f(x_1, x_2) \right)$$

$$\phi_f \left( x_1, x_2, x_3 \right) = \left[ \log_{\log_{\log_{\left[ f(x_1)^{f(x_2)} \right]^{f(x_3)}} \left( f(x_1,x_2) \right)} \left(f(x_1,x_3)\right)} \left( f(x_2, x_3) \right) \right]^{f(x_1, x_2, x_3)}$$

## Logarithm

