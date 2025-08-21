print("task 1")
def mul_all(*args):
    result = 1
    for arg in args:
        result *= arg
    return result
   
print(mul_all(1,2,3,4,5))

print("task2")
def des_per(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
des_per(name = "john", age = "30")

print("task3")
menu={
    "burger": 120,
    "pizza": 150,
    "salad": 100
}

item = input("enter the item name: ").lower()
if item in menu.keys():
    print(f"price of {item.capitalize()} is Rs.{menu[item]}")

print("final challenge")
def report_card(name, **marks):
    print(f"Student: {name}")
    total = 0
    for subject, mark in marks.items():
        total += mark
    
    avg = total / len(marks)
        
    if avg >= 90:
        grade = "Excellent"
    elif avg >= 75:
        grade = "Good"
    else:
        grade = "Needs Improvement"
        
    print(f"Average: {avg}")
    print(f"Grade: {grade}")

report_card("Arya", math=95, science=90, english=85)