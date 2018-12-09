# Title:                            Dictionaries in Python
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# This code is to try and test how to use dictionaries in python

# Defining dictionaries
day_convert = {
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday"
}

month_convert = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Printing values from the dictionaries
print(day_convert["Mon"])
print(day_convert.get("Sun", "Invalid key"))
print(day_convert.get("TUH", "Invalid key"))
print(month_convert[1])
print(month_convert.get(6, "Invalid key"))
print(month_convert.get(14, "Invalid key"))

