import turtle
import prettytable

tony = turtle.Turtle()
my_screen = turtle.Screen()


def move_back():
    tony.back(10.0)


def move_forward():
    tony.forward(10.0)


def move_right():
    tony.right(10.0)


def move_left():
    tony.left(10.0)


my_screen.bgcolor("orange")
tony.shape("turtle")
tony.color("white")
my_screen.listen()
my_screen.onkeypress(move_back, "Down")
my_screen.onkeypress(move_right, "Right")
my_screen.onkeypress(move_left, "Left")
my_screen.onkeypress(move_forward, "Up")
my_screen.exitonclick()

print(tony)
print(my_screen)
