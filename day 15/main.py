from functions import check_resources, clear_console, process_payment, make_coffee, insert_coins, show_machine_details
import art


def turn_on_coffee_machine():
    clear_console()
    print(art.logo1)

    show_machine_details("menu")

    while True:

        order = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()

        if order == "off":
            print("Machine Turned Off.")
            break

        if order == "report":
            show_machine_details("report")
            continue

        if order != "espresso" and order != "latte" and order != "cappuccino":
            continue

        if not check_resources(order):
            print("Not enough resources.")
            continue

        payment = insert_coins()

        if not process_payment(order, payment):
            continue

        make_coffee(order)


turn_on_coffee_machine()
