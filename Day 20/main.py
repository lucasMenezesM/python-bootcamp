from turtle import Screen
from Snake import Snake
from Food import Food
from scoreboard import ScoreBoard
from game import Game


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake(shape="square")
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")


game = Game(score=score, screen=screen, snake=snake, food=food)

initial_message = ScoreBoard()

# if not game.is_game_on:
#     game.show_initial_message()

screen.onkey(game.start_game, "space")

screen.exitonclick()
