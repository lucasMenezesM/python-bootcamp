from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True, position: tuple = (0, 0)) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2.5, stretch_wid=1)
        self.goto(position)
