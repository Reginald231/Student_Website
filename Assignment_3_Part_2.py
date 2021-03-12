"""
Reginald Long
CS4308 - Internet Programming
Assignment 3 Part 2:
The Word Guesser
"""

import random
import time

win = False

#Note: You need to download the words.txt file from my webpage and store it in the same directory to run this program!
with open("words.txt") as f:
    word_list = f.read().splitlines()

millis = int(round(time.time() * 1000))
random.seed(millis)

word_index = random.randint(0, len(word_list)-1)

progress = "_" * len(word_list[word_index])


def guess_letter(my_letter):
    p = list(progress)
    new_progress = ""
    word = list(word_list[word_index])
    for idx, val in enumerate(word):
        if my_letter == val:
            p[idx] = val

    for char in p:
        new_progress += char

    if p.count("_") == 0:
        print(f'Congratulations! You guessed the word correctly!\nThe word was "{word_list[word_index]}".')
        exit(0)

    return new_progress


while win is not True:
    print("\nThis is your current progress on the word: " + progress)
    my_letter = input("Enter a letter to guess for the hidden word: ")
    progress = guess_letter(my_letter)



