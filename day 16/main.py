# # import turtle
# # import prettytable

# # tony = turtle.Turtle()
# # my_screen = turtle.Screen()


# # def move_back():
# #     tony.back(10.0)


# # def move_forward():
# #     tony.forward(10.0)


# # def move_right():
# #     tony.right(10.0)


# # def move_left():
# #     tony.left(10.0)


# # my_screen.bgcolor("orange")
# # tony.shape("turtle")
# # tony.color("white")
# # my_screen.listen()
# # my_screen.onkeypress(move_back, "Down")
# # my_screen.onkeypress(move_right, "Right")
# # my_screen.onkeypress(move_left, "Left")
# # my_screen.onkeypress(move_forward, "Up")
# # my_screen.exitonclick()

# # print(tony)
# # print(my_screen)

# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Names", "", "c", "t")
# table.add_column("Age", "", "c", "t")
# table.add_column("Occupation", "", "c", "t")
# table.add_row(["Jack", "40", "programmer"])
# table.add_row(["RObert", "33", "System analist"])

# new_person = []

# new_person.append(input("Type the name"))
# new_person.append(input("Type the age"))
# new_person.append(input("Type the occupation"))

# table.add_row(new_person)

# table.align = "r"

# print(table.get_string(border=False, padding_width=5))
# print(table.get_string(sortby="Age"))

# # print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os


def clear_console():
    os.system('cls')


menu = Menu()
coffeeMaker = CoffeeMaker()
moneyProcessor = MoneyMachine()


def start_machine():
    clear_console()

    print(menu.get_items())

    while True:

        user_order = input("What would you like? (espresso/latte/cappuccino)")

        if user_order == "off":
            break
        if user_order == "report":
            coffeeMaker.report()
            continue

        order = menu.find_drink(user_order)
        if not order:
            continue

        if coffeeMaker.is_resource_sufficient(order) and moneyProcessor.make_payment(order.cost):
            coffeeMaker.make_coffee(order)


start_machine()
