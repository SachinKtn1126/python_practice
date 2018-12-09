# Title:                            Guessing game
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# This code prompts a hint and user has to guess the answer within 3 attempts

# Hint printed on screen to the user
print("Guess The animal name."
      "\nHINT: an animal in open jungle who loves to eat leafs on tree and has patches on skin"
      "\nYou have 3 guesses to win this game!\n")

# Initialised the variables
secret_word = "giraffe"     # The answer
guess = ""                  # Variable to store the user's input
guess_count = 0             # Variable to keep count of the number of attempts
guess_limit = 3             # Maximum guess limit
out_of_guesses = False      # Boolean value to keep track if the user id out of attempts

# Using while loop and if statement to process the game
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses, YOU LOSE!")
else:
    print("Right guess, YOU WIN!")
