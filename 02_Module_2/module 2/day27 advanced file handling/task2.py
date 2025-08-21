file = open("diary.txt", "r")

lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()