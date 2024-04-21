from turtle import Turtle

DATA_PATH = "Day 20\data.txt"


class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.high_score = self.read_high_score()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            with open(DATA_PATH, mode="w") as data:
                data.write(f"{self.score}")

            self.high_score = self.read_high_score()

        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 30, "normal"))

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def read_high_score(self):
        with open(DATA_PATH, mode="r") as data:
            high_score = data.read()
            print(int(high_score))
            return int(high_score)

    # def game_over(self):
