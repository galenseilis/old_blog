The distinction of "parametric" vs "nonparametric" statistics is worth making as it allows us to categorize braod areas of techniques. It isn't without problems, however. Soe of the difficulties with the term "nonparametric statistics" are alluded to by Andrew Wasserman in his textbook *All of Nonparametric Statistics*:

> The basic idea of nonparemetric inference is to use data to infer an unknown quantity while making as few assumptions as possible. Usually, this means using statistical models that are infinite-dimensional. Indeed, a better name for nonparametric inference might be infinite-dimensional inference. But it is difficult to give a precise definition of nonparametric inference, and if I did venture to give one, no doubt I would be barraged with dissenting opinions.

This notion of infinite-dimensional inference I suspect pertains to the usage of infinite function spaces that occur in some non-parametric procedures. Chapter 9 of All of Nonparametric Statistcs by Wasserman cover Wavelets which are a nice example of functional analysis. Wavelets can be used to form bases of function spaces in a way analogous to how Fourier series can be used to construct Fourier bases. It turns out that lots of functions can be expressed as linear combinations of such mathematical functions. Both of these approaches to representing function spaces rely on inner products making these spaces Hilbert spaces which are allowed to be infinite dimensional. The word *dimension* can be a bit of an overloaded term. Here I meant "dimension" in the same sense as vector spaces.

Let us compare this to the description on Wikipedia (accessed 2022-12-18):

> The term ”nonparametric statistics” has been imprecisely defined in the following two ways, among others:
> 1.
> The first meaning of nonparametric covers techniques that do not rely on data belonging to any particular parametric family of probability
> distributions.
> These include, among others:
> - distribution-free methods, which do not rely on assumptions that the data are drawn from a given parametric family of probability
distributions. As such it is the opposite of parametric statistics.
> - nonparametric statistics (a statistic is defined to be a function on a sample; no dependency on a parameter).
> Order statistics, which are based on the ranks of observations, is one example of such statistics.
> The following discussion is taken from Kendall’s Advanced Theory of Statistics.
> Statistical hypotheses concern the behavior of observable random variables.... For example, the hypothesis (a) that a normal distribution
> has a specified mean and variance is statistical; so is the hypothesis (b) that it has a given mean but unspecified variance; so is the
> hypothesis (c) that a distribution is of normal form with both mean and variance unspecified; finally, so is the hypothesis (d) that two
> unspecified continuous distributions are identical.
> It will have been noticed that in the examples (a) and (b) the distribution underlying the observations was taken to be of a certain form
> (the normal) and the hypothesis was concerned entirely with the value of one or both of its parameters. Such a hypothesis, for obvious
> reasons, is called parametric.
> Hypothesis (c) was of a different nature, as no parameter values are specified in the statement of the hypothesis; we might reasonably
> call such a hypothesis non-parametric. Hypothesis (d) is also non-parametric but, in addition, it does not even specify the underlying
> form of the distribution and may now be reasonably termed distribution-free. Notwithstanding these distinctions, the statistical literature
> now commonly applies the label ”non-parametric” to test procedures that we have just termed ”distribution-free”, thereby losing a useful
> classification.
> 2. The second meaning of non-parametric covers techniques that do not assume that the structure of a model is fixed. Typically, the model
> grows in size to accommodate the complexity of the data. In these techniques, individual variables are typically assumed to belong to
> parametric distributions, and assumptions about the types of connections among variables are also made. These techniques include, among
> others:
> - non-parametric regression, which is modeling whereby the structure of the relationship between variables is treated non-
> parametrically, but where nevertheless there may be parametric assumptions about the distribution of model residuals.
> - non-parametric hierarchical Bayesian models, such as models based on the Dirichlet process, which allow the number of latent
> variables to grow as necessary to fit the data, but where individual variables still follow parametric distributions and even the
> process controlling the rate of growth of latent variables follows a parametric distribution.

What I find salient about this wikipedia entry and Wasserman’s quote is that non-parametric elludes a
formal, unique, and rigorous definition. This makes it difficult to reason precisely about, but it still helps us
roughly classify methods.

Ever since I first heard of non-parametric statistics it always seemed like a misnomer to me that non-
parametric does not mean something lacking parameters. A nice example of this is kernel density estimation
(KDE) with a Gaussian kernel. Although each kernel has a mean and standard deviation, Gaussian KDE is
often seen as a non-parametric procedure because it can really take on such a wide variety of shapes that
resemble other distributions that it seems like we have not assumed much. Perhaps if one fixed the number
of kernels and the bandwidth that they could argue they have a parametric procedure, but in practice most
of us place KDE in the nonparametric side of the distinction.

What KDE and many other non-parametric methods have in common is not that you cannot assume
a particular family of distributions if you insist, but rather that some model structures and estimators are
so flexible that they can fit practically anything. (In some cases we have theorems that show extremely general capabilities of approximation. The field of mathematics called
approximation theory explores how functions can look like each other. Often these proofs involve (ε-δ)-proofs under a choice of
metric or specialized bounds such as Pinsker’s inequality.) With this flexibility they also readily overfit, which can
be combatted with a variety of regularization techniques, and we can assess how badly such models have
overfit using cross-validation. It is with such methods that you may hear phrases like, “the method is non-
parametric because we have not assumed a fixed model structure ahead of time”. And it is in this sense that
random forests or LOESS/LOWESS regression are non-parametric.

Rank-based non-parametric statistcs are more like the other sense of non-parametric mentioned in the
wikipedia article. It isn’t that statistics calculated on ranks are themselves really flexible in the same sense
as discussed above. Rather, they often ignore many of the properties of the data.
