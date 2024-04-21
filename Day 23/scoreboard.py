from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.update_score(score=0)

    def update_score(self, score):
        self.clear()
        self.goto(x=-200, y=240)
        self.write(arg=f"Level {score}", align="center", font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write(arg=f"Game Over", align="center", font=FONT)
