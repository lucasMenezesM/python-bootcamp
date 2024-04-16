from dataBase import resources, MENU
import os


def clear_console():
    """Clear the Terminal when executes."""
    os.system('cls')


def check_resources(user_order):
    """Check if the item ordered by the user is available. Returns True if it's or False if it's not."""

    order = MENU[user_order]
    order_ingredients = order['ingredients']

    print(f"{user_order} selected. | Cost: ${order['cost']}\n")

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            return False

    return True


def insert_coins():
    """Collect the coins from the user and returns the total"""

    quarters_qty = int(input("How much quarters? "))
    dimes_qty = int(input("How much dimes? "))
    nickles_qty = int(input("How much nickles? "))
    pennies_qty = int(input("How much pennies? "))

    total = (quarters_qty * 0.25) + (dimes_qty * 0.1) + \
        (nickles_qty * 0.05) + (pennies_qty * 0.01)

    return total


def process_payment(user_order, payment):
    """Takes the order and the total paid to process the payment. Returns True if the payment was successfull made or False if it fails."""

    order = MENU[user_order]
    cost = order['cost']

    print(f"\nTotal cost: {cost} | Total payment: {round(payment, 2)}")

    if payment < cost:
        print("Sorry that's not enough money. Money refunded\n")
        return False

    if payment > cost:
        # change = round()
        print(f"Here is ${round(payment - cost, 2)} dollars in change.\n")

    resources['money'] += cost
    return True


def make_coffee(user_order):
    """Prepare the order."""
    # TODO function to make the coffee

    print("Preparing order...")
    order = MENU[user_order]
    order_ingredients = order['ingredients']

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"\nHere is your {user_order}. Enjoy!")


def show_machine_details(option):
    if option == "menu":
        print("HERE'S THE MENU:")
        for item in MENU:
            print(f"{item} - ${MENU[item]['cost']}")
        print("")

    elif option == "report":
        print(f"Coffee: {resources['coffee']}g")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: ${resources['money']}\n")
