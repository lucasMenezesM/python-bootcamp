import random
import turtle
from Painter import Painter

# timmy = turtle.Turtle()


# def move_right():
#     timmy.setheading(0)
#     timmy.forward(10)


# def move_left():
#     timmy.setheading(180)
#     timmy.forward(10)


# def move_up():
#     timmy.setheading(90)
#     timmy.forward(10)


# def move_down():
#     timmy.setheading(270)
#     timmy.forward(10)


# def draw_forwards():
#     timmy.forward(10)


# def draw_back():
#     timmy.back(10)


# def draw_right():
#     timmy.right(20)


# def draw_left():
#     timmy.left(20)


# def clear_screen():
#     timmy.setposition(0, 0)
#     timmy.clear()


# # timmy = Arrow()
screen = turtle.Screen()


# screen.listen()
# screen.onkey(move_right, "Right")
# screen.onkey(move_left, "Left")
# screen.onkey(move_up, "Up")
# screen.onkey(move_down, "Down")

# screen.onkey(draw_right, "d")
# screen.onkey(draw_left, "a")
# screen.onkey(draw_forwards, "w")
# screen.onkey(draw_back, "s")
# screen.onkey(clear_screen, "c")

screen.setup(width=500, height=400)
colours = ["red", "blue", "green", "purple", "yellow", "orange"]

# turtle1 = turtle.Turtle(shape="turtle")
# turtle2 = turtle.Turtle(shape="turtle")
# turtle3 = turtle.Turtle(shape="turtle")
# turtle4 = turtle.Turtle(shape="turtle")
# turtle5 = turtle.Turtle(shape="turtle")

# turtle1.penup()
# turtle2.penup()
# turtle3.penup()
# turtle4.penup()
# turtle5.penup()

# turtle1.color(colours[0])
# turtle2.color(colours[1])
# turtle3.color(colours[2])
# turtle4.color(colours[3])
# turtle5.color(colours[4])

# turtle1.setposition(-230, 0)
# turtle2.setposition(-230, 50)
# turtle3.setposition(-230, -50)
# turtle4.setposition(-230, 100)
# turtle5.setposition(-230, -100)

turtles = []

for i in range(0, 6):
    new_turtle = Painter(shape="turtle", color=colours[i])
    # new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(-230, -150 + (50 * i))

    turtles.append(new_turtle)


user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? ")

is_race_on = False

if user_bet:
    is_race_on = True


while is_race_on:
    for competitor in turtles:
        if competitor.xcor() > 230:
            if competitor.pencolor() == user_bet:
                print(f"You won! | The {competitor.pencolor()} won the race!")
            else:
                print(f"You lost! | The {competitor.pencolor()} won the race!")
            is_race_on = False
            break

        competitor.move_forward(random.randint(5, 15))

# jhon = Painter("blue", "turtle")

# # print(jhon.color())

# jhon.move_down()
# jhon.move_up()

screen.exitonclick()
