with open("notes.txt", "w+") as f:
    f.write("This is new note.\n")
    f.seek(0)
    print(f.read())
    
with open("notes.txt", "a+") as f:
    f.write("This is new note.\n")
    f.seek(0)
    print(f.read())