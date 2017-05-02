"""Simple demo of ctypes in action, using libc's printf() function"""

import ctypes
libc = ctypes.cdll.LoadLibrary("libc.so.6")
printf = libc.printf
printf(b"Hello, %s\n", b"world!") # also returns the number of characters printed
