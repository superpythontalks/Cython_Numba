"""Define a mean() function in pure Python"""

import numpy as np

def mean(x):
    sumvals = 0.0
    # sum up values in x, divide by number of values:
    for val in x:
        sumvals += val
    return sumvals / len(x)

N = 1000000
x = np.random.random(N)
