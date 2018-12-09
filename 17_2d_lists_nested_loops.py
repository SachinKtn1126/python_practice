# Title:                            2D list and nested loops
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# This code is to try and tes the 2D list and the nested loop

# Defining the 2D List
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])
print(number_grid[1][2])

# Using for loop, print each row from the 2D list
for row in number_grid:
    print(row)

# Using nested loop, print each value of the 2D list in each line
for row in number_grid:
    for col in row:
        print(col)
