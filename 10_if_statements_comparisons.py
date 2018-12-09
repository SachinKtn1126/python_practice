# Title:                            If statement in python
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        07-12-2018
# Last modified date (DD-MM-YYYY):  07-12-2018
#
# ABOUT:
# This code is to try and test the working of if statement

# Defining boolean variables
is_male = False
is_tall = False

# If statement
if is_male:
    print("You are male")
else:
    print("You are female")

# If else statement
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("Ypu are a tall female")
else:
    print ("you are a short female")

# Defining a function to return the maximum number from 3 numbers
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Input values from the user
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
num3 = input("Enter num3: ")

# calling the function to get the max number and printing it
print("The maximum number is " + str(max_num(int(num1), int(num2), int(num3))))

