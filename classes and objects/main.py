# Python Classes and Objects

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its
# properties and methods.
# A Class is like an object constructor, or a "blueprint"
# for creating objects.


# Create a Class
# To create a class, use the keyword class:

class MyClass:
    x = 5


# Create object

p1 = MyClass()
print(p1.x)


# ------------ The __init__() Function ----------

# The examples above are classes and objects in their simplest
# form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the
# built-in __init__() function.

# All classes have a function called __init__(), which is always
# executed when the class is being initiated.

# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is
# being created:

# Example

# Create a class named Person, use the __init__() function to assign
# values for name and age:

class Person:
    def __init__(self, a_name, a_age, a_salary):
        self.name = a_name
        self.age = a_age
        self.salary = a_salary


p1 = Person("Johny", 36, 120000)
p2 = Person("Sins", 34, 13000)
print(p1.name)
print(p1.age)
print(p1.salary)


# Object Methods
# Objects can also contain methods. Methods in objects are functions
# that belong to the object.

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello my name is " + self.name)


p1 = Person1("John", 36)
p1.sayHello()


# --------- The self Parameter -------------


# Note: The self parameter is a reference to the current
# instance of the class, and is used to access variables
# that belong to the class.

# It does not have to be named self , you can call it whatever you
# like, but it has to be the first parameter of any function in the
# class:

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person2("Rohan", 36)
p1.myfunc()


# Modify Object Properties
# You can modify properties on objects like this:

p1.age = 40
print(p1.age)


# Delete Object Properties

del p1.age


# Delete Objects

del p1


# pass Stetement

class Person3:
    pass


# without contructor

class Student:
    pass


rahul = Student()

rahul.age = 10

print(rahul.age)
