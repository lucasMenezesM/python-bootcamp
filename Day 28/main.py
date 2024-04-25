from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")
    check_symbol.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    work_sec = WORK_MIN*60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60

    global reps
    reps += 1
    if reps % 8 == 0:
        timer_title.config(text="Break")
        count_down(long_break)
    elif reps % 2 == 0:
        timer_title.config(text="Break")
        count_down(short_break)
    else:
        timer_title.config(text="Work!")
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count: int):
    count_min = math.floor(count/60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔️"
        check_symbol.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# --------TIMER TITLE----------
timer_title = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 40))
timer_title.grid(column=1, row=0)

# --------CANVAS IMAGE----------
canvas = Canvas(bg=YELLOW, width=200, height=224, highlightthickness=0)
tomato_img = PhotoImage(file="Day 28/tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(column=1, row=1)

# --------START BUTTON----------
start_button = Button(text="Start", width=5, font=("Arial", 10, "bold"), background="white", border=0, command=start_count)

start_button.grid(column=0, row=2)

# --------CHECK SYMBOL----------
check_symbol = Label(foreground=GREEN, background=YELLOW, font=(FONT_NAME, 15), pady=5)
check_symbol.grid(column=1, row=3)

# --------RESET BUTTON----------
reset_button = Button(text="Reset", width=5, font=("Arial", 10, "bold"), background="white", border=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()