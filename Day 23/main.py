import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")

screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()
list_of_cars = cars.car_list

game_is_on = True

screen.listen()
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_up, "Up")

while game_is_on:

    time.sleep(0.1)
    screen.update()
    cars.spawn_car()

    cars.move_car()

    if player.ycor() > FINISH_LINE_Y:
        player.finish_crossing()
        score.update_score(score=player.level)
        cars.increase_speed()

    # todo Use for loop to create colision later
    for car in list_of_cars:

        if player.distance(car.pos()) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()
