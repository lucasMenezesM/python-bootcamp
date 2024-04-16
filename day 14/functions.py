import art
import os


def clear_console():
    os.system('cls')


def print_logo():
    clear_console()
    print(art.logo)


def print_celebrities(person_a, person_b):
    print(
        f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(art.vs)
    print(
        f"Compare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.\n")


def compare(person_a, person_b):
    right_answer = ""
    if person_a['follower_count'] > person_b['follower_count']:
        right_answer = 'a'
    else:
        right_answer = 'b'

    return right_answer


def check_answer(user_answer, right_answer):
    print_logo()
    if user_answer == right_answer:
        return True

    else:
        return False
