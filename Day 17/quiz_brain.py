from question_model import Question
import random


class QuizzBrain:
    def __init__(self) -> None:
        self.question_number = 0
        self.question_list = []

    def create_questions(self, data):
        collection = []
        for question in data:
            collection.append(
                Question(question["question"], question["correct_answer"]))
        self.question_list = collection

    def next_question(self):
        question = random.choice(self.question_list)
        self.question_list.remove(question)
        self.question_number += 1
        return question
