#!/usr/bin/env python3

import random
import sys


name = input("What is your name? ")

print("Good Luck ! ", name)

words = [
    "en",
    "de",
    "het",
    "ik",
    "is",
    "dat",
    "niet",
    "van",
    "je",
    "te",
    "aan",
    "hij",
    "zij/ze",
    "er",
    "maar",
    "met",
    "voor",
    "als",
    "jij/u",
    "ben",
    "was",
    "we",
    "wat",
    "zijn",
    "in",
    "mij",
    "op",
    "heb",
    "mijn",
    "nog",
    "haar",
    "naar",
    "dan",
    "die",
    "dit",
    "zo",
    "kan",
    "heeft",
    "wel",
    "door",
    "over",
    "ze",
    "bij",
    "ook",
    "nee",
    "ja",
    "uit",
    "daar",
    "waar",
    "moet",
    "wil",
    "goed",
    "geen",
    "iets",
    "alles",
    "nu",
    "dus",
    "meer",
    "doen",
    "of",
    "omdat",
    "wie",
    "altijd",
    "tijd",
    "gaan",
    "hier",
    "heel",
    "veel",
    "zelf",
    "om",
    "daarom",
    "alleen",
    "komt",
    "bijna",
    "hoe",
    "mensen",
    "worden",
    "werken",
    "dag",
    "willen",
    "toch",
    "zien",
    "jaar",
    "daarvoor",
    "niets",
    "misschien",
    "geld",
    "leven",
    "land",
    "klaar",
    "waarom",
    "helpen",
    "ver",
    "andere",
    "nodig",
    "dank",
    "soms",
    "manier",
    "genoeg",
    "moeilijk",
]


def select_word(words):
    return random.choice(words)


remaining_attempts = 12
guessed_letters = ""
user_input = " "


def print_secret_word(secret_word, guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(" {} ".format(letter), end="")
        else:
            print(" _ ", end="")
    print("\n")


def is_guess_in_secret_word(guess, secret_word):
    if len(guess) > 1 or not guess.isalpha():
        print("Only single letters are allowed. Unable to continue...")
        sys.exit()
    else:
        if guess in secret_word:
            return True
        else:
            return False


secret_word = select_word(words)
print(" _ " * len(secret_word))


def get_unique_letters(word):
    return "".join(set(word))


while remaining_attempts > 0 and len(guessed_letters) < len(
    get_unique_letters(secret_word)
):
    guess = input("Guess a letter: ")
    guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)

    if guess_in_secret_word:
        if guess in user_input:
            print("You have already guessed the letter {}".format(guess))
        else:
            print("Yes! The letter {} is part of the secret word".format(guess))
            guessed_letters += guess
            user_input += guess
    else:
        if guess in user_input:
            print("You have already guessed the letter {}".format(guess))
        else:
            print("No! The letter {} is not part of the secret word".format(guess))
            remaining_attempts -= 1
            user_input += guess

    print(remaining_attempts)
    print("\n{} attempts remaining\n".format(remaining_attempts))
    print_secret_word(secret_word, guessed_letters)
    print("\n\nLetters guessed: {} \n".format((user_input)))

if len(guessed_letters) == len(get_unique_letters(secret_word)):
    print("+++ Well done, you have won this game! +++\n")
else:
    print("--- Sorry, you have lost this game! ---\n")
