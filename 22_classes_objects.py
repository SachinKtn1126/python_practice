# Title:                            Classes and Objects
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# This code imports the "student" class from "student_class"
# Please refer to "student_class.py" for the class code

# Import thr student class from the student_class
from student_class import student

# Defining a new variable with values being passed as object to the class
student1 = student("Jim", "Business", 3.1, False)

print(student1.gpa)