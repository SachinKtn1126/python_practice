# Title:                            For loop in python
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# This is a practice code to test and try the for loop

# To print each letter in the given string
for letter in "Sachin Kotian":
    print(letter)

# To print each value in the given list
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

# To print each number in the given range
for index in range(3, 10):
    print(index)

# To print each value in the given list for every available index of the list
for index in range(len(friends)):
    print(friends[index])

# Combination of for loop and if statement ot print index number of the given range
for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print(index)
