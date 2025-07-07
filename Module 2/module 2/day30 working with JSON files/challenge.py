import json

try: 
    with open("profiles.json", "r") as f:
        profiles = json.load(f)
except(FileNotFoundError, json.JSONDecodeError):
    profiles = []

while True:
    print("\nMenu\n")
    print("1. Add a new profile\n2. View all saved profiles\n3. Exit the app")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice:Try again")
        continue
    

    if choice == 1:
        name = input("Enter user name: ")
        age = input("Enter user age: ")
        country = input("Enter user country: ")
        skills = input("Enter user skills(seperated with comma): ").split(",")
        skills = [s.strip() for s in skills]
        
        new_profile = {
            "Name" : name,
            "Age": age,
            "Country": country,
            "Skills": skills
        }

        profiles.append(new_profile)

        with open("profiles.json", "w") as j:
            json.dump(profiles, j)

        print("\nProfile added successfully")
        
    elif choice == 2:
        with open("profiles.json", "r") as r:
            loader = json.load(r)
        
        for i, profile in enumerate(profiles, start=1):
            print(f"{i}. {profile["Name"]}-{profile["Age"]}-{profile["Country"]}-{profile["Skills"]}")
    
    elif choice == 3:
        print("Thank you for using our service....exiting")
        break
    else:
        print("Invalid Choice try again") 
