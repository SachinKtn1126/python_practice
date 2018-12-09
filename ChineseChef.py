# Importing Chef class into ChineseChef
from Chef import Chef

# Defining new functions for ChineseChef
class ChineseChef(Chef):

    def makes_special_dish(self):
        print("The chef makes orange chicken")

    def makes_fried_rice(self):
        print("The chef makes fried rice")
