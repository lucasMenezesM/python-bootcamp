from art import logo
import os
from operators import execute_operation, operations


def format_name(f_name, l_name):
    return f"{f_name} {l_name}".title()

# # print(format_name("LUCas", "mENEzeS"))

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
# # TODO: Add more code here 👇

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(year):
#     month_days[1] += 1

#   return month_days[month - 1]

# #🚨 Do NOT change any of the code below
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)

# ? ====================== CALCULATOR PROGRAM ======================


def clear_terminal():
    os.system('cls')


def print_operators():
    for operator in operations:
        print(operator)

# calculation_function = operations[chosen_operator]
# result = calculation_function(chosen_number, chosen_number2)

# # result = int(execute_operation(chosen_number, chosen_number2, chosen_operator))

# print(f"Result: {chosen_number} {chosen_operator} {chosen_number2} = {result}")

# should_continue = input(
#     "Whant to make another operation? 'yes' or 'no'").lower()

# if should_continue == 'no':
#     loop_repetition = False


def calculator():
    clear_terminal()
    print(logo)
    chosen_number = float(input("What's the first number? "))

    loop_repetition = True
    while loop_repetition:
        print_operators()
        chosen_operator = input("What's the operator? ")

        next_number = float(input("What's the next number? "))

        # ? possible ways to get a result

        # # ? Using the dictionary
        # calculation_function = operations[chosen_operator]
        # result = calculation_function(chosen_number, next_number)

        # # ? Using the execute_operation function from the other file
        result = (execute_operation(
            chosen_number, next_number, chosen_operator))

        print(
            f"Result: {chosen_number} {chosen_operator} {next_number} = {result}")

        if input(f"Whant to make another operation with {result}? 'yes' or 'no': ").lower() == 'no':
            loop_repetition = False
            calculator()
        else:
            chosen_number = result


calculator()

clear_terminal()
print(logo)
print("\nProgram finished.\n")
