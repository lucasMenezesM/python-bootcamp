from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface

question_bank = [
    Question(q_text=question["question"], q_answer=question["correct_answer"]) for question in question_data
]

quiz = QuizBrain(question_bank)

quiz_interface = QuizzInterface(quiz_brain=quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
