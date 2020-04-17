'''
Project: Hangman
Author: Ari24
'''

import random


# helper functions
def find_every_char_of_string(char, string):
    indexes = []

    for i, letter in enumerate(list(string)):
        if char == letter:
            indexes.append(i)

    return indexes

def list_to_word(char_sequence):
    return ''.join(char_sequence)

def format_list(_list):
    return list_to_word(_list).replace(" ", "_ ")

# Main Code

words = ["banana", "apple", "juice", "german"]
word_to_guess = random.choice(words)
right_letters = []

tries = 6

for letter in word_to_guess:
    right_letters.append(" ")

print("The word has " + str(len(right_letters)) + " chars!")

# Main Loop
game = True
while game:
    user_input = input("\nEnter char/word: ")

    if user_input.lower() in word_to_guess:
        for letter in user_input:
            indexes = find_every_char_of_string(letter, word_to_guess)

            for index in indexes:
                right_letters[index] = letter

            print("Right!")
            print(format_list(right_letters))

        if list_to_word(right_letters).lower() == word_to_guess.lower():
            print("Nice, u won!")
            game = False
    else:
        if tries <= 0:
            print("Bad, u havent guessed the word!")
            game = False
            break
        else:
            tries -= 1
            print(f"Sorry, wrong char/word.\nTries left: {tries}")









