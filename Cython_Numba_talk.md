# Accelerate your code with Cython and Numba

- Outline
    - Python C extensions
        - ctypes
    - Cython
    - Numba

## what happens when you type `python`?

- runs a program called "python"
- Python is actually a C program
    - source code for Python itself is written in C, called CPython
    - alternate implementations in other langauges
        - Java: Jython
        - C#: IronPython
        - Python: PyPy

## why write C extensions?

1. create Python interface to a C library
    - example: data acquisition system that only comes with a C interface
    - write C extension which allows Python access to that C library, and therfore the acquisition hardware
    - writing C extensions by hand is **tedious** and **difficult**
    - `DT.c` example
    - accessing C libraries is now much easier using builtin module `ctypes`
        - lets you directly call any C library function from within Python

2. accelerate your code!
    - code written in C won't have overhead of Python, can *potentially* run much faster

## when *not* to accelerate your code:

- when it doesn't matter - don't waste time optimizing code that doesn't take much time anyway

> "Premature optimization is the root of all evil" — Donald Knuth

- Pareto principle, i.e. 80/20 rule, i.e. power law
    - probably some small part of your code takes up most of the execution time
- find the part of your code that's the slowest, work on that
    - profile your code to find the slowest parts:
    - `import profile`, `import cProfile`, or in IPython use `prun`

## first and best option: numpy!

- vectorize! (see upcoming Super Python talk)
- but some complex loops you simply can't vectorize with numpy
- sometimes you need complicated loop that iterates over every entry in an array
- GAC clustering algorithm example

## Cython: http://cython.org

- a much easier way to write C extensions
- Cython language is superset of Python
    - Python code + static C type declarations
1. write your extension in Cython syntax in `.pyx` file
2. "cython" it to generate C code
3. compile the C code with a compiler
4. import the compiled C extension from within Python
    - `import myextension`
- given a .pyxbld file whose name matches the .pyx file, all this happens automatically on import
- in IPython, `%%cython` denotes a block of Cython code

## what's the GIL?

- Global Interpreter Lock
- allows for reference tracking to objects, and therefore garbage collection and therefore automatic memory deallocation when an object is no longer needed
- this in incompatible with multithreading
    - multithreading vs. multiprocessing
        - single process w/ shared memory vs. separate processes w/ separate memory
- turning off the GIL allows you to use multithreading, exposes you to the risks
    - however, if your threads are simple, i.e. your code is "embarassingly parallel", then it's relatively safe, with big payoff
- `nogil`
- openMP

## Numba: http://numba.pydata.org

- newer than Cython, maybe less stable/mature
- numba is harder to install, so harder to distribute code that relies on numba
- but, Numba is **much** simpler than Cython. It's close to magic!
- should work out of the box in Anaconda distribution on any platform
- installing separately is a bit tricky:
    - need to install the LLVM compiler "system"
        - LLVM = low-level virtual machine originally
        - like an alternative to GCC, allows for "just in time compiling" similar to Java, but for any language, including C and Python

## jit

- `@jit`, or `jit()`
    - what's a decorator?
    - dynamically modifies a function/method
        - little bit analogous to subclassing a class and redefining some methods
        - basically: wraps a function in other code. A decorator gets the original function and its arguments as arguments, and can then do whatever it wants with it. To stop decorating, remove the @decorator, or the decorator() call
- `jit(nopython=True)`
- `guvectorize`
- http://numba.pydata.org/numba-doc/dev/user/examples.html

## More comparisons:

- https://jakevdp.github.io/blog/2013/06/15/numba-vs-cython-take-2/
    - comparison of plain python, numpy, cython, numba, and other acceleration methods,
    - uses example of calculating a matrix of pairwise distances
