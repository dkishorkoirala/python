import csv

while True:
    print("\nMenu\n")
    print("1. Add new Contact\n2. View all saved Contacts\n3. Exit")

    try:
        choice = int(input("Enter your choice (1/2/3): "))
    except ValueError:
        print("\nInvalid input! Please enter numbers only.")
        continue
    
    if choice == 1:
        info = []
        for i in range(1):
            name = input("Enter your name: ")
            phone = input("Enter your number: ")
            email = input("Enter user email: ")
            info.append([name, phone, email])
        
        with open("contacts.csv", "a", newline='') as a:
            writer = csv.writer(a)
            writer.writerows(info)

    elif choice == 2:
        with open("contacts.csv", "r") as r:
            reader = csv.reader(r)
            for row in reader:
                print(row)
    
    elif choice == 3:
        print("Thanks for using us...")
        break
    else:
        print("Invalid input choose next one...")
