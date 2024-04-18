from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from scoreboard import ScoreBoard
import time
import pygame


class Game():

    def __init__(self, screen: Screen, snake: Snake, score: ScoreBoard, food: Food) -> None:
        self.snake = snake
        self.screen = screen
        self.score = score
        self.food = food
        self.is_game_on = False
        pygame.init()
        pygame.mixer.music.load(
            'A:\projetos python\Bootcamp 100 days of code Python\Day 20\main-theme.mp3')

    def start_game(self):
        self.score.clear()
        pygame.mixer.music.play()
        self.game_is_on = True

        while self.game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move_forward()

            if self.snake.head.distance(self.food) < 15:
                self.food.spawn()
                self.score.increase()
                self.snake.increase()

            if self.snake.head.ycor() < -299 or self.snake.head.ycor() > 299 or self.snake.head.xcor() < -299 or self.snake.head.xcor() > 299:
                print("gamer over")
                self.score.game_over()
                pygame.mixer.music.stop()
                self.game_is_on = False
                pygame.mixer.music.set_volume(0.5)

            self.snake_body_colision = self.snake.snake_body[1: len(
                self.snake.snake_body)]
            for piece in self.snake_body_colision:
                if self.snake.head.distance(piece) < 15:
                    self.score.game_over()
                    pygame.mixer.music.stop()
                    self.game_is_on = False

    # def show_initial_message(self):
    #     self.score.goto(0, 0)
    #     self.score.write(arg="Press Space to start the Game",
    #                      align="center", font=("Arial", 25, "normal"))
