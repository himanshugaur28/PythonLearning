# Adds an element at the end of the list
lst = []
lst.append(21)
lst.append(28)
lst.append(28)
lst.append("GAUR")
print(lst)
# Removes all the elements from the list
lst.clear()
print(lst)
# Returns a copy of the list
lst.copy()
print(lst)
lst1=[21,21,28,28,"gaur","gaur"]
print(lst1)
# Returns the number of elements with the specified value
print(lst1.count(28))
cars = ["lamborg","audi","verna"]
# Add the elements of a list (or any iterable), to the end of the current list
cars.extend(lst1)
print(cars)
# Returns the index of the first element with the specified value
print(cars.index("lamborg"))
# Adds an element at the specified position
cars.insert(2,"fortuner")
print(cars)
# Removes the element at the specified position
cars.pop(2)
print(cars)
# Removes the first item with the specified value
lst1.remove(28)
print(lst1)
cars = ["lamborg","audi","verna"]
# Reverses the order of the list
cars.reverse()
print(cars)
# Sorts the list
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)