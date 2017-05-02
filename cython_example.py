"""Test mean() function written in Cython"""

from mean import mean, x

# plain python:
%timeit mean(x) ## takes about 80 ms per loop

# Cython:
import pyximport
# tell Cython to create .c files locally, and to compile them locally as well,
# i.e., don't do it in some temporary directory:
pyximport.install(build_in_temp=False, inplace=True)
from cython_mean import cython_mean, cython_mean_2, cython_mean_3
%timeit cython_mean(x) ## 1.2 ms per loop, about 66x faster!
%timeit cython_mean_2(x) ## 1.2 ms per loop, about 66x faster!

# numpy:
%timeit x.mean() ## 0.37 ms per loop, about 215x faster!
%timeit np.mean(x) ## also 0.37 ms per loop, about 215x faster!
