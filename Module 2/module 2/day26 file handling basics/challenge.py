message = input("Enter any message to add in diary: ")
with open("diary.txt", "a") as file:
    file.write(message + "\n")
