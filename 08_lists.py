# Title:                            Lists in python
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        07-12-2018
# Last modified date (DD-MM-YYYY):  07-12-2018
#
# ABOUT:
# This code is to test various functions and methods to use a list in Python

# Defining lists:
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
lucky_numbers = [4, 12, 8, 15, 42, 26]
print(friends)
print(lucky_numbers)

# Replacing the value at index 3 in list "friends"
friends[3] = "Mike"
print(friends)

# Printing values of list using the index numbers
print(friends[1])
print(friends[-2])
print(friends[3])

# Add a new value at the end of the list "friends"
friends.append("Roy")
print(friends)

# Add a new value in between of the list "friends"
friends.insert(1, "Kelly")

# Remove a value from the list "friends"
friends.remove("Toby")

# Create a copy of list "friends"
friends2 = friends.copy()
print(friends2)

# pop - removes the last value of the list
friends.pop()
print(friends)

# clear - clears all the vlues in the list
friends2.clear()
print(friends2)

# get the index number of the value in the list
print(friends.index("Oscar"))

# get the count of how many times the value repeats in the list
print(friends.count("Jim"))

# print the list in ascending order
print(lucky_numbers.sort())

# print the list in the descending order
print(lucky_numbers.reverse())



