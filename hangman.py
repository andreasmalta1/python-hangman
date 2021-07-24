import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while (len(word_letters) > 0) and (lives > 0):

        print("You have", lives, "lives left. You have used these letter: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in word")
        elif user_letter in used_letters:
            print("You have already used that character")
        else:
            print("Invalid")

    if lives == 0:
        print(f"You died. the word was {word}")
    else:
        print(f"Congrats, you guessed {word}")


hangman()
