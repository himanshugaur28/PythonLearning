# String Literals
# String literals in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".



# assign String to a variable

a = "Hello"
print(a)


# Multiline Strings

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)


# String are arrays

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# 0061    'a'; LATIN SMALL LETTER A
# 0062    'b'; LATIN SMALL LETTER B
# 0063    'c'; LATIN SMALL LETTER C

c = "Hello"
print(c[2])


# Slicing

d = "Hello World"
print(d[0:3])


# Negative indexing

e = "hello"
print(e[-4:-2])


# String length
print(len(e))



# ------------------   String Methods -------------------------

# strip() --- removes white spaces

f = " abc "
print(f.strip())

# lower()/upper() -- lowercase/uppercase the string

g = "HELLO"
print(g.lower())

h = "hello"
print(h.upper())

# replace() --- replace a string with another string

i = "hello tushar"
print(i.replace("tushar","himanshu"))


# split() ---- split the string into substrings if it finds instances of the separator

j = "tushar , himanshu"
print(j.split(","))


# check() ---- to check if certain phrase is present in a string, we can use the keywords in or not in

k = "this is dj tushar"
x = "dj" in k
print("is tushar a DJ: ",x) 
# not in
y = "dr." not in k
print("tushar is not a dr. :", y)


# String concatenation ---- To concatenate, or combine, two strings you can use the + operator.

l = "this"
m = "is"
n = "a laptop!"

o = l+m+n
print(o)

# to add space b/w strings

print("himanshu"+" "+"tushar")


# String format 

# age = 18
# name = "ram is "+age+" years old."
#print(name) #---------------------> this will give an error!

name = "ram is {} years old."
age = 18
print(name.format(age)) # ---------------> this is the correct method


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
myorder = "I want to pay {0} dollars for {2} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


# Escape Character ---- To insert characters that are illegal in a string, use an escape character.
                       #An escape character is a backslash \ followed by the character you want to insert.

# txt = "We are the so-called "Vikings" from the north."  ------------> will get an error if you use double quotes 
#                                                                       inside a string that is surrounded by double quotes

txt = "we are \"PROGRAMMERS\" from INDIA!"
print(txt)

#     Code	        Result	
#     \'	        Single Quote	
#     \\	        Backslash	
#     \n	        New Line	
#     \r	        Carriage Return	
#     \t	        Tab	
#     \b	        Backspace	
#     \f	        Form Feed	
#     \ooo	        Octal value	
#     \xhh	        Hex value




# --------------  String Methods -------------------

# capitalize() ----- Converts the first character to upper case

msg = "this is a collab"
print(msg.capitalize())


# casefold() ----- Converts string into lower case

string = "Yo Yo Honey Singh"
print(string.casefold())


# center()	----- Returns a centered string

# arguments --> 
#               length  -	Required. The length of the returned string
#               character	Optional. The character to fill the missing 
#                           space on each side. Default is " " (space)

string = "this is a laptop"
print(string.center(20,"-"))


# count() ----- Returns the number of times a specified value occurs in a string

# arguments -->
#                 value --	    Required. A String. The string to value to search for
#                 start --	    Optional. An Integer. The position to start the search. Default is 0
#                 end	--      Optional. An Integer. The position to end the search. Default is the end of the string


abc = "peetal k patile me papita peela peela"
print(abc.count("peela",0,35))


# encode() ---- Returns an encoded version of the string

xyz = "hey!  åthere i'm using python"
print(xyz.encode(encoding="ascii",errors="backslashreplace"))


# endswith() ---- Returns true if the string ends with the specified value


# Parameter	    Description
# value	        Required. The value to check if the string ends with
# start	        Optional. An Integer specifying at which position to start the search
# end            Optional. An Integer specifying at which position to end the search 


string1 = "this line ends with johny"
print("is string1 ending with johny : ",string1.endswith("johny"))


# expandtabs() ----	Sets the tab size of the string

string2 = "j\to\th\tn"
z = string2.expandtabs(10)
print(z)


# find() ---- Searches the string for a specified value and returns the position of where it was found

# Parameter	        Description
# value	            Required. The value to search for
# start	            Optional. Where to start the search. Default is 0
# end	            Optional. Where to end the search. Default is to the end of the string

# The find() ---- method finds the first occurrence of the specified value.

# The find() ---- method returns -1 if the value is not found.

# The find() --- method is almost the same as the index() method,
# the only difference is that the index() method raises an exception
#  if the value is not found. 

ax = "Never Give Up"
print(ax.find("Up",5,7))


# format_map() ----	Formats specified values in a string

# The format_map(mapping) is similar to str.format(**mapping) method.

# The only difference is that str.format(**mapping) copies the dict whereas 
# str.format_map(mapping) makes a new dictionary during method call. 
# This can be useful if you are working with a dict subclass

point = {'x':4,'y':-5,'z':7}
print('{x} {y} {z}'.format_map(point))
print(type('{x} {y}'.format_map(point)))


data = {'name':["ram","lucky"],'address':["bkn","jaipur"],'age':[18,16]}
print('this is {name[0]}, he lives in {address[0]}, he is {age[0]} years old.'.format_map(data))
print('this is {name[1]}, he lives in {address[1]}, he is {age[1]} years old.'.format_map(data))


# index() ---- Searches the string for a specified value and returns the position of where it was found

# Parameter	        Description
# value	            Required. The value to search for
# start	            Optional. Where to start the search. Default is 0
# end             	Optional. Where to end the search. Default is to the end of the string

string = "hello tushar"
print("tushar is at index : ",string.index("tushar"))


# isalnum() ----	Returns True if all characters in the string are alphanumeric (alphabet+numeric))

string = "hello123"
print(string.isalnum())


# isalpha() ---- Returns True if all characters in the string are in the alphabet

string = "123"
print(string.isalpha())


# isdecimal()	Returns True if all characters in the string are decimals

string = "12"
print(string.isdecimal())


# isdigit() ---- Returns True if all characters in the string are digits

string = "1.2"
print(string.isdigit())


# isidentifier() ---- Returns True if the string is a valid identifier

txt = '1for'
print(txt.isidentifier())



# islower() ----	Returns True if all characters in the string are lower case

txt = "this is awesome"
print(txt.islower())


# isnumeric() ---- Returns True if all characters in the string are numeric

num = "1324"
print(num.isnumeric())


# isprintable() ---- Returns True if all characters in the string are printable

txt = "qwerty"
print(txt.isprintable())


# isspace() ---- Returns True if all characters in the string are whitespaces

txt = "          "
print(txt.isspace())


# istitle() ---- Returns True if the string follows the rules of a title
                 #make the first letter capital in each word    
                 #Note that the first letter after a non-alphabet letter is converted into a upper case letter
txt = "Hello This is a title"
print(txt.istitle())


# isupper() ----	Returns True if all characters in the string are upper case

txt = "HeLLo"
print(txt.isupper())


# join() ----  Joins the elements of an iterable to the end of the string

lst = ["tushar","himanshu","rohan"]
x = "#".join(lst)
print(x)


# ljust()	Returns a left justified version of the string

# Parameter	        Description
# length	        Required. The length of the returned string
# character	        Optional. A character to fill the missing space (to the right of the string). Default is " " (space).

txt = "tushar"
print(txt.ljust(20,"*"))
print(txt.rjust(20,"@"))

# lstrip() ---- Returns a left trim version of the string

txt = "          Himanshu naam to suna hi hoga"
print(txt.lstrip())

# maketrans() ---- Returns a translation table to be used in translations
txt = "Hello Sam!"
mytable = txt.maketrans("H", "P")
print(txt.translate(mytable))


# partition() ---- Returns a tuple where the string is parted into three parts

txt = "I can eat bananas all day"

x = txt.partition("bananas")

print(x)


# replace() ---- Returns a string where a specified value is replaced with a specified value

txt = "hello tushar"
print(txt.replace("tushar","himanshu"))


# rfind()	Searches the string for a specified value and returns the last position of where it was found

# Parameter	        Description
# value	        Required. The value to search for
# start	        Optional. Where to start the search. Default is 0
# end	            Optional. Where to end the search. Default is to the end of the string


txt = "Hello, welcome to my world."

x = txt.rfind("e")
y = txt.find("e")

print(x)
print(y)


# rindex()	Searches the string for a specified value and returns the last position of where it was found

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)


# rjust()	Returns a right justified version of the string

txt = "banana"

x = txt.ljust(20)
print(x, "is my favorite fruit.")
x = txt.rjust(20)
print(x, "is my favorite fruit.")


# rpartition() ---- Returns a tuple where the string is parted into three parts

# Search for the last occurrence of the word "bananas", and return a tuple with three elements:

# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)


# rsplit()	Splits the string at the specified separator, and returns a list
# Split a string into a list, using comma, followed by a space (, ) as the separator:

# Parameter	Description
# separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"


txt = "tushar,himanshu,rohan,ram,lucky"
x = txt.rsplit(",",1) # splits into n+1 elements
print(x)


# rstrip()	Remove any white spaces at the end of the string

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")


# split()  Split a string into a list where each word is a list item

txt = "this is a laptop"
x = txt.split()
print(x)


# splitlines() ---- Splits the string at line breaks and returns a list

txt = """hey this is himanshu
         this is tushar"""
print(txt.splitlines())


# startswith() ---- Returns true if the string starts with the specified value

# Parameter 	Description
# value	        Required. The value to check if the string starts with
# start	        Optional. An Integer specifying at which position to start the search
# end	        Optional. An Integer specifying at which position to end the search

txt = "hey this is himanshu "
print(txt.startswith("is",9))


# swapcase() ---- Swaps cases, lower case becomes upper case and vice versa

txt = "small CAPITAL"
print(txt.swapcase())


# title() ---- Converts the first character of each word to upper case

txt = "its yo boy raftaar"
x = txt.title()
print(x)


# translate() ---- Returns a translated string

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


# zfill()	Fills the string with a specified number of 0 values at the beginning

# Fill the string with zeros until it is 10 characters long
txt = "50"
x = txt.zfill(10)
print(x)