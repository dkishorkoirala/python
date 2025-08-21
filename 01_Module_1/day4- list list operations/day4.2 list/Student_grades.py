# challenge of the day: student grades
# task:
# ask the user for names and scores of 3 students.
# store them in a nested list.
# then print all students with their scores, and the average score.

students = []
total_score = 0
for i in range(3):
    name = input(f"Enter student name:")
    score = float(input(f"Enter student score:"))
    students.append([name, score])
    total_score += score

for student in students:
    print(f"{student[0]}: {student[1]}")

average = total_score / 3
print(f"Average score: {average:.2f}")