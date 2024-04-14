from art import logo
import os
import random


def clear_console():
    os.system('cls')


def check_answer(guess, answer):
    if guess == answer:
        return True

    if guess > answer:
        print("too high...")
    else:
        print("Too low...")

    return False


def set_difficulty():
    difficulty = input("Choose the difficulty. 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        lives = 10
        print(
            f"You chosen the {difficulty} difficulty. So you will have {lives} lives")
    elif difficulty == 'hard':
        lives = 5
        print(
            f"You chosen the {difficulty} difficulty. So you will have {lives} lives")
    else:
        lives = 10
        print("Invalid input. You will have 10 lives.")

    return lives


def start_game():

    clear_console()
    print(logo)

    lives = set_difficulty()

    target_number = random.choice(range(1, 100))

    print("\nThe computer chosen a number. Now it's time to guess!\n")

    while lives > 0:
        user_guess = int(input("Choose a number."))

        if check_answer(user_guess, target_number):
            print(
                f"You guessed the number! Congratulations!\nYou won with {lives} lives remaining.\n")
            break
        else:
            lives -= 1
            if lives > 0:
                print(f"Wrong guess. You still have {lives} lives remaining\n")
            else:
                print("You ran out of lives. Try again...")


while input("Want to start a new game? type 'y' or 'n': ").lower() == 'y':
    start_game()
else:
    clear_console()
    print(logo)
    print("\nthanks for playing")
