# properties      ordered      changeable     duplicable

# List []           yes          yes               yes
# Tuple ()          yes          no                yes
# Set {}            no           /////             no
# Dict {key:val}    no           yes               no



# example of a list
lst = [1,2,3,4]
print(lst)


# access item
print(lst[0])


# negative indexing
print(lst[-1])


# range of indexes
print(lst[0:2])

print(lst[:2])

print(lst[1:])

# range of negative indexing
print(lst[-4:-2])
print(lst[-2:-4:-1])


# reverse a list
print(lst[::-1])


# change item value
lst[1] = "one"
print(lst)


# loop through a list

for x in lst:
    print(x)

# for making numeric tables 

table = [1,2,3,4,5]
for y in table:
    print(5,"*",y,"=",5*y)


# check if item exists

guests = ["tushar","himanshu","rahul","rohan"]

if "tushar" in guests:
    print("yes, tushar is in guestlist!")
else:
    print("no, tushar is not invited :(")



# list length

print("total number of guest : ",len(guests))


# add items --  at last position

guests.append("naveen")
print(guests)


# insert --  at particular index

guests.insert(2,"lomad")
print(guests)


# remove  -- specific item

guests.remove("lomad")
print(guests)


# pop   -- of specific index / last item if index not mentioned

guests.pop(2)
print(guests)


# del -- of specific index /  index must be given

del guests[0]
print(guests)


# clear -- delete all items of the list

lst.clear()
print(lst)


# copy a list 

guests2 = guests.copy()
print(guests2)


# join two lists

lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]

lst3 = lst1 + lst2
print(lst3)


# joining two list using loop

for x in lst2:
    lst1.append(x)

print(lst1)


# extend 

a = ["a","b","c"]
b = ["d","e","f"]

a.extend(b)
print(a)


# list constructor

list_a = list((1,2,3,4,5))
print(list_a)