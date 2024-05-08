from ExerciseCalculator import ExerciseCalculator
from SpreedSheet import Spreadsheet

exercise_calculator = ExerciseCalculator()
exercise_list = exercise_calculator.calculate_exercises(age=20, height=155.0, weight=85.0)

spreedsheet = Spreadsheet()
spreedsheet.update_spreadsheet(exercises_list=exercise_list)