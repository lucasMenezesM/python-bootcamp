# ==================================DAY 8 PYTHON==================================
import functions

# functions.greet("Python")
# # functions.greet_with("Someone", "Brazil")
# functions.greet_with(location="Brazil", name="Someone")
# todo ****************PAINT WALL***************
# wall_coverage = 5
# wall_width = int(input("What is the width of the wall?"))
# wall_wight = int(input("What is the height of the wall?"))

# numbers_of_can = functions.calc_paint(
#     width=wall_width, height=wall_wight, coverage=wall_coverage)

# print(
#     f"You will need to buy {numbers_of_can} cans of paint to paint the wall!")

# todo **********PRIME NUMBER**************
# number_chosen = int(input("Type a number: "))

# is_prime_number = functions.prime_number(n=number_chosen)

# print(is_prime_number)

# todo **********DAY 8 PROJECT - ENCRYPT MESSAGE**************
import art

loop_execution = True
while loop_execution:
    print(art.logo)

    direction = input("Do you want to encode ou decode?").lower()

    if direction == "encode" or direction == "decode":
        # ? mjqqt
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift you want: "))

        functions.caeser(text=text, shift=shift, direction=direction)
    else:
        print(f"'{direction}' is not a valid input. Try again")

    loop = input("Do yout want to go again? | yes or no | ").lower()
    if loop == "no":
        loop_execution = False
else:
    print("\nThank you for using")
