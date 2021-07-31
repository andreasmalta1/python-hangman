# HANGMAN!!!
# Words are loaded into the words.py file which is a list of English worlds
# To play type a letter
# Program will inform you whether you guessed correctly, which letters you have already guessed and the lives left

import random
import string
from words import words


# Importing the list of words
def get_valid_word(words):
    # Choosing a word on random only if it does not contain spaces or hyphens '-'
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    # Returning an uppercase word
    return word.upper()


def hangman():
    word = get_valid_word(words)
    # Choosing the unique letters
    word_letters = set(word)
    # Alphabet is made of a set of characters from A to Z in uppercase
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # Game is played until there are no letters left to guess or there are no lives left
    while (len(word_letters) > 0) and (lives > 0):

        print("You have", lives, "lives left. You have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        # If letter has not been used remove it from alphabet and add it to used letter
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in word")
        # If letter has already been used
        elif user_letter in used_letters:
            print("You have already used that character")
        else:
            print("Invalid")

    if lives == 0:
        print(f"You died. the word was {word}")
    else:
        print(f"Congrats, you guessed {word}")


hangman()
