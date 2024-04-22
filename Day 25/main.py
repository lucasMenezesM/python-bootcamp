# # with open("Day 25/weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     weather_data = []
# #     for line in data:
# #         weather_data.append(line.strip("\n"))

# # import csv

# # with open("Day 25/weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for index, row in enumerate(data):
# #         if index == 0:
# #             continue
# #         temperatures.append([row[0], int(row[1]), row[2]])
# # # print(data)
# # print(temperatures)

# import pandas

# # data = pandas.read_csv("Day 25/weather_data.csv")

# # temp_list = data["temp"].to_list()
# # max_temperature = data.temp.max()
# # avg_temp = sum(temp_list) / len(temp_list)
# # # print(data["temp"].max())
# # # print(f"Avarage temperature: {round(avg_temp, 2)}")
# # # print(data[data.temp == max_temperature].temp)
# # # (0 °C × 9/5) + 32 = 32 °F

# # monday_temp = ((data[data.day == "Monday"].temp[0]) * 9/5) + 32
# # print(monday_temp)

# data = pandas.read_csv(
#     "Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# # print(data["Primary Fur Color"])
# gray_list_count = len(data[data["Primary Fur Color"]
#                       == "Gray"]["Primary Fur Color"])
# cinnamon_list_count = len(
#     data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"])
# black_list_count = len(
#     data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"])

# colors_list = {
#     "Fur Colors": ["Black", "Red", "Gray"],
#     "Count": [black_list_count, cinnamon_list_count, gray_list_count],
# }

# dic_colors = pandas.DataFrame(colors_list)
# dic_colors.to_csv("Day 25/colors.csv")

import turtle
import pandas
from writer import Writer

IMAGE_PATH = "Day 25/blank_states_img.gif"
CSV_PATH = "Day 25/50_states.csv"

states_data = pandas.read_csv(CSV_PATH)

total_states = len(states_data.state)
all_states = states_data["state"].to_list()
guessed_states = []

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

writer = Writer()

game_is_on = True
while game_is_on:

    user_guess = screen.textinput(
        title=f"U.S. States Game {len(guessed_states)}/{total_states}", prompt="Type the name of the State").title()

    if user_guess == "Exit":
        break

    state = states_data[states_data["state"] == user_guess]
    if state.state.empty:
        print("Does not exist.")
        continue
    else:
        guessed_states.append(state.state.item())
        writer.write_state(text=state.state.item(), position=(
            state.x.item(), state.y.item()))
        print(state)
        print("Right answer!")

    # if states_answered == total_states:
    #     game_is_on = False


missing_states = []
missing_states_dic = {
    "state": []
}

for state in all_states:
    if state not in guessed_states:
        missing_states_dic["state"].append(state)

df = pandas.DataFrame(missing_states_dic)
df.to_csv("Day 25/Missing_States.csv")

print(missing_states_dic)
print(len(missing_states_dic["state"]))
