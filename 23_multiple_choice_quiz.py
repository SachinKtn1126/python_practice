# Title:                            Multiple Choice Question game
# Author:                           Sachin Kotian
# Created date (DD-MM-YYYY):        08-12-2018
# Last modified date (DD-MM-YYYY):  08-12-2018
#
# ABOUT:
# This code prompts a question and takes user input as answer.
# In the end it shows the score
# Please refer to "Question.py" to see the class and the method

# Import the question class from Question
from Question import question

# Stor the questions in a list
question_prompt = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "What color are cherries?\n(a) Yellow\n(b) Red\n(c) Blue\n",
]

# initialising the list with class question
questions = [
    question(question_prompt[0],"a"),
    question(question_prompt[1],"c"),
    question(question_prompt[2],"b")
]

# Defining a funtion to run the test when called
def run_test(questions):
    score = 0                                                      # Set the score as 0
    for question in questions:                                     # For every question in the question list
        answer = input(question.prompt + "\nanswer: ")             # Get input from the user for each question as answer
        if answer == question.answer:                              # IF user's answer == the stored answer
            score +=1                                              # Score increments by 1
    print("Ypu get" + str(score) + "/" + str(len(questions)))      # At the end of the for loop print the score

# Call the function to run the test
run_test(questions)