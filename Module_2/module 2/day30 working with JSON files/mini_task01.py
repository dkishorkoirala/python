import json

profile = {
    "name" : "Dibash",
    "age" : 24,
    "country": "Nepal",
    "skills": ["Python", "Django"]
}

with open("profile.json", "w")as f:
    json.dump(profile, f)

#mini-task 2: 
with open("profile.json", "r") as r:
    loader = json.load(r)

print("Name:", loader["name"])
print("Age:", loader["age"])
print("Country:", loader["country"])
print("Skills:", loader["skills"])
