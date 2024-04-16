from quiz_brain import QuizzBrain
from player import Player
from data import question_data
import requests


def fetch_data(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
    except:
        print("Error fetching api...")


def start_game():
    name = input("Type your name: ").lower()
    difficulty = input("Choose a difficulty: easy, medium or hard: ").lower()

    player = Player(name, difficulty)
    print("Loading...")
    data = fetch_data(
        f"https://opentdb.com/api.php?amount=10&category=18&difficulty={difficulty}&type=boolean")

    game = QuizzBrain()
    game.create_questions(data["results"])

    while player.attempts != 0:
        question = game.next_question()
        print(f"Question {game.question_number}: {question.text}")
        user_answer = input("False or True?: ").title()

        player.answer_question(question, user_answer)


start_game()
