# python has following datatypes

# Text Type       :	    str
# Numeric Types   :	    int, float, complex
# Sequence Types  :	    list, tuple, range
# Mapping Type    :	    dict
# Set Types       :	    set, frozenset
# Boolean Type    :     bool
# Binary Types    :     bytes, bytearray, memoryview


# getting the datatype

x = 5
print(type(x))


# setting the datatype

a = "hello world"                                           # str
b = 5                                                       # int   
c = 20.5                                                    #float
d = 1j                                                      #complex
e = ["apple", "banana", "cherry"]                           #list
f = ("apple", "banana", "cherry")                           #tuple
g = range(10)                                               #range
h = {"name":"tushar","age":"18"}                            #dict
i = {"apple", "banana", "cherry"}                           #set
j = frozenset({"apple", "banana", "cherry"})                #frozenset
# print(j)
k = True                                                    #bool
l = b"hello"                                                #bytes
# print(l)                                                
m = bytearray(5)                                            #bytarray
# print(m)
n = memoryview(bytes(5))                                    #memoryview
# print(n)

# setting the specific datatype

x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)	
x = dict(name="John", age=36)		
x = set(("apple", "banana", "cherry"))	
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)		
x = bytes(5)	
x = bytearray(5)	
x = memoryview(bytes(5))	