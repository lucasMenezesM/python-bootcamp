from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.change_bg = self.window.after(0, None)

        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "normal"))
        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125, 
            text="Some Question", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR, 
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="Day 34/images/true.png")
        self.true_button = Button(image=true_image, borderwidth=0, bg=THEME_COLOR, highlightthickness=0, command=self.check_right)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="Day 34/images/false.png")
        self.false_button = Button(image=false_image, borderwidth=0, bg=THEME_COLOR, highlightthickness=0, command=self.check_wrong)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.score_text.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)

            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You completed all the questions!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    
    def check_right(self) -> None:
        is_right = self.quiz.check_answer(user_answer="true")
        self.give_feedback(is_right)
    
    
    def check_wrong(self) -> None:
        is_right = self.quiz.check_answer(user_answer="false")
        self.give_feedback(is_right)

    def give_feedback(self, answer: bool):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.canvas.itemconfig(self.question_text, fill="white")

        self.change_bg = self.window.after(1000, self.get_next_question)
