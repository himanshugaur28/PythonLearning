# Tuple
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)


# Access Tuple Items

print(thistuple[1])

# Negative Indexing

print(thistuple[-1])


# Range of Indexes

print(thistuple[2:5])
print(thistuple[-4:-1])


# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.


# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

for x in thistuple:
    print(x)


# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

if "apple" in thistuple:
    print("apple is in this tupple")


# Tuple Length
# To determine how many items a tuple has, use the len() method:

print(len(thistuple))


# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

"""thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)"""


# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.


thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))


# Remove Items
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:

del thistuple


# Join Two Tuples
# To join two or more tuples you can use the + operator:


tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

x = thistuple.count("cherry")
print(x)

y = thistuple.index("cherry")
print(y)
