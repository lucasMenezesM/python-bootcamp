# students_scores = {
#     "harry": 81,
#     "ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }

# def grade_definer(score):
#     if score > 90:
#         return "Outstanding"
#     elif score > 80:
#         return "Exceeds Expecations!"
#     elif score > 70:
#         return "Acceptable"
#     else:
#         return "fail"

# students_grades = {}

# for student in students_scores:
#     name = student
#     score = students_scores[student]

#     students_grades[name] = grade_definer(score)

# # print(students_grades)


# #? ======================= TRAVEL LOG EXERCISE ===============================

# travel_log = {
#     "france": [
#         {"city": "Paris", "visits": 4}, 
#         {"city": "Dijon", "visits": 2}
#     ],
#     "Brazil": [
#         {"city": "Rio de Janeiro", "visits": 1},
#         {"city": "Sao Paulo", "visits": 2},
#     ]
# }

# travel_log2 = [
#     {
#         "country": "france",
#         "visited_cities": ["Paris", "Dijon"],
#         "total visits": 3
#     },
#     {
#         "country": "brazil",
#         "visited_cities": ["Sao Paulo", "Rio de Janeiro"],
#         "total visits": 2
#     }
# ]

# def add_country(country_name, visited_cities, total_visits):
#     new_country = {
#         "country": country_name,
#         "visited_cities": visited_cities,
#         "total_visits": total_visits
#     }

#     travel_log2.append(new_country)

# user_country = input("Type the country name: ")

# user_cities = []
# loop = True

# while loop:
#     user_cities.append(input("Type a city that you visited: "))
#     another_city = input("Do you have another city? Type with 'yes' or 'no'").lower()
#     if another_city == 'no':
#         loop = False

# total_visits = input("How much visits did you do?")

# add_country(user_country, user_cities, total_visits)

# print("Visited citys:")

# #for country in travel_log:
#  #   for city in travel_log[country]:
#   #      print(city["city"], end=", ")

# for country in travel_log2:
#     print(country["visited_cities"]);


# print(f"I visited {travel_log2[2]['country']} {travel_log2[2]['total_visits']} times. And my favorite city was {travel_log2[2]['visited_cities'][1]}")

#? ====================== AUCTION PROGRAM ==========================

import os
import art

def clear_terminal():
    os.system('cls')

clear_terminal()
print(art.logo)
print("Welcome to the Auction Program!")

auction_participants = []

def define_winner(auction_list):
    highest_value = 0
    winner = {}

    for person in auction_list:
        if person["bid"] > highest_value:
            winner = person
    
    return winner

active = True

while active:
    name = input("Type your name: ")
    bid = int(input("Type your bid: $"))

    auction_participants.append({"name": name, "bid": bid})

    repeat = input("Is there another person to include in the auction? type 'yes' or 'no': ")
    clear_terminal();

    if repeat == "no":
        active = False

print("CALCULATING THE RESULT....")

winner = define_winner(auction_participants)

print(art.logo)
print(f"The winner was: {winner['name']} with the bid value of ${winner['bid']}")