students_scores = {
    "harry": 81,
    "ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

def grade_definer(score):
    if score > 90:
        return "Outstanding"
    elif score > 80:
        return "Exceeds Expecations!"
    elif score > 70:
        return "Acceptable"
    else:
        return "fail"

students_grades = {}

for student in students_scores:
    name = student
    score = students_scores[student]

    students_grades[name] = grade_definer(score)

print(students_grades)