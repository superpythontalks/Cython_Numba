"""Test numba for accelerating pure python mean() function"""

from python_example import python_mean, x

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

# can use numba.vectorize to parallelize your code
