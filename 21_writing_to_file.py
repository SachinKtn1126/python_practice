# Title:                            Writing to files
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# This code is to test methods of how to write values to an external file

# Open the file connection with append rights
emp_file = open("employees.txt", "a")

# Append nes lines to the file
emp_file.write("Toby - HR")
emp_file.write("\nKelly - Customer support")

# Close the append file connection
emp_file.close()

# Open the connection to file with write rights
emp_file = open("employees1.txt", "w")

# With write rights, the file get over written with new values
emp_file.write("Toby - HR")
emp_file.write("\nKelly - Customer support")

# Close the write file connection
emp_file.close()
