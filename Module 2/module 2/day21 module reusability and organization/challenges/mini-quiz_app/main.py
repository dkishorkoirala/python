from myLibrary import get_questions, ask_question
score = 0
questions = get_questions()

for q, ans in questions:
    if ask_question(q, ans):
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\nYour final score is: {score}/{len(questions)}")
