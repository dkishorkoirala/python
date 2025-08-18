def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

age = get_number("Enter your age: ")
height = get_number("Enter your height in cm: ")

print(f"You are {age} years old and {height} cm tall.")