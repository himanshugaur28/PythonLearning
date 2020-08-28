# Python Lambda

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments,
# but can only have one expression.

# Syntax
# lambda arguments : expression

# The expression is executed and the result is returned:

# ----------- Example ------------------
#  A lambda function that adds 10 to the number passed in as an argument,
# and print the result:

def x(a): return a + 10


print(x(5))


def y(a, b): return a*b


print(y(2, 3))


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as
# an anonymous function inside another function.

# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:

x = int(input("enter number : "))


def myfunc(n):
    return lambda a: a * n


double_it = myfunc(3)

print(double_it(x))

print("hello")
