# ====================================== DAY 4 PYTHON ======================================
import random
print('''
__-----__
      ..;;;--'~~~`--;;;..
    /;-~IN GOD WE TRUST~-.\
   //      ,;;;;;;;;      \\
 .//      ;;;;;    \       \\
 ||       ;;;;(   /.|       ||
 ||       ;;;;;;;   _\      ||
 ||       ';;  ;;;;=        ||
 ||LIBERTY | ''\;;;;;;      ||
  \\     ,| '\  '|><| 1995 //
   \\   |     |      \  A //
    `;.,|.    |      '\.-'/
      ~~;;;,._|___.,-;;;~'
          ''=--'
''')
print("\nWelcome to the coin toss")

random_value = random.randint(0, 1)
if random_value == 1:
    print("Head")
else:
    print("Tails")


# -------------who's gonna pay the meal?------------------
names = input("Type the names... ")
names_list = names.split(", ")
# final_result = random.randint(0, len(names_list) - 1)
# payer = names_list[final_result]
payer = random.choice(names_list)
print(f"{payer} will pay the meal today!")

fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0][3])

# # # # ---------------treasure map -----------------------------

dificulty = int(
    input("Choose the dificulty:\n1- easy (3x3) \n2- medium (4x4) \n3- hard (5x5)\n..."))


attempts = 0
while True:
    attempts += 1
    print("\n===========Welcome to the treasure hunt!===========\n")

    if dificulty == 1:
        row1 = ["⬜", "⬜", "⬜"]
        row2 = ["⬜", "⬜", "⬜"]
        row3 = ["⬜", "⬜", "⬜"]
        map = [row1, row2, row3]

    elif dificulty == 2:
        row1 = ["⬜", "⬜", "⬜", "⬜"]
        row2 = ["⬜", "⬜", "⬜", "⬜"]
        row3 = ["⬜", "⬜", "⬜", "⬜"]
        row4 = ["⬜", "⬜", "⬜", "⬜"]
        map = [row1, row2, row3, row4]

    elif dificulty == 3:
        row1 = ["⬜", "⬜", "⬜", "⬜", "⬜"]
        row2 = ["⬜", "⬜", "⬜", "⬜", "⬜"]
        row3 = ["⬜", "⬜", "⬜", "⬜", "⬜"]
        row4 = ["⬜", "⬜", "⬜", "⬜", "⬜"]
        row5 = ["⬜", "⬜", "⬜", "⬜", "⬜"]
        map = [row1, row2, row3, row4, row5]

    random_line = random.randint(0, len(row1) - 1)
    random_column = random.randint(0, len(row1) - 1)

    chosen_location = input("Where do your want to dig? ")

    chosen_line = int(chosen_location[0]) - 1
    chosen_column = int(chosen_location[1]) - 1

    if random_line == chosen_line and random_column == chosen_column:
        print("\nCongratulations! You earned the treasure!")
        if attempts == 1:
            print("You succeded in your first attempt! How did you do that?")
        else:
            print(f"Total attempts: {attempts}")

        attempts = 0
        map[chosen_line][chosen_column] = "❎"
    else:
        print("\nYou missed the spot! Keep trying")
        map[chosen_line][chosen_column] = "❌"
        map[random_line][random_column] = "✔️"

    if dificulty == 1:
        print(f"{row1}\n{row2}\n{row3}")
    elif dificulty == 2:
        print(f"{row1}\n{row2}\n{row3}\n{row4}")
    elif dificulty == 3:
        print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}")

    print("\nDescription:\n✔️ : Right spot | ❌ : Missed attempt | ❎ : Right attempt")

    play_again = input("\n Do you want to play again? N or Y: ")
    if play_again.lower() == "n":
        break


print("\nThanks for playing!")


# # # # # # -----------------------------project day 4--------------------------------
papper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
player_choice = int(
    input("Make your choice:\n1- Rock \n2- Scissors \n3- Papper\n..."))

computer_choice = random.randint(1, 3)
print("Computer play: ")
if player_choice > 3:
    print("The computer said it was so easy he didn't even try!")
else:
    if computer_choice == 1:
        print(rock)
    elif computer_choice == 2:
        print(scissors)
    else:
        print(papper)


print("Your play:")
if player_choice == 1:
    print(rock)
elif player_choice == 2:
    print(scissors)
elif player_choice == 3:
    print(papper)
else:
    print("invalid input")


def defineWinner(player, computer):
    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print(f"you Won!")
    elif player == computer:
        print(f"It was a draw")
    else:
        if player > 3:
            print("\nYou choose an invalid number")
        print("You loose")


defineWinner(player_choice, computer_choice)
