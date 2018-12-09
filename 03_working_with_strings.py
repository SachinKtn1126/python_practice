# Title:                            Working with strings
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        07-12-2018
# Last modified date (DD-MM-YYYY):  07-12-2018
#
# ABOUT:
# This code uses a variable to store a string value
# then various string functions are tested in print command

print("\"Python\"\nBest language to learn")

# variable defined with value:

phrase = "Rud Raw Tattoos"
print(phrase)

# print the string in upper case:

print(phrase.upper())
print(phrase.upper().isupper())

# check the length of the string:

print(len(phrase))

# print the letter in index number 2
print(phrase[2])

# print the index number of the letter u
print(phrase.index("R"))

# Replace the word 'Rud' by 'Red'
print(phrase.replace("Rud", "Red"))

