from turtle import Turtle, Screen
from car import Car
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.car_list: list[Car] = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(x=300, y=random.randint(-220, 220))
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.backward(self.move_speed)
            # car.goto(x=car.xcor()+(-self.move_speed), y=car.ycor())

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
