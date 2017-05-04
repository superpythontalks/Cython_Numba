"""Test numba for accelerating python_mean() function"""

from python_example import python_mean, python_rms, x

# plain python:
%timeit python_mean(x) ## takes about 80 ms per loop

# numba:
from numba import jit
numba_mean = jit(python_mean)
%timeit numba_mean(x) ## also 1.2 ms per loop, about 66x faster!

# numpy is still faster:
%timeit x.mean() ## 0.37 ms per loop, about 215x faster!
%timeit np.mean(x) ## also 0.37 ms per loop, about 215x faster!


# other numba options:
numba_mean_nopython = jit(mean, nopython=True)
numba_mean_nogil = jit(mean, nogil=True)
numba_mean_nopython_nogil = jit(mean, nopython=True, nogil=True)
# for this simple example, it seems the nopython and nogil kwargs don't help:
%timeit numba_mean_nopython(x) ## also 1.2 ms per loop, about 66x faster!
%timeit numba_mean_nogil(x) ## also 1.2 ms per loop, about 66x faster!
%timeit numba_mean_nopython_nogil(x) ## also 1.2 ms per loop, about 66x faster!

# You can use numba.vectorize to parallelize your code

"""Test numba for accelerating python_rms() function"""

# plain python:
%timeit python_rms(x) ## takes about 132 ms per loop

# numba:
numba_rms = jit(python_rms)
%timeit numba_rms(x) ## 1.2 per loop, about 108x faster!
