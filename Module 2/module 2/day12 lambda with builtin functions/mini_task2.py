print("1. find the name with the smallest length in the list below:")

names = ["Sam", "Elizabeth", "Jo", "Charles"]

smallest_name = min(names, key = lambda x: len(x))
print(smallest_name)

print ("\n2. from the list of students, find the one with the lowest average score:")
student=[
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [70, 88, 95]},
    {"name": "Charlie", "scores": [90, 92, 85]}
]

lowest_average = min (student , key = lambda x: sum(x["scores"])/len(x["scores"]))
print(lowest_average)

print("\n3. Find the dictionary with the highest age from this list:")
people = [
    {"name": "Tom", "age": 32},
    {"name": "Jerry", "age": 25},
    {"name": "Spike", "age": 40}
]

highest_average= max(people, key = lambda x: x["age"])
print(highest_average)

print("\n4. Find the tuple where the product of elements is the highest:")

tuples = [(2, 5), (1, 10), (4, 3)]
highest_multiple = max(tuples, key= lambda x: x[0]*x[1])
print(highest_multiple)

print("\n5. Find the student with the highest lowest individual score:")

students = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [70, 88, 95]},
    {"name": "Charlie", "scores": [90, 92, 85]},
]
highest_lowest= max(students, key = lambda x: min(x["scores"]))
print(highest_lowest)