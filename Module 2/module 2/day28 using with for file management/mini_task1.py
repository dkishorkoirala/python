name = input("Enter your name: ").strip()

with open("user.txt", "w") as f:
    f.write(name)

print("Name saved!!")