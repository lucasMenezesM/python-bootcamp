import turtle


class Painter(turtle.Turtle):
    def __init__(self, color: str, shape: str):
        super().__init__()
        self.color(color)
        self.shape(shape)

    def move_right(self):
        self.setheading(0)
        self.forward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def move_up(self):
        self.setheading(90)
        self.forward(10)

    def move_down(self):
        self.setheading(270)
        self.forward(10)

    def move_forward(self, distance):
        self.forward(distance)
