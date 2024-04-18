from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Turtle):
    def __init__(self, shape: str = "classic", color: str = "white", undobuffersize: int = 1000, visible: bool = True, is_pen_up: bool = True) -> None:
        super().__init__(shape=shape, undobuffersize=undobuffersize, visible=False)

        self.color(color)
        self.snake_body = []
        self.create_snake()
        self.tail = self.snake_body[-1]
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_snake_piece(START_POSITION[i])

    def add_snake_piece(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake_body.append(new_turtle)

    def move_forward(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            following_seg = (self.snake_body[seg_num - 1])

            self.snake_body[seg_num].goto(
                (following_seg.xcor(), following_seg.ycor()))

        self.head.forward(20)
        # self.snake_body[0].setheading(90)

    def turn_up(self):
        self.head.setheading(
            90) if self.head.heading() != 270 else None

    def turn_down(self):
        self.head.setheading(
            270) if self.head.heading() != 90 else None

    def turn_left(self):
        self.head.setheading(
            180) if self.head.heading() != 0 else None

    def turn_right(self):
        self.head.setheading(
            0) if self.head.heading() != 180 else None

    def increase(self):

        self.add_snake_piece(self.tail.pos())
