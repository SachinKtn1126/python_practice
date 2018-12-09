# Title:                            Inheritance in Python
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# This code imports the "Chef" and "ChineseChef" class
# ChineseChef inherits all the function from Chef
# Please refer to "Chef.py" and "ChineseChef.py" for the class code

# Importing the Chef and ChineseChef classes
from Chef import Chef
from ChineseChef import ChineseChef

# Defining the chefs 1 and 2
myChef1 = Chef()
myChef2 = ChineseChef()

# Calling the functions of the classes
myChef1.makes_chicken()
myChef1.makes_special_dish()
myChef2.makes_fried_rice()
myChef2.makes_salad()
