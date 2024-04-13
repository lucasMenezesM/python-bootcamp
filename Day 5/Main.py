# ====================================== DAY 5 PYTHON ======================================
import random
# user_input = input("Write the heights: ")
# student_heights = user_input.split(" ")
# sum = 0
# amount_students = 0
# for student in student_heights:
#     value = int(student)
#     sum += value
#     amount_students += 1


# everage_result = sum // amount_students
# print(everage_result)

# input_scores = input("Type the scores: ")
# score_list = input_scores.split(" ")
# maximum_score = 0
# for score in score_list:
#     # if score == score[0]:
#     #     maximum_score = int(score)

#     if int(score) > maximum_score:
#         maximum_score = int(score)

# print(f"The highest score is: {maximum_score}")

# total = 0
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number

# for number in range(0, 101, 2):
#     total2 += number


# print(total)
# print(total2)

# for number in range(1, 101):
#     if (number % 3 == 0) and (number % 5 == 0):
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)

# -------------------------PASSWORD GENERATOR PROJECT DAY 5----------------------------
print("\n===========Welcome to the password generator===========\n")
# letters_numbers = int(
#     input("How manny latters do you want do add to the password?"))
# symbols_numbers = int(
#     input("How manny symbols do you want do add to the password?"))
# numbers_numbers = int(
#     input("How manny numbers do you want do add to the password?"))

# letters_options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
#                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers_options = [str(i) for i in range(1, 10)]
# symbols_options = ['#', '*', '@', '!', '?', '$']

# final_password = ''
# total_digits = letters_numbers + symbols_numbers + numbers_numbers

# for j in range(1, letters_numbers+1):
#     final_password += letters_options[random.randrange(
#         len(letters_options))]
# for j in range(1, numbers_numbers+1):
#     final_password += numbers_options[random.randrange(
#         len(numbers_options))]
# for j in range(1, symbols_numbers+1):
# final_password += symbols_options[random.randrange(
#     len(symbols_options))]
# for i in range(1, (total_digits+1)):
# actual_digit = random.randint(1, 3)
# if actual_digit == 1:
#     final_password += letters_options[random.randrange(
#         len(letters_options))]
# elif actual_digit == 2:
#     final_password += symbols_options[random.randrange(
#         len(symbols_options))]
# else:
#     final_password += numbers_options[random.randrange(
#         len(numbers_options))]




# final_password = []
# for i in range(1, (letters_numbers+1)):
#     # final_password += letters_options[random.randrange(len(letters_options))]
#     random_capital_letter = random.randint(1, 2)

#     if random_capital_letter == 1:
#         final_password.append(random.choice(letters_options).upper())
#     else:
#         final_password.append(random.choice(letters_options))

# for i in range(1, (numbers_numbers+1)):
#     # final_password += numbers_options[random.randrange(len(numbers_options))]
#     final_password.append(random.choice(numbers_options))

# for i in range(1, (symbols_numbers+1)):
#     # final_password += symbols_options[random.randrange(len(symbols_options))]
#     final_password.append(random.choice(symbols_options))

# random.shuffle(final_password)
# print("\nYour password result is:")
# for digit in final_password:
#     print(digit, end='')

#? JUST A TEST

letters_options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_options = [str(i) for i in range(1, 10)]
symbols_options = ['#', '*', '@', '!', '?', '$']

print("Welcome to the password generator!")

number_quantity = int(input("How many numbers do you want? "))
letters_quantity = int(input("How many letters do you want? "))
symbols_quantity = int(input("How many symbols do you want?"))

# total_length = number_quantity + letters_quantity + symbols_quantity
final_password = ''

for letter in range(number_quantity):
    final_password += str(random.choice(numbers_options))+ " "

for letter in range(letters_quantity):
    final_password += random.choice(letters_options)+ " "

for letter in range(symbols_quantity):
    final_password += random.choice(symbols_options)+ " "

final_result = final_password.split();
random.shuffle(final_result)

print(final_password)
for letter in range(1, len(final_result)):
    print(final_result[letter], end="")