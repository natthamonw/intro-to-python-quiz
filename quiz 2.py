import sys

def levelinput():
    # levelinput() doesn't take any direct input but within the function solicits a
    # user input to determine which level the player would like to select
    # Reference: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    print "\x1b[6;30;42m" + """
Welcome to Python Quiz!""" + "\x1b[0m"
    level_input = raw_input("""
Please select your level ( easy | medium | hard ): """)
    if level_input == "easy":
        correct_incorrect(easy_questions, easy_answers)
    if level_input == "medium":
        correct_incorrect(medium_questions, medium_answers)
    if level_input == "hard":
        correct_incorrect(hard_questions, hard_answers)

def playagain():
    # playagain() takes any direct input but within the function solicits a user input
    # to determine whether the player would like to play the game again
    play_again = raw_input("""
Would you like to play again? ( Y | N ): """)
    if play_again == "Y":
        levelinput()
    if play_again == "N":
        # Reference: http://www.hashbangcode.com/blog/stopping-code-execution-python
        sys.exit("""
""" + "\x1b[6;30;42m" + "Gotcha. Thanks for stopping by!" + "\x1b[0m" + """
""")

def replaced_sentence(question, answer):
    # replaced_sentence() takes two inputs and replace the blank ("______") in the
    # first input and replace it with the second input. It then prints the replaced
    # sentence
    blank = "______"
    whole_sentence_answer = question.replace(blank, answer)
    question_end_index = whole_sentence_answer.find("Your answer: ")
    print "\x1b[6;30;42m" + """
""" + str(whole_sentence_answer[:question_end_index])+ "\x1b[0m"

def correct_incorrect(set_of_questions, set_of_answers):
    # correct_incorrect() takes two inputs: a list of questions and a list of answers.
    # The function then solicits two types of user input. One is the number of guesses
    # the player wants in this particular round. The other is the player's answer to
    # each question in the list. The function then determines whether the latter
    # user input corresponds with the correct answer. If the player guesses
    # correctly, she proceeds to the next question until exhausting all the questions
    # in that particular list, upon which she will be asked whether she wants to play
    # the game again. When guessing in incorrectly, the player is prompted to try
    # again and given the number of guesses left in the currect round until she exhausts
    # the number of guesses stipulated at the beginning of the game, upon which she
    # will be prompted to decide whether to play the game again.
    guess_number_input = raw_input("""
How many guesses would you like to have in this particular round?: """)
    count = 0
    index = 0
    while count <= int(guess_number_input):
        user_input = raw_input(set_of_questions[index])
        # If correct, the player proceeds to the next question
        if user_input == str(set_of_answers[index]):
            replaced_sentence(set_of_questions[index], set_of_answers[index])
            if index < len(set_of_questions):
                index += 1
            # Once the player answers all the questions in the current level correctly, they are asked if they want to play again
            if index == len(set_of_questions):
                print "\x1b[6;30;42m" + """
Congrats, you totally breezed through this level!""" + "\x1b[0m"
                playagain()
        else:
            count += 1
            # When running out of guesses, the player is asked if she wants to play the game again
            if int(guess_number_input) - count == 0:
                print "\x1b[6;30;41m" + """
No more guesses. You lose :-(""" + "\x1b[0m"
                playagain()
            else:
                # If guessed incorrectly, the player is informed of the number of guesses left and prompted to try again
                print "\x1b[6;30;41m" + """
Your answer is incorrect. Please try again. The number of guesses left is """ + str(int(guess_number_input) - count) + "." + "\x1b[0m"

# All questions in easy
easy_questions = ["""
The command ______ is used to display an absolute path to where one currently is in the computer's file structure system.
Your answer: """,
"""
To see all contents in a directory, we use the command ______.
Your answer: """,
"""
The equality comparison is done using ______.
Your answer: """,
"""
The ______ statement allows us to stop the loop even while the test condition is true.
Your answer: """,
"""
When it comes to debugging, the ______ line of python tracebacks will tell you what went wrong. Starting from there will tell you more about where the problem occurred.
Your answer: """]

# All answers in easy
easy_answers = ["pwd", "ls", "==", "break", "last"]

# All questions in medium
medium_questions = ["""
Take a look at the code below:

def say_hello(name)
    greeting = "Hello " + name + "!"
    return greeting

______ is missing so the Python code will not work properly.
Your answer: """,
"""
If you want your function to produce output, it must end with a ______ statement.
Your answer: """,
"""
To display the results of a function call, it is important to include a ______ command.
Your answer: """,
"""
time = 60
time = time - 45
time = time * 2
The value of the variable time after running this code is ______.
Your answer: """,
"""
Given that name = "Paul Revere", the value of name[4:8] is ______.
Your answer: """]

# All answers in medium
medium_answers = [":", "return", "print", "30", " Rev"]

# All questions in hard
hard_questions = ["""
A. "python'
B. '"python'
C. "python"'
D. python

______ is a valid string in Python.
Your answer ( A | B | C | D ): """,
"""
Given that:

string -- is the string whose substring needs to be replaced by a new substring
old -- is the old substring to be replaced
new -- is the new substring that would replace the old substring

______ is the valid syntax of the replace() method.
*Do not include any space in your answer.
Your answer: """,
"""
A ______ is a multi-line string that acts as a descriptive comment for a function, but it is retained by the computer as the code executes and can be accessed by users as the code runs.
Your answer: """,
"""
______ is a result of following code:

print range(0, 5)

*Do not include any space in your answer.
Your answer: """
]

# All questions in hard
hard_answers = ["B", "string.replace(old,new)", "docstring", "[1,2,3,4]"]

levelinput()
