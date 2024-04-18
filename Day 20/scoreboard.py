from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self, font: str = "Arial", fontsize: int = 15, align: str = "center"):
        self.clear()
        self.write(
            arg=f"Score: {self.score}", align=align, font=(font, fontsize, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 30, "normal"))

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
