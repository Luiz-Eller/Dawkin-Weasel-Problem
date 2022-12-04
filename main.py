"""
Dawkins’ Weasel Program
Activity 001 - Class of LPC 2022/2 - UEA/EST
Author: Luiz Eduardo Eller
Last Modified on: 01/12/2022
"""


import random

# Declare Constants
USE_DEFAULT_MESSAGE = True
LETTER_MUTATION_PERCENTAGE = 5
NUMBER_OF_CLONES = 100


# Generates and returns a character that can be any
# lower or uppercase letters or an empty space
# checks to see if the char is not the excluded_char
def random_char(excluded_char=''):
    char = excluded_char
    while char == excluded_char:
        offset = random.randrange(0, 53)
        if offset == 0:
            char = ' '

        elif 0 < offset <= 26:
            # Returns a uppercase letter
            char = chr(65 + offset - 1)

        else:
            # Returns a lowercase letter
            char = chr(97 + offset - 27)
    return char


def give_score(desired_string, current_string):
    # Returns the number of letter that match
    # (same letter and position) between two strings
    # Is case-sensitive
    score = 0
    goal = list(desired_string)
    current = list(current_string)
    for ite in range(len(goal)):
        if goal[ite] == current[ite]:
            score += 1
    return score


def mutate_string(text):
    # Returns a new string with a chance of some characters
    # to swapped with a new random one
    mutated_text = list(text)
    for ite in range(len(mutated_text)):
        if random.randint(0, 100) < LETTER_MUTATION_PERCENTAGE:
            mutated_text[ite] = random_char(mutated_text[ite])
    return "".join(mutated_text)


# Initializes variables
matriz_string = []
highest_score = 0
highest_score_position = 0
generation = 0

if USE_DEFAULT_MESSAGE:
    desired_message = "METHINKS IT IS LIKE A WEASEL"
else:
    desired_message = input()
message_length = len(desired_message)

for i in range(NUMBER_OF_CLONES):
    # Initializes the strings, all with random characters
    # Only creates strings of the same length as the desired_message
    temp_string = ''
    for j in range(message_length):
        temp_string += random_char()
    matriz_string.append(temp_string)

while highest_score < message_length:
    # Creates n clones of the message that got the closest to the
    # desired_message, has a chance to mutate any letter of the clones
    # Repeats this process until a string matchs all the letters
    # of the desired_message
    highest_score = 0
    for i in range(NUMBER_OF_CLONES):
        # Checks the highest score, if tied chooses the first one to appear
        temp_score = give_score(desired_message, matriz_string[i])
        if temp_score > highest_score:
            highest_score_position = i
            highest_score = temp_score
    winner_string = matriz_string[highest_score_position]
    
    print(f"Winner of generation {generation}: {winner_string}"
          f" Score: {highest_score}")

    for i in range(NUMBER_OF_CLONES):
        matriz_string[i] = mutate_string(winner_string)
    generation += 1
