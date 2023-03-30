import random
import requests
from art import *

# Declare variable
lives = 6
url = "https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json"
display = []
word_list= []
game_is_finish = False

json_word = requests.get(url).json()

for word in json_word.keys():
    word_list.append(word)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)

# print(f'Pssst, the solution is {chosen_word}.')

# Cycle for to do display list
for i in range(word_length):
    display.append("_")

# Cycle "while" condition to exit "game_is_finish" is True
while not game_is_finish:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"The letter '{guess}' is guess ready!")

    # Cycle to read position
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            no_letter = True

    # "if" condition to check the letter guess in choseword
    if guess not in chosen_word:
        print(f"The letter '{guess}' is not in word!")
        lives -= 1
        if lives == 0:
            game_is_finish = True
            print(f"The word was '{chosen_word}'")
            print("You Lose!")

    print(f"{' '.join(display)}")

    # "if" condition to check if we found all guess letter
    if "_" not in display:
        game_is_finish = True
        print("You win.")

    print(stages[lives])
