from turtle import Turtle


class Writer(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()

    def write_state(self, position, text):
        self.goto(position)
        self.write(arg=text, align="center", font=("Arial", 10, "normal"))
