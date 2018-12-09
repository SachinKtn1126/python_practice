# Title:                            Objects and functions
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# This code imports the "student" class from "student_class"
# Please refer to "student_class.py" for the class code

# Importing the class student from student_class
from student_class import student

# New variables created using the student class
student1 = student("Oscar", "Accounting", 3.1)
student2 = student("Phyllis", "Business", 3.8)

# using the function from the student class
print(student1.on_honor_roll())
print(student2.on_honor_roll())
