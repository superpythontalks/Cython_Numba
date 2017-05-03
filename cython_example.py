"""Test function(s) written in Cython"""

from python_example import python_mean, x

# plain python:
%timeit python_mean(x) ## takes about 80 ms per loop

# Cython:
import pyximport
# tell Cython to create .c files locally, and to compile them locally as well,
# i.e., don't do it in some temporary directory:
pyximport.install(build_in_temp=False, inplace=True)
from cython_mean import cython_mean # compiles on import

%timeit cython_mean(x) ## 1.2 ms per loop, about 66x faster!

# numpy is still faster:
%timeit x.mean() ## 0.37 ms per loop, about 215x faster!
%timeit np.mean(x) ## also 0.37 ms per loop, about 215x faster!
