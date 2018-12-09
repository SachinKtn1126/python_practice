# Title:                            Creating a better calculator
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        07-12-2018
# Last modified date (DD-MM-YYYY):  07-12-2018
#
# ABOUT:
# This code is to create a better calculator using if else statement and user input.

# Input values from the user and store it in variables
num1 = float(input("Enter num 1: "))
op = input("Enter operator: ")
num2 = float(input("Enter num 2: "))

# Performing mathematical functions using the if else statement
if op == "+":
    print("The sum is " + str(num1 + num2))
elif op == "-":
    print("The difference is " + str(num1 - num2))
elif op == "/":
    print("The division is " + str(num1 / num2))
elif op == "*":
    print("The multiple is " + str(num1 * num2))
elif op == "%":
    print("The modulus is " + str(num1 % num2))
else:
    print("Invalid operator")
