# Defining the student class and its object

class student:
    def __init__(self, name, major, gpa):          # Self initialising the objects
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):                        # a new function that returns boolean value for the input object
        if self.gpa >= 3.5:
            return True
        else:
            return False
