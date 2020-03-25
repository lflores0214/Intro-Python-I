"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
import platform
import socket
# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for arg in sys.argv:
      print("sys.argv", arg)


# Print out the OS platform you're using:
# YOUR CODE HERE
print("os name", os.name)
print("platform system", platform.system())
print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("python version #",
      sys.version_info[0], ".", sys.version_info[1], ".", sys.version_info[2])

# Print the current process ID
# YOUR CODE HERE
print("process ID", os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print("CWD", os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
import getpass
print("socket hostname",socket.gethostname())
print("os hostname",os.uname()[1])
print(os.getlogin())
