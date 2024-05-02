from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# data = pandas.read_csv("Day 31/data/french_words.csv")
# words_list = data.to_dict(orient="records")

cards_list = None

try:
    data = pandas.read_csv("Day 31/data/cards_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("Day 31/data/french_words.csv")
    data.to_csv("Day 31/data/cards_to_learn.csv", index=False)
finally:
    cards_list = data.to_dict(orient="records")

# Alternative code:
# words_list = [{row["French"]: row["English"]} for index,row in data.iterrows()]


#---------- Functions --------------
card = {}


def right_answer():
    # global cards_list
    cards_list.remove(card)
    list_to_learn = pandas.DataFrame(cards_list)
    list_to_learn.to_csv("Day 31/data/cards_to_learn.csv", index=False)
    next_card()


def next_card():
    global flip_timer, card
    window.after_cancel(flip_timer)

    if len(cards_list) == 0:
        canvas.itemconfig(card_title, text="Congratulations!", fill="white")
        canvas.itemconfig(card_word, text="You completed all cards", fill="white", font=("Arial", 35, "bold"))
        return
    

    canvas.itemconfig(canvas_bg_img, image=card_front_img)
    card = random.choice(cards_list)
    # french, english = list(random.choice(words_list).items())[0]

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=card["French"], fill="black")

    flip_timer = window.after(3000, flip_card)

    
def flip_card():
    canvas.itemconfig(canvas_bg_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")



window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card")

# Canvas Setup
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="Day 31/images/card_front.png")
card_back_img = PhotoImage(file="Day 31\images\card_back.png")
canvas_bg_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# Buttons Setup
green_btn_img = PhotoImage(file="Day 31/images/right.png")
green_btn = Button(image=green_btn_img, highlightthickness=0, borderwidth=0, command=right_answer)
green_btn.grid(column=0,row=1)

red_btn_img = PhotoImage(file="Day 31/images/wrong.png")
red_btn = Button(image=red_btn_img, highlightthickness=0, borderwidth=0, command=next_card)
red_btn.grid(column=1,row=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()