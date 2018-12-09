# Title:                            Translator
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# Please refer to 18_readme_translator.txt
# Here user's input string is translated to RUD RAW LANGUAGE

# Defining a function to carries out the translation
def translate(phrase):
    translation = ""                                # Variable to store the translated string
    for letter in phrase:                           # For loop to carry the translation letter by letter
        if letter.lower() in "aeiou":               # translation condition
            if letter.isupper():                    # If statement to translate the letter to RUD RAW LANGUAGE
                translation = translation + "R"     # append the translated letter to translation variable
            else:
                translation = translation + "r"     # append the translated letter to translation variable
        else:
            translation = translation + letter      # append the letter to translation variable
    return translation                              # return the string in translation

# Prompt user to input a string value
phrase = input("Please enter a word or a phrase: ")

# Call the translate funtion and print the translated value
print("\nThe translation is: " + translate(phrase))
