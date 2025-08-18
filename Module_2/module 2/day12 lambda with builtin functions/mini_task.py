print("task 1 : sort this list of tuples by first item")

pairs = [(3,4),(1,2),(5,0)]
sorted_pair= sorted(pairs, key = lambda x: x[0])
print(sorted_pair)

print("\n2. sort this list of names by their length:")

names=["Sam", "Elizabeth", "Jo", "Charles"]
sorted_names = sorted(names, key = lambda x: len(x))
print(sorted_names)

print("\n3. sort a list of dictionaries by age:")
people = [
    {"name" :"Tom", "age" : 32},
    {"name": "jerry","age": 25},
    {"name": "spike","age": 40}
]

sorted_people = sorted(people, key = lambda x: x['age'])
print(sorted_people)

print("\nBonus task")

students = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [70, 88, 95]},
    {"name": "Charlie", "scores": [90, 92, 85]},
]

sorted_student = sorted(students, key = lambda x: sum(x['scores'])/len(x['scores']))
print(sorted_student)

print("\nbonus 2")
students = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [70, 88, 95]},
    {"name": "Charlie", "scores": [90, 92, 85]},
]

sorted_student = sorted(students, key = lambda x: max(x['scores']))
print(sorted_student)