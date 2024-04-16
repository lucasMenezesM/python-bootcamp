from question_model import Question


class Player:
    def __init__(self, name, difficulty) -> None:
        self.score = 0
        self.name = name
        self.attempts = 5 if difficulty == "easy" else 3

    def answer_question(self, question: Question, user_answer: str):
        if question.answer == user_answer:
            self.score += 1
            print("Correct answer!")
        else:
            self.attempts -= 1
            print("Wrong answer...")
        print(
            f"Attempts remaning: {self.attempts} | Total score: {self.score}\n")
        if self.attempts == 0:
            print("\nGame over! You've ran out of attempts.")
