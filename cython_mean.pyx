"""Define a mean() function in Cython. Use `cython -a cython_mean.pyx` to create an annotated
.html file highlighting any inefficiencies in how this function is defined

Can also use a .pyxbld file with same name to enable multithreading with OpenMP
"""

def cython_mean(double[:] x):
    """Takes numpy 1D double (float64) array, returns mean"""
    cdef double sumvals = 0.0 # declare static type of internal variable
    cdef int n = len(x)
    for i in range(n):
        sumvals += x[i]
    return sumvals / n

# other options that might speed things up further:
#@cython.boundscheck(False)
#@cython.wraparound(False)
