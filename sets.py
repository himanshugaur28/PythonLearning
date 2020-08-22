# Python Sets

# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

# Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)


# Access Items

# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


# Check if "banana" is present in the set:

print("banana" in thisset)


# Change Items
# Once a set is created, you cannot change its items, but you can add new items.


# Add Items

# To add one item to a set use the add() method.

# To add more than one item to a set use the update() method.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# Add multiple items to a set, using the update() method:

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)


# Get the Length of a Set
# To determine how many items a set has, use the len() method.

print(len(thisset))


# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

# Note: If the item to remove does not exist, remove() will raise an error.

thisset.remove("banana")
print(thisset)


# Remove "banana" by using the discard() method:
# Note: If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)


# Join Two Sets
# There are several ways to join two or more sets in Python.

# You can use the union() method that returns
# a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another:

# using union method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# using update method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.


# The set() Constructor
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)


# set methods

# add()	Adds an element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)


# clear()	Removes all the elements from the set
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)


# copy() Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)


# difference() Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)


# difference_update() Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)


# discard() Remove the specified item
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)


# intersection() Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


# intersection_update() Removes the items in this set that are not present in other, specified set(s)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


# isdisjoint() Returns whether two sets have a intersection or not
# if no intersection it is disjont
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)


# issubset() Returns whether another set contains this set or not
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)


# issuperset() Returns whether this set contains another set or not
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


# symmetric_difference() Returns a set with the symmetric differences of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


# symmetric_difference_update() inserts the symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
