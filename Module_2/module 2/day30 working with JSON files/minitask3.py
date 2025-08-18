import json
choice = int(input("Enter how many profile you wish to enter : "))

l = []
for i in range(choice):
    name = input("Enter Profiles name: ")
    age = input("Enter profile's age: ")
    country = input("Enter your country: ")
    skills = input("Enter your skills(commas-seperated): ").split(",")
    skills = [s.strip() for s in skills]
    l.append({
        "Name" : name,
        "Age" : age,
        "Country": country,
        "Skills": skills
    })

with open("profile.json", "w") as a:
    json.dump(l, a)

print("All profiles saved successfully")