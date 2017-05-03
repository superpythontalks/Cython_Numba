"""Simple demo of ctypes in action, using libc's printf() function"""

import ctypes
libc = ctypes.cdll.LoadLibrary("libc.so.6")
printf = libc.printf
printf(b"Hello, %s\n", b"world!") # also returns the number of characters printed
# note that strings have to be specified as raw bytes (leading 'b') for C to understand them,
# because in Python 3, strings are unicode, which are a different format from plain ASCII
