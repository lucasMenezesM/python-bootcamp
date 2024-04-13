# ====================================== DAY 3 PYTHON ======================================
number = int(input("Write a number: "))
if number % 2 == 0:
    print(f"Your number ({number}) is even")
else:
    print(f"the number you typed ({number}) is odd")

# -------BMI CALCULATOR 2.0------------
height = float(input("Write your height "))
weight = int(input("Write your weight "))
bmi_result = weight/height**2
print(round(bmi_result, 2))  # rounded to two decimals
print(int(bmi_result))  # printed the result as a whole number
# Division was made directly to a integer using the // operator
print(weight // height ** 2)
# print(f"your BMI reuslt is {round(bmi_result, 2)}")

if bmi_result < 18.5:
    print(f"Your BMI is {bmi_result} and you are underweight")
elif bmi_result < 25:
    print(f"Your BMI is {bmi_result} and you have a normal weight")
elif bmi_result < 30:
    print(f"Your BMI is {bmi_result} and you are overwight")
elif bmi_result < 35:
    print(f"Your BMI is {bmi_result} and you are obese")
else:
    print(f"Your BMI is {bmi_result} and you are clinically obese")

# ---------LEAP YEAR--------------
year = int(input("Type a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
    print("This is a leap year!")
else:
    print("This is not a leap year")


# -------ORDERING PIZZA------------
print("Welcome to python pizza\n")

pizza_ordered = input("What size do you want? ")
wants_pepperoni = input("Do you want some Pepperoni? ")
cheese = input("Do you want extra cheese? ")
bill = 0

if cheese == "y":
    bill += 1

if pizza_ordered == "s":
    bill += 15

    if wants_pepperoni == "y":
        bill += 2

elif pizza_ordered == "m":
    bill += 20

    if wants_pepperoni == "y":
        bill += 3

elif pizza_ordered == "l":
    bill += 25

    if wants_pepperoni == "y":
        bill += 3
else:
    print("type a valid value in the field")

print(f"The final Value of your order is ${bill}")

# ----------letters---------------
first_name = input("Type the first name: ")
second_name = input("Type the second name: ")

combined_names = first_name.lower() + second_name.lower()
true_combined = 0
true_combined += combined_names.count("t")
true_combined += combined_names.count("r")
true_combined += combined_names.count("u")
true_combined += combined_names.count("e")

love_combined = 0
love_combined += combined_names.count("l")
love_combined += combined_names.count("o")
love_combined += combined_names.count("v")
love_combined += combined_names.count("e")

final_result = str(true_combined) + str(love_combined)

if int(final_result) < 10 and int(final_result) > 90:
    print(f"your score is {final_result} | You both are like coke and mentos")
elif int(final_result) > 40 and int(final_result) < 50:
    print(f"your score is {final_result} | You both are ok together")
else:
    print(f"Your score is {final_result}")


# --------PROJECT DAY 3 | TREASURE ISLAND ----------------
print(
    '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
print("\nWelcome to Treasure Island. \nYour Mission is to find the treasure!")
chosen_option = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right'")
if chosen_option.lower() == "r":
    print("\nFall into a hole. \nGame over.")
elif chosen_option.lower() == "l":

    chosen_option = input("Swim or wait? ")

    if chosen_option.lower() == "s":
        print("\nAttacked by trout. \nGame Over.")

    elif chosen_option.lower() == "w":
        chosen_option = input("Which door? red, blue or yellow?")

        if chosen_option.lower() == "r":
            print("\nBurned by fire. \nGamer Over")
        elif chosen_option.lower() == "b":
            print("\nEaten by beasts. \nGame Over.")
        elif chosen_option.lower() == "y":
            print("You win!")

        else:
            print("Gamer Over")
    else:
        print("\nGame Over!")
else:
    print("Gamer Over.")
