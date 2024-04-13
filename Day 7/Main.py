# ====================================== DAY 7 PYTHON ======================================



# random_word = random.choice(dataBase.word_list)
# display = []
# lives = 6

# print(random_word)
# print(figures.logo)

# for i in random_word:
#     display.append("_")

# print(display)

# while "_" in display:
#     user_guess = input("\nTry a letter: ").lower()
#     clear_terminal()

#     if user_guess in display:
#         print(f"\nThe letter {user_guess} was already guessed!")

#     for i in range(len(random_word)):
#         if random_word[i] == user_guess:
#             display[i] = random_word[i]

#     print(display)

#     if not user_guess in random_word:
#         lives -= 1
#         print(f"\nThe letter {user_guess} is not in the word. You lost a life")

#     print(figures.stages[lives])

#     if lives < 1:
#         print("You lost the game...")
#         break
# else:
#     print("You won the game!")
# print("\nThank you for playing")
# print(figures.logo)

import random
import dataBase
import figures
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_display():
    print(display)

target_word = random.choice(dataBase.word_list)
print("Target word: "+ target_word)

display = []
for letter in target_word:
    display.append("_")

game = True
player_lives = 5
attempts = 0
while game:
    
    print("Target word: "+ target_word)

    if player_lives == 0:
        print(f"You lost the game with {attempts}")
        break

    print_display()

    player_guess = input("Choose a letter: ").lower()
    attempts += 1
    clear_terminal()

    if player_guess not in target_word:
        player_lives -= 1
        if player_lives > 0:
            print(f"Wrong answer! You still have {player_lives} lives remaning.")
        continue

    print("You get the rigth answer!")

    for i in range(0, len(target_word)):
        if player_guess == target_word[i]:
            display[i] = player_guess
    
    if "_" not in display:
        print(f"You won the game! Total attempts: {attempts}")
        break