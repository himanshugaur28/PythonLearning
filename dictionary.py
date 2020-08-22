# A dictionary is a collection which is unordered,
# changeable and indexed. In Python dictionaries are
# written with curly brackets, and they have keys and values

# Create and print a dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)


# Accessing Items

# You can access the items of a dictionary by referring
# to its key name, inside square brackets:

x = thisdict["model"]
print(x)

# There is also a method called get() that will give you
# the same result:

# Get the value of the "model" key:

x = thisdict.get("model")
print(x)


# Change Values

# You can change the value of a specific item by
# referring to its key name:
# Change the "year" to 2018:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)


# Loop Through a Dictionary

# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are
# the keys of the dictionary, but there are methods to
# return the values as well.

# Print all key names in the dictionary, one by one:


for x in thisdict:  # FOR KEYS ONLY
    print(x)


for x in thisdict:  # FOR VALUES ONLY
    print(thisdict[x])


for x in thisdict:    # FOR KEYS AND VALUES
    print(x, thisdict.get(x))

    #    OR

for x in thisdict.values():
    print(x)


# Check if Key Exists

# To determine if a specified key is present in a
# dictionary use the in keyword:

if "model" in thisdict:
    print("'model' is a key in given dictionary")


# Dictionary Length

# To determine how many items (key-value pairs) a
# dictionary has, use the len() function

print(len(thisdict))


# Adding Items

# Adding an item to the dictionary is done by using a
# new index key and assigning a value to it:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


# Removing Items

# There are several methods to remove items from a dictionary:

# The pop() :- method removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() :- method removes the last inserted item
# (in versions before 3.7, a random item is removed instead):

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)


# The del keyword removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)


# The del keyword can also delete the dictionary completely:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
# print(thisdict) this will cause an error because "thisdict" no longer exists.


# The clear() method empties the dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)


# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1,
# because: dict2 will only be a reference to dict1, and
# changes made in dict1 will automatically also be made in
# dict2.

# There are ways to make a copy, one way is to use the
# built-in Dictionary method copy()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)


# Nested Dictionaries

# A dictionary can also contain many dictionaries, this is
# called nested dictionaries.

# Create a dictionary that contain three dictionaries:

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)
# Or, if you want to nest three dictionaries that
# already exists as dictionaries:

# Create three dictionaries, then create one dictionary
# that will contain the other three dictionaries:

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

# The dict() Constructor
# It is also possible to use the dict() constructor
# to make a new dictionary:

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


# -------------------Dictionary Methods----------------


# fromkeys() :- Returns a dictionary with the specified keys and value

# Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)


# items() :- Returns a list containing a tuple for each key value pair

# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
# The view object will reflect any changes done to the dictionary, see example below.


# Return the dictionary's key-value pairs:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)
print(type(x))


# keys() Returns a list containing the dictionary's keys

print(car.keys())


# setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value, see example below


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)


# update() Updates the dictionary with the specified key-value pairs

# The update() method inserts the specified items to the dictionary.
# The specified items can be a dictionary, or an iterable object.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.update({"color": "White"})

print(car)


# values() Returns a list of all the values in the dictionary

# The values() method returns a view object. The view object contains the values of the dictionary, as a list.
# The view object will reflect any changes done to the dictionary, see example below

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)