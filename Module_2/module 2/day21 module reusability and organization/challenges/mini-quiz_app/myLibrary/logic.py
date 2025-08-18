def ask_question(question, correct_answer):
    user_input = input(f"{question} ").strip().lower()
    return user_input == correct_answer.lower()
