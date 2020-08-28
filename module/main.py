# Python Modules
# Consider a module to be the same as a code library.

# A file containing a set of functions you want
# to include in your application.


# Create a Module
# To create a module just save the code you want
# in a file with the file extension .py :

from mymodule import data
import platform
import mymodule as md

md.sayhello("Rohan")


print("his name is", md.data["name"])
print("his hobby is", md.data["hobby"])
print("he lives in", md.data["city"])


# ------- Built-in Modules ---------

# There are several built-in modules in Python,
# which you can import whenever you like.


x = platform.system()
print(x)  # return os of user


# -------- using the dir() -------------

# There is a built-in function to list all the function
# names (or variable names) in a module. The dir() function:

# Example

# List all the defined names belonging to the platform module:


x = dir(platform)
print(x)


# ----------- Import From Module --------------

# You can choose to import only parts from a module, by using the
# from keyword.


print(data["name"])
