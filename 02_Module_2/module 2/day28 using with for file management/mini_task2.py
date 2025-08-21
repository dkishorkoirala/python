with open("user.txt", "r") as f:
    name = f.readline().strip()
    print(f"Welcome {name}")