from turtle import Turtle, Screen
import turtle
import random
import colorgram

tommy = Turtle()
screen = Screen()

turtle.colormode(255)


def draw_square():
    tommy.forward(100)
    tommy.left(90)
    tommy.forward(100)
    tommy.left(90)
    tommy.forward(100)
    tommy.left(90)
    tommy.forward(100)


colors = ["red", "blue", "green", "orange", "yellow", "purple", "pink"]


def draw_shape(num_sides):
    tommy.color(random.choice(colors))
    angle = 360 / num_sides
    for i in range(num_sides):
        tommy.forward(100)
        tommy.left(angle)


def draw_different_shapes():

    for i in range(5):
        draw_shape(i+4)


def move_forward():
    tommy.forward(5)
    tommy.penup()
    tommy.forward(5)
    tommy.pendown()


def move_left():
    tommy.left(90)


def move_right():
    tommy.right(90)


def move_back():
    tommy.back(180)


def pick_random_color():
    color1 = random.randint(1, 255)
    color2 = random.randint(1, 255)
    color3 = random.randint(1, 255)
    return (color1, color2, color3)


def draw_different_circles():
    for i in range(1, 100):
        tommy.color(pick_random_color())
        tommy.circle(75.0)
        tommy.left(i)


def random_walk():
    directions = ["left", "right"]

    for i in range(1, 50):
        direction_chosen = random.choice(directions)
        tommy.color(pick_random_color())

        if direction_chosen == "left":
            tommy.right(90)
        else:
            tommy.left(90)

        tommy.forward(50)


tommy.pensize(1)
tommy.speed(11)
screen.listen()
# screen.onkeypress(move_forward, "Up")
# screen.onkeypress(move_left, "Left")
# screen.onkeypress(move_right, "Right")
# screen.onkeypress(move_back, "Down")
# screen.onkeypress(draw_different_circles, "space")


def generate_color_from_image(link, colors_number):
    """Generate a list with the colors of a specific image. Returns a list of different RGB colors from the image selected"""

    paiting_colors = colorgram.extract(link, colors_number)
    colors = []
    for color in paiting_colors:
        colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))
    return colors


# screen.screensize(100, 100)
print(screen.screensize())

tommy.penup()
tommy.setposition(-400, -300)
# tommy.setposition(-350, -300)
# tommy.dot(20, "red")
# tommy.setposition(-300, -300)
# tommy.dot(20, "red")

rgb_colors = generate_color_from_image(
    'A:\projetos python\Bootcamp 100 days of code Python\Day 18\painting.jpg', 30)

x = tommy.pos()[0]
y = tommy.pos()[1]

for i in range(1, 14):
    move_x = x
    for j in range(1, 16):
        move_x += 50
        tommy.setposition(move_x, y)
        tommy.dot(20, random.choice(rgb_colors))
    y += 50

tommy.shape("turtle")
tommy.color("blue")

# screen.bgcolor("black")
screen.exitonclick()
