# ===================== Black Jack Project ============================
import random
import os
from art import logo


def clear_terminal():
    """Clear the console"""
    os.system('cls')


def sumCards(cards):
    total = sum(cards)

    if total == 21 and len(cards) == 2:
        return 0

    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)

    return total


def addCard(cards, options):
    card = random.choice(options)
    cards.append(card)
    options.remove(card)


def verifyWinner(user_cards, computer_cards):

    userWon = False

    total_user_cards = sumCards(user_cards)
    total_computer_cards = sumCards(computer_cards)

    if total_computer_cards == 0:
        print("BlackJack by computer")
        return

    if total_user_cards == 0:
        print("BlackJack by user")
        return

    if total_computer_cards > 21:
        userWon = True

    if total_user_cards > total_computer_cards and total_user_cards < 21:
        userWon = True

    if total_user_cards == total_computer_cards or (total_user_cards > 21 and total_computer_cards > 21):
        print("\nDraw!")
    elif userWon:
        print("\nYou Won the game!")
    else:
        print("\nYou lost the game!")

    print(f"Your Cards: {user_cards} = {total_user_cards}")
    print(f"Computer cards: {computer_cards} = {total_computer_cards}")


def blackJack():
    """Initiates the blackJack Game"""

    available_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    clear_terminal()
    print(logo)

    user_cards = []
    computer_cards = []

    while True:

        addCard(user_cards, available_cards)
        addCard(computer_cards, available_cards)

        if sumCards(user_cards) == 0 or sumCards(computer_cards) == 0:
            break

        if sumCards(user_cards) > 21 or sumCards(computer_cards) > 21:
            break

        print(f"Your Cards: {user_cards} = {sumCards(user_cards)}")
        print(f"Computer Cards: [{computer_cards[0]},...]")

        if input("do you want to hit or pass? ") == "hit":
            continue
        else:
            break

    verifyWinner(user_cards, computer_cards)

    if input("Do you want to play again? type 'y' or 'n': ").lower() == 'y':
        blackJack()


blackJack()
