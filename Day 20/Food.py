from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, color: str = "blue", shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape(shape)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(color)
        self.speed("fastest")
        self.spawn()

    def spawn(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto((random_x, random_y))
