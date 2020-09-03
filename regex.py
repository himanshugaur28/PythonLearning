# Python RegEx

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module

# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module:

import re


# Example

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


if x:
    print("yes we have a match")

else:
    print("no")


# ------------------- RegEx Functions --------------------

# The re module offers a set of functions that allows us to search a string for a match:

# Function	        Description

# findall	        Returns a list containing all matches
# search	        Returns a Match object if there is a match anywhere in the string
# split         	Returns a list where the string has been split at each match
# sub	            Replaces one or many matches with a string


# Metacharacters

# Metacharacters are characters with a special meaning:

# Character	        Description	                                                                    # Example

# []	            A set of characters	                                                            "[a-m]"
x = re.findall("[a-f]", txt)
print(x)


# \	                Signals a special sequence (can also be used to escape special characters)	    "\d"

txt = "this cost 1500$ rs"
x = re.findall("\d", txt)
print(x)


# .             	Any character (except newline character)	                                    "he..o"

txt = "hello world hero"
x = re.findall("he..o", txt)
print(x)

# ^                	Starts with	                                                                    "^hello"

x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")


# $	                Ends with	                                                                    "world$"

x = re.findall("hero$", txt)
if x:
    print("Yes, the string ends with 'hero'")
else:
    print("No match")


# *	                Zero or more occurrences	                                                    "aix*"

txt = "hello shein share"
# Check if the string contains "sh" followed by 0 or more "e" characters:
x = re.findall("she*", txt)
print(x)
if x:
    print("Yes, there is", len(x), "matches")
else:
    print("No match")

# +	                One or more occurrences	                                                        "aix+"

txt = "hello shein share"
# Check if the string contains "sh" followed by 1 or more "e" characters:
x = re.findall("she+", txt)
print(x)
if x:
    print("Yes, there is", len(x), "matches")
else:
    print("No match")


# {}	            Exactly the specified number of occurrences	                                    "al{2}"

txt = "The rain in Spain falls al alu allsss mainly in the plain!"

# Check if the string contains "a" followed by exactly two "l" characters:

x = re.findall("al{2}", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


# |	                Either or	                                                                    "falls|stays"

txt = "The rain in Spain falls stays mainly in the plain!"

# Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


# ()               	Capture and group


# Special Sequences

# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:


# Character	            Description	                                                                        Example


# \A	                Returns a match if the specified characters are
#                       at the beginning of the string	                                                    "\AThe"

txt = "Then rain in Spain"

# Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")


# \b	                Returns a match where the specified characters are                                  r"\bain"
#                       at the beginning or at the end of a word

txt = "The rain in Spain"

# Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

#                       (the "r" in the beginning is making sure that the
#                       string is being treated as a "raw string")                                          r"ain\b"

txt = "The rain in Spain"

# Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


# \B	                Returns a match where the specified characters are
#                       present, but NOT at the beginning (or at the end) of a word                         r"\Bain"
#                       (the "r" in the beginning is making sure that the string is                         r"ain\B"
#                       being treated as a "raw string")

# \d	                Returns a match where the string contains digits (numbers from 0-9)	                "\d"

# \D	                Returns a match where the string DOES NOT contain digits	                        "\D"

# \s	                Returns a match where the string contains a white space character	                "\s"

# \S	                Returns a match where the string DOES NOT contain a white space character	        "\S"

# \w	                Returns a match where the string contains any word characters
#                       (characters from a to Z, digits from 0-9, and the underscore _ character)	        "\w"

# \W	                Returns a match where the string DOES NOT contain any word characters	            "\W"

# \Z	                Returns a match if the specified characters are at the end of the string	        "Spain\Z"







# ============================================

# --------------- will do it later -----------------

# =============================================


print("hello")