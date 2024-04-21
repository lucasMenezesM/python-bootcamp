with open("Day 24/Input/Names/invited_names.txt", mode="r") as data:
    names_list = data.readlines()
    formated_names = []
    for name in names_list:
        formated_names.append(name.strip("\n"))


with open("Day 24/Input/Letters/starting_letter.txt", mode="r") as data:
    starting_letter = data.read()


for name in formated_names:
    new_letter = starting_letter.replace("[name]", name)
    with open(f"Day 24/Output/ReadyToSend/Letter_for_{name}.txt", mode="w") as data:
        data.write(new_letter)
