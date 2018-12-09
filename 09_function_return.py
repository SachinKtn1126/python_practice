# Title:                            Functions and return
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        07-12-2018
# Last modified date (DD-MM-YYYY):  07-12-2018
#
# ABOUT:
# In this code, functions are created and also one function returns a value

# Defining functions
def say_hi():
    print("Hello there")
say_hi()

def say_name(name):
    print ("Hello " + name)

# Prompting user to input value and calling the function
name = input("\nEnter your name: ")
say_name(name)

# Defining a function for name and age
def say_name_age(name, age):
    print("Hello " + name + ", your age is " + age)

# Prompting user to input values and calling the function
name = input("\nEnater your name: ")
age = input("\nEnater your age: ")
say_name_age(name,age)

# Defining a funtion that returns a value
def cube(num):
    return num*num*num

# prompting user to input a number and calling the function
num = input("Enter the number you want cube of: ")
print(cube(int(num)))




