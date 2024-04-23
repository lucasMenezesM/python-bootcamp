# # list = [5, 6, 1, 2, 4, 5]

# # new_list = [number+1 for number in list]
# # # print(new_list)

# # name = "lucas"

# # # new_list = [letter.upper() for letter in name]
# # # print(new_list)

# # new_list = [number * 2 for number in range(1, 5)]
# # print(new_list)

# import random

# names = ["jack", "Gus", "walter", "Jessie", "Walter Jr"]
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)

# passed_students = {student: score for (student, score) in students_score.items() if score >= 60}

# print(passed_students)

import pandas

# TODO 1. Create a dictionary in this format:

data = pandas.read_csv("Day 26/nato_phonetic_alphabet.csv")

alphabetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}

# for (index, row) in data.iterrows():
#     alphabetic_dic[row.letter] = row.code

# print(alphabetic_dic)luca

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_name = input("Type your name: ").upper()

result = [alphabetic_dic[letter] for letter in user_name]

    
print(result)