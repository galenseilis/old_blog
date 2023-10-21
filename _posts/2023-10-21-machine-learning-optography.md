---
title: Machine Learning For Optography?
date: 2023-10-21 00:50:15
categories: [machine-learning,optography]
tags: [machine-learning,optography,deep-learning,convolution,convolutional-neural-networks,optogram,ethics,privacy]
math: true
mermaid: true
---

I watched this [YouTube short](https://youtube.com/shorts/tBFErdYD1wU?si=GudeTQq0rwEmbLVm) by VSauce (Michael Stevens). It describes [optography](https://en.wikipedia.org/wiki/Optography) which is an obscure topic of obtaining images from the retinas of certain animals including humans and rabbits.

I wonder if there is a way to use machine learning to get useful information from optograms. There are some substantial challenges to this. 

The first is likely to be a lack of data. I tried searching online for a dataset of optograms and didn't find anything substantial. 

A second related issue is having additional information paired to optograms, such as classes for classification or continuous variables as regression targets. Maybe an unsupervised approach could produce something interesting for the optograms themselves. 

A third issue is the unusual ethical and privacy concerns that may arise from obtaining and extracting information from optograms.

But if one were take the approach of supervised machine learning, I think a Bayesian convolutional neural network approach would be interesting. Why convolutional neural networks? Well, the translationally equivariant operation of the convolution operator is efficient for images. Why Bayesian? Bayesian inference would allow us to put prior information into the problem that may be difficult to represent using data.

Machine learning for optography sounds pretty cool to me from a sci-fi perspective, but it comes with a bunch of issues both technical and ethical.
