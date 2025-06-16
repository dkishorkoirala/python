print("1. Given a list of numbers, filter out only the odd numbers.")

numbers = [10, 15, 20, 25, 30, 35]

odd= list(filter( lambda x: x % 2 != 0, numbers))
print(odd)

print("\n2. Given a list of strings, use map and lambda to convert all strings to uppercase.")

words = ["apple", "banana", "cherry"]

upperword = list(map(lambda x: x.upper(), words))
print(upperword)

print("\n3. From the list of students below, filter only those who have an average score above 85.")

students = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [70, 88, 95]},
    {"name": "Charlie", "scores": [90, 92, 85]},
]

avg = list(filter(lambda x: sum (x["scores"])/len(x["scores"]) > 85, students))
print(avg)

print("\nBonus_challene 1")
data = [("Alice", 85), ("Bob", 90), ("Charlie", 82)]

re= list(map(lambda x:   f"{x[0]}: {x[1]}", data))
print(re)

print("\nBonus_challenge 2")

students = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [70, 88, 95]},
    {"name": "Charlie", "scores": [90, 92, 85]},
]

new= list(map(lambda x: {**x , "average": round(sum(x['scores'])/len(x['scores']), 2)},students))
print(new)