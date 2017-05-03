"""Define a mean() function in Cython. Use `cython -a cython_mean.pyx` to create an annotated
.html file highlighting any inefficiencies in how this function is defined

Can also use a .pyxbld file with same name to enable multithreading with OpenMP
"""

def cython_mean(double[:] x):
    cdef double sumvals = 0.0
    cdef int n = len(x)
    for i in range(n):
        sumvals += x[i]
    print('hi')
    return sumvals / n
