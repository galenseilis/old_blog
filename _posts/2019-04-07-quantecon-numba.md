---
title: QuantEcon 2 Numba
date:   2019-04-09 12:00:50 -0700
categories: [python,numba]
tags: [python,numpy,timeit,precompiling,just-in-time-compiling,jit,vectorizing]
math: true
mermaid: true
---

# Introduction

[Numba](http://numba.pydata.org/) is a Python library that provides an open source just-in-time compiler that allows a coder to mark selected parts of their code to be compiled for faster execution. As someone interested in computation at any scale, from calculating 13 * 19 (mental arithmetic is not my forte) to analyzing the behaviour of tens of thousands of genes or hundreds of thousands of IP addresses. I am not one to squeeze every inch of performance out of something small that was only meant to run once as a proof of concept, but it can be worth speeding up tasks that are either huge or will be repeated.

Let's get into how to use Numba -- hang on! Why not just use compiled languages like C, C++ or FORTRAN? Well, herein lies one of meta-problems of development that requires some optimization. Coding in Python is useful for quickly coding up proofs of concept, but properties like its dynamic typing slow it down compared to memory-managed code in C. Coding in C will give a faster execution for the same code, but will often require more time and degugging to get ready for deployment. Using Python with Numba is an attempt to get the best of both worlds, and in practice is not much slower than software compiled from well-written low-level languages.

# Precompiling

The first way we can use Numba to speed up our code is by compiling a function so that future executions can use the compiled version, removing the need to compile at runtime. Let's take a function that gives us the first *n* Fibonnacci numbers, and see how it performs.

```python
import numpy as np
from timeit import timeit

def fib(n):
    '''
    Adjusted from:
    https://lectures.quantecon.org/py/numba.html
    https://en.wikipedia.org/wiki/Fibonacci_number
    https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    '''

    if n == 1:
        return np.ones(1)
    elif n > 1:
        x = np.empty(n)
        x[0] = 1
        x[1] = 1
        for i in range(2,n):
            x[i] =  x[i-1] + x[i-2]
        return x
    else:
        print('WARNING: Check validity of input.')

print(timeit('fib(10)', globals={'fib':fib}))
```
Running the above code on my laptop gives around 4.7 seconds to run the function 1000000 times according to timeit, which is reasonable for small *n* but let's see if we can speed this up with the Numba's jit.

```python
from numba jit
import numpy as np
from timeit import timeit

def fib(n):
    '''
    ARGUMENTS:
    n: Max index to calculate Fibonacci numbers up to (int)
    RETURNS
    x: Array of Fibonnacci numbers (numpy.ndarray)
    
    NOTES:
    Adjusted from:
    https://lectures.quantecon.org/py/numba.html
    https://en.wikipedia.org/wiki/Fibonacci_number
    https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    '''

    if n == 1:
        return np.ones(1)
    elif n > 1:
        x = np.empty(n)
        x[0] = 1
        x[1] = 1
        for i in range(2,n):
            x[i] =  x[i-1] + x[i-2]
        return x
    else:
        print('WARNING: Check validity of input.')

fib = jit(fib)

print(timeit('fib(10)', globals={'fib':fib}))
```
Running the above code with jit brought the execution time down to about 0.71 second, which is about 6.6 times faster than the original function.

# Vectorizing

Another approach to speeding up code is vectorizing, where multiple operations are applied to each entry directly instead of producing multiple intermediate arrays as operations are applied. Originally I had wanted to use our `fib` function, but [I quickly learned](https://stackoverflow.com/questions/55564403/numba-indexing-error-typeerror-cant-index-at-0-in-i8) that it is not [vectorizable](https://numba.pydata.org/numba-doc/dev/user/vectorize.html) because it cannot be made into a [universal function](https://docs.scipy.org/doc/numpy/reference/ufuncs.html). For a function to be universal, it is necessary that they map scalars into scalers, and map arrays into arrays. With that in mind, we'll vectorize a suitable function to show how the time performance is improved. Let's start by timing the unvectorized function.

```python
import numpy as np
import quantecon as qe

def f(x, y):
    return np.exp(np.abs(x -y**3)) *  np.cos(x**2 + y**2)

# generate data
grid = np.linspace(-3, 3, 1000)
x, y = np.meshgrid(grid, grid)

start = qe.util.tic()
f(x, y)
end = qe.util.toc()
```

On my machine the execution time was about 0.05 seconds, which isn't half-bad by itself. Not let's run the same code in vectorized form.

```python
from numba import vectorize
import numpy as np
import quantecon as qe

@vectorize
def f(x, y):
    return np.exp(np.abs(x -y**3)) *  np.cos(x**2 + y**2)

# generate data
grid = np.linspace(-3, 3, 1000)
x, y = np.meshgrid(grid, grid)

f(x,y) # precompile

start = qe.util.tic()
f(x, y)
end = qe.util.toc()
```

This vectorized form took about 0.0042 seconds to execute, which is about 12 times faster! This is a clear demonstration that vectorizing functions is worthwhile as scalability becomes an issue.

Because the vectorization of this function means that each element of the array is calculated independently, we can further attempt to speed this calculation up by calculating elements in parallel! We do that by telling the decorator the element types (we'll use `float64`), and that the target is function should be done in parallel.

```python
from numba import vectorize
import numpy as np
import quantecon as qe

@vectorize('float64(float64, float64)', target='parallel')
def f(x, y):
    return np.exp(np.abs(x -y**3)) *  np.cos(x**2 + y**2)

# generate data
grid = np.linspace(-3, 3, 1000)
x, y = np.meshgrid(grid, grid)

f(x,y) # precompile

start = qe.util.tic()
f(x, y)
end = qe.util.toc()
```

This last acceleration to make the calculations parallel squeezed the execution time down to 0.0031 seconds. This is only 0.0011 seconds faster than without the parallel execution, but still a worthwhile addition to the toolkit for doing independent calculations.

# Conclusion

Using Numba allows us an easy way to increase the performance of functions in Python without going to a lower-abstraction language such as C or FORTRAN. Some functions will be more suitable to `@jit` than `@vectorize` based on the type of operations and whether the function is universal (or can be made into a universal function). These accelerations in performance becomes increasingly valuable as the amount of data being processed becomes large!
