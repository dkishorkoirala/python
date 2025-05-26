print("-----Task1-----")
fruits_tuple = ("apple", "banana","cherry","mango","watermelon")

print(fruits_tuple[1])

print("\n-----Task2-----")
# fruits_tuple[2] = "potato"
# Traceback (most recent call last):
#   File "D:\coding everything\python_with_exercises\python\day6\practice_ex.py", line 7, in <module>
#     fruits_tuple[2] = "potato"
#     ~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

print("\n-----Task3-----")
print(fruits_tuple.count("mango"))

print("\n-----Task4-----")
color_set = {"red", "blue", "green","orange","black"}
print(color_set)

print("\n-----Task5-----")
color_set.add("white")
print(color_set)

print("\n-----task6-----")
color_set.add("red")
print(color_set)

print("\n-----task7-----")
color_set.remove("blue")
print(color_set)

print("\n------task8-----")
color_set2 = {"red", " yellow","pink","green"}
print(color_set.union(color_set2))

print("\n-----task9-----")
print(color_set.intersection(color_set2))

print("\n-----task10-----")
print(color_set.difference(color_set2))

print("\n\n-----mini-challenge-----")
attendance= set()
for i in range(5):
    name = input("Enter your name: ")
    attendance.add(name)

check_name = input("Enter name to chek:")

if check_name in attendance:
    print(f"{check_name} is present")
else:
    print(f"{check_name} is not present")    