import random
import dataBase
import functions


def start_game():
    functions.print_logo()

    user_score = 0
    random_celebrity_A = random.choice(dataBase.data)

    while True:

        random_celebrity_B = random.choice(dataBase.data)
        while random_celebrity_A == random_celebrity_B:
            random_celebrity_B = random.choice(dataBase.data)

        functions.print_celebrities(random_celebrity_A, random_celebrity_B)

        user_answer = input(
            "Who has more followers? Type 'A' or 'B': ").lower()
        right_answer = functions.compare(
            random_celebrity_A, random_celebrity_B)

        if functions.check_answer(user_answer, right_answer):
            if user_answer == 'b':
                random_celebrity_A = random_celebrity_B
            user_score += 1
            print(f"You're right! Current score: {user_score}.\n")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            break


while input("Do your want to start a new game? 'y' or 'n'").lower() == 'y':
    start_game()
