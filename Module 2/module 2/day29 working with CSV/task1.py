import csv

with open("people.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Country"])
    writer.writerow(["Ram", "Nepal"])
    writer.writerow(["John", "USA"])
    writer.writerow(["Priya", "India"])

with open("people.csv", "r") as a:
    reader = csv.reader(a)
    for row in reader:
        print(row)
r = [
    ["Apple", "Fruit"],
    ["Tomato", "vegitable"]
]

with open("people.csv", "a", newline='') as N:
    writer = csv.writer(N)
    writer.writerows(r)