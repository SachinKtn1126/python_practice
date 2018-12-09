# Title:                            Exponent function
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# This code has function to calculate the exponent of the values input by the user
# eg: 2^3 = 8 (i.e.: 2*2*2 = 8)

# Defining the function
def raise_to_power(base_num, power_num):
    result = 1                                  # setting the variable "result" as 1 to calculate 1*base_num = result
    for index in range(power_num):              # For loop to repeat the multiplication for the given power
        result = result * base_num
    return result                               # return the result whn function is called

# Get inputs from the user
base_num = int(input("Enter the base number: "))
power_num = int(input("Enter the power: "))

# Call the funtion and print the result
print("\nThe exponent is: "+ str(raise_to_power(base_num, power_num)))
