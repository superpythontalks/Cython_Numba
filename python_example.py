"""Define some functions in pure Python"""

import numpy as np

def python_mean(x):
    sumvals = 0.0
    # sum up values in x, divide by number of values:
    for val in x:
        sumvals += val
    return sumvals / len(x)

def python_rms(x):
    sumsquares = 0.0
    for val in x:
        sumsquares += val*val
    return np.sqrt(sumsquares / len(x))


N = 1000000 # that's a lot
x = np.random.random(N)
