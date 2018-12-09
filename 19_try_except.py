# Title:                            Try-Except in python
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# this code is to test the Try-Except method in python for error handling

# Initialising Try. All the code/computing should be done inside try
try:
    # Prompt user to input values and print the output
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    print(num1 / num2)

# except - print the error statement based on error type
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input")
