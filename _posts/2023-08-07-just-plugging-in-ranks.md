---
title: Just Plugging In Ranks
date: 2023-08-07 00:52:00 -0800
categories: [mathematics,statistics,rank-based-statistics]
tags: [math,mathematics,statistics,rank-based-statistics,ranks,functions,transformations]
math: true
mermaid: true
---

This post is part of continued response to the following YouTube video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/qee6b7vl2O0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This post picks up with responding to the following quote.

> Quotation (Dustin Fife)
>
> You lose the interpretability of the estimates. So a slope doesn't mean what it meant before, a Cohen's D doesn't mean what it meant before, and those sorts of things.

It is usually a bad idea to just expect plugging in variables (transformed or otherwise) into a function without doing some sort of checking. Fortunately, we can sometimes check! Let's try plugging in ranks into some basic functions and statistics to see what we learn. I'll be assuming dense ranks with no ties between elements.

Let's start simple with summation. If we have $\operatorname{rank}(X) = \\{1, \ldots, m \\}$, we can consider their sum:

$$\sum_{i=1}^m \operatorname{rank}(x_i) = \sum_{i=1}^m i = \frac{m(m+1)}{2}.$$

Likewise, the mean of the ranks gives

$$\frac{1}{m} \sum_{i=1}^m \operatorname{rank}(x_i) = \frac{1}{m} \frac{m(m+1)}{2} = \frac{m+1}{2}.$$

which at a glance might seem meaningless. Actually, it is the median in disguise. Consider that the rank function is a table of values, and since we are assuming there are no ties we have a bijection. Thus the inverse element of the ranking,  $\text{rank}^{-1}(x_i)$, uniquely exists. When the sample size is odd, then the inverse of the mean rank is the sample median: 

$$\text{rank}^{-1} \left( \frac{m+1}{2} \right) = \text{median}(x_1, \ldots, x_m).$$

When $m$ is even then the inverse will not exist. Does that entail that it says nothing about the data? Not quite. We can consider the interval of the floor and ceiling round of the mean rank which will exist in the domain of the inverse rank, and the inverses of these bounds provide the smallest interval using elements of the sample which cover the sample median. That is

$$\left[ \text{rank}^{-1} \left( \Bigl\lfloor \frac{m+1}{2} \Bigr\rfloor \right),  \text{rank}^{-1} \left( \Bigl\lceil \frac{m+1}{2} \Bigr\rceil \right)\right] = \left[x_{\frac{m}{2}}, x_{\frac{m}{2}+1} \right]$$

where
$$\text{median}(x_1, \ldots, x_m) \in \left[x_{\frac{m}{2}}, x_{\frac{m}{2}+1} \right]$$

and there does not exist an $x_i > x_{\frac{m}{2}}$ in the sample such that $x_i \leq \text{median}(x_1, \ldots, x_m)$, and there likewise does not exist $x_i < x_{\frac{m}{2}+1}$ such that $x_i \geq \text{median}(x_1, \ldots, x_m)$. We can also note that the centerpoint of this preimage interval is the sample median: 

$$\frac{x_{\frac{m}{2}} + x_{\frac{m}{2}+1}}{2} = \text{median}(x_1, \ldots, x_m).$$	

Not as precise as when $m$ is odd, but I think it counts for something.


And now here is the product of the ranks


$$\prod_{i=1}^m \operatorname{rank}(x_i) = \prod_{i=1}^m i = m!$$

which gives the number of permutations on the $m$ elements. It is the only example I am currently aware of in which applying a permutation invariant operation on the ranks still tells us something about the order properties of the data. We can further consider the geometric mean on ranks to be $\sqrt[m]{m!}$ as a counterpart to the arithmetic mean on ranks.

And we can consider the sample variance:

$$\begin{align*}
\hat \sigma_{\text{rank}(x)}^2 &= \frac{\sum_{i=1}\left( \text{rank}(x_i) - \frac{1}{m}\sum_{i=1} \text{rank}(x_i) \right)^2}{m}\\
&=  \frac{(m+1)(2m+1)}{6} - \frac{(m+1)^2}{4}\
\end{align*}$$


In each of these cases we were able to show these relatively simple functions of ranks are uniquely determined by the sample size. It is clear enough that changing the sample size will also change the value of these functions. This is because both summation and multiplication are permutation invariant!

> There are formal procedures using representations of permutation groups, but you can also convince yourself that this is true by considering that both addition and scalar multiplication are associative and commutative. These two operation properties together allow you to rearrange things into any order you like and still get the same result.
{:.prompt-info}

They lose information about the order of the operands which defeats the purpose of using the rank transform: to study order.

Let's consider the sample covariance, which actually *does* depend on the order of elements in the data:

$$\begin{align*}
\hat \sigma_{\text{rank}(x) \text{rank}(y)} &= \frac{1}{m} \sum_i^m \text{rank}(x_i) \text{rank}(y_i) - \left( \frac{1}{m} \sum_i^m \text{rank}(x_i) \right) \left( \frac{1}{m} \sum_i^m \text{rank}(y_i) \right)\\
&= \frac{1}{m} \sum_i^m \text{rank}(x_i) \text{rank}(y_i) - \left( \frac{1}{m} \sum_i^m i \right)^2\\
&= \frac{1}{m} \sum_i^m \text{rank}(x_i) \text{rank}(y_i) - \left( \frac{1}{m} \frac{m(m+1)}{2} \right)^2\\
&= \frac{1}{m} \sum_i^m \text{rank}(x_i) \text{rank}(y_i) - \left( \frac{m+1}{2} \right)^2\\
&= \frac{1}{m} \sum_i^m \text{rank}(x_i) \text{rank}(y_i) - \frac{(m+1)^2}{4}\\
\end{align*}$$

This sample covariance should be bounded from below and from above. The minimum value is obtained from taking either of the paired ranks to be in reverse order to the other:

$$\begin{align*}
\hat \sigma_{\text{rank}(x) \text{rank}(y)} & \geq \frac{1}{m} \sum_i^m \left[ i (m-i+1) \right] - \frac{(m+1)^2}{4} \\
& \geq \frac{1}{m} \sum_i^m \left[ (m+1)i - i^2 \right] - \frac{(m+1)^2}{4} \\
& \geq \frac{m+1}{m} \sum_i^m i - \frac{1}{m} \sum_i^mi^2 - \frac{(m+1)^2}{4} \\
& \geq \frac{m+1}{m} \frac{m(m+1)}{2} - \frac{1}{m} \frac{m (m+1) (2m+1)}{6} - \frac{(m+1)^2}{4} \\
& \geq  \frac{(m+1)^2}{2} - \frac{(m+1) (2m+1)}{6} - \frac{(m+1)^2}{4} \\
& \geq  - \frac{(m+1) (2m+1)}{6} + \frac{(m+1)^2}{4} \\
& \geq  - \hat \sigma_{\text{rank}(x)}^2 = - \hat \sigma_{\text{rank}(y)}^2\\
\end{align*}$$

We can similarly find the upper bound of the sample covariance on ranks by aligning the pairs of ranks.

$$\begin{align*}
\hat \sigma_{\text{rank}(x) \text{rank}(y)} & \leq \frac{1}{m} \sum_i^m i^2 - \frac{(m+1)^2}{4} \\
& \leq \frac{1}{m} \frac{m(m+1)(2m+1)}{6} - \frac{(m+1)^2}{4} \\
& \leq \frac{(m+1)(2m+1)}{6} - \frac{(m+1)^2}{4} \\
& \leq \hat \sigma_{\text{rank}(x)}^2 = \hat \sigma_{\text{rank}(y)}^2 \\
\end{align*}$$

This has an immediate consequence for the simple ordinary least squares estimator of the slope, which is that the slope of the ranks of $Y$ with respect to the ranks of $X$ is the same as that of the ranks of $X$ with respect to the ranks of $Y$.

$$\begin{align*}
\hat \beta &= \frac{\hat \sigma_{\text{rank}(x) \text{rank}(y)}}{\hat \sigma_{\text{rank}(x)}^2} \\
&= \frac{\hat \sigma_{\text{rank}(x) \text{rank}(y)}}{\hat \sigma_{\text{rank}(y)}^2} \\
\end{align*}$$

These results also show us that $-1 \leq \hat \beta \leq 1$, where -1 is acheived when the data is antimonotone and 1 is acheived when the data is monotone. That is to say, the slope of the ranks indicates whether the variables go up or down in either direction. Perhaps less obvious is that this is actually the same as the Spearman rank correlation:

$$\hat \beta = \hat r_{\rho}$$

Keep in mind that these tidy equalities do not hold when we have tied ranks, in which case the results will depend on how ties are handled and which paired values are tied. While the results become less tidy in other cases, similar conclusions are reached in terms of what the slope and correlation on the ranks quantify: agreement in order. Because equality between the variances of the ranks does not generally hold, nor the equality between slope and Spearman's rank correlation, I advise using Spearman's rank correlation which is a function of both variances and the covariance for these pairwise order comparisons.


Now, as a final example, let's consider Cohen's $d$ since he mentioned it. I see there are a couple of slightly different *Cohen's d* calculations. Let us take it to be

$$d = \frac{\bar x_1 - \bar{x_2}}{s}$$

where $\bar x_1$ and $\bar x_2$ are the sample means, $s$ is the *pooled standard deviation* given by

$$s = \sqrt{\frac{(m_1 - 1) s_1^2 + (m_2 - 1)s_2^2}{m_1 + m_2 - 2}}$$

and $s_1^2$ and $s_2^2$ are the Bessel-corrected sample variances. Based on what we've discussed, can you guess whether it is determined solely by sample size when we compute it on the ranks? Let's find out, starting with computing one of the Bessel-corrected sample variances.

$$\begin{align*}
s_1^2 &= \frac{1}{m_1 - 1} \sum_{i=1}^{m_1} \left( \text{rank}(x_i) - \frac{1}{m_1}\sum_{i=1}^{m_1} \text{rank}(x_i) \right)^2\\
&= \frac{1}{m_1 - 1} \sum_{i=1}^{m_1} \left( i - \frac{1}{m_1}\sum_{i=1}^{m_1} i \right)^2 \\
&= \frac{1}{m_1 - 1} \sum_{i=1}^{m_1} \left( i - \frac{1}{m_1}\frac{m_1 (m_1+1)}{2} \right)^2 \\
&= \frac{1}{m_1 - 1} \sum_{i=1}^{m_1} \left( i - \frac{ (m_1+1)}{2} \right)^2 \\
&= \frac{1}{m_1 - 1} \sum_{i=1}^{m_1} \left( i^2 - 2i\frac{(m_1+1)}{2} + \frac{(m_1+1)^2}{4} \right) \\
&= \frac{1}{m_1 - 1}\left( \sum_{i=1}^{m_1}  i^2 - (m_1+1)\sum_{i=1}^{m_1} i + \sum_{i=1}^{m_1}\frac{(m_1+1)^2}{4} \right) \\
&= \frac{1}{m_1 - 1}\left( \frac{m_1 (m_1 + 1) (2 m_1 + 2) }{6} - \frac{m_1 (m_1+1)^2 }{2} + \frac{m_1(m_1+1)^2}{4} \right) \\
&= \frac{1}{m_1 - 1}\left( \frac{m_1 (m_1 + 1) (2 m_1 + 2) }{6} - \frac{m_1 (m_1+1)^2 }{4} \right) \\
\end{align*}$$

Now we'll put together the pooled variance...

$$\begin{align*}
s &= \sqrt{\frac{(m_1 - 1) \frac{1}{m_1 - 1}\left( \frac{m_1 (m_1 + 1) (2 m_1 + 2) }{6} - \frac{m_1 (m_1+1)^2 }{4} \right) + (m_2 - 1)\frac{1}{m_2 - 1}\left( \frac{m_2 (m_2 + 1) (2 m_2 + 2) }{6} - \frac{m_2 (m_2+1)^2 }{4} \right)}{m_1 + m_2 - 2}} \\
&= \sqrt{\frac{ \frac{m_1 (m_1 + 1) (2 m_1 + 2) }{6} - \frac{m_1 (m_1+1)^2 }{4} +  \frac{m_2 (m_2 + 1) (2 m_2 + 2) }{6} - \frac{m_2 (m_2+1)^2 }{4} }{m_1 + m_2 - 2}} \\
&= \frac{1}{\sqrt{2}}\sqrt{\frac{ \frac{m_1 (m_1 + 1) (2 m_1 + 2) }{3} - \frac{m_1 (m_1+1)^2 }{2} +  \frac{m_2 (m_2 + 1) (2 m_2 + 2) }{3} - \frac{m_2 (m_2+1)^2 }{2} }{m_1 + m_2 - 2}} \\
\end{align*}$$

And in case that wasn't verbose enough, let's put together Cohen's d on the ranks:

$$\begin{align*}
d &= \frac{\frac{m_1 + 1}{2} - \frac{m_2 + 1}{2}}{\frac{1}{\sqrt{2}}\sqrt{\frac{ \frac{m_1 (m_1 + 1) (2 m_1 + 2) }{3} - \frac{m_1 (m_1+1)^2 }{2} +  \frac{m_2 (m_2 + 1) (2 m_2 + 2) }{3} - \frac{m_2 (m_2+1)^2 }{2} }{m_1 + m_2 - 2}}} \\
&= \frac{\sqrt{2}}{2} \frac{m_1 - m_2}{\sqrt{\frac{ \frac{m_1 (m_1 + 1) (2 m_1 + 2) }{3} - \frac{m_1 (m_1+1)^2 }{2} +  \frac{m_2 (m_2 + 1) (2 m_2 + 2) }{3} - \frac{m_2 (m_2+1)^2 }{2} }{m_1 + m_2 - 2}}} \\
\end{align*}$$

We can quickly surmise a couple of facts about Cohen's d on ranks. First, and most generally, it is entirely determined by the two respective sample sizes $m_1$ and $m_2$. Using permutation invariant operations on the ranks (e.g. summation), we have thrown away any useful information about the ordering of the data. A secondary observation is that it obtains a score of zero when the sample sizes are equal. Indeed, all this has accomplished is a rather overcomplicated way of computing whether two (exactly known) sample sizes were equal.

In summary, computing statistics on the ranks of the data seems to be informative if (1) you usually compute only functions that depends on the order properties of the data and (2) you are interested in the order properties of the data. Further, let me offer a flippant retort to the quote at the start of this section: of course these statistics don't mean the same thing in composition with a rank transform! If they did, then there would be no point in composing them with a rank transform! But Dustin and I agree that you *can* lose interpretability of the estimates. I just wouldn't agree that we *always* lose interpretability of the resulting estimates when you compose various functions with a rank transform. When we apply a transform that preserves little more than order, and then apply further transformations that are order-invariant, there isn't much left to consider afterwards. But beyond that rank-based statistics can tell us about the order properties of the data.
