print("MINI TASK")
print("===========")

def favorite_book(name, book):
    return f"{name}'s favorite book is {book}."

print(favorite_book(name="Dibash", book="The Alchemist"))
print("\nChallenge")
print("===========")
def meal_plan(name, breakfast="toast", lunch="rice", dinner="pasta"):
    return f"{name}'s meal plan: Breakfast - {breakfast}, Lunch - {lunch}, Dinner - {dinner}."

print(meal_plan(name="Dibash"))
print(meal_plan("Kishor", lunch="burger"))
print(meal_plan("Krishna", breakfast="egg", lunch="roti", dinner= "roti and half rice plate" ))