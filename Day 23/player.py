from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shape("turtle")
        self.level = 0
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

    def finish_crossing(self):
        self.level += 1
        self.goto(STARTING_POSITION)
