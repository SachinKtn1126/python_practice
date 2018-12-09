# Title:                            Reading from files
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# this code is to test methods of how to read values from an external file

# open file connection with read permission
emp_file = open("employees.txt", "r")

# Check if file is readable
print(emp_file.readable())

# Print all the content of the file
print(emp_file.read())

# Print the content of the file line by line
print(emp_file.readline())
print(emp_file.readline())

# Print the content of the file based on the line index number
print(emp_file.readlines())
print(emp_file.readlines()[1])

# For loop to print the content of the file line by line
for employee in emp_file.readlines():
    print(employee)

# Close the file connection
emp_file.close()
