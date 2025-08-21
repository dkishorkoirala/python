print("------task1-----")
var = "stop"

while True:
    inp = input("Enter a Word: ").lower()
    if inp == var:
        break

print("-------task2------")
for i in range(11):
    if i % 2 == 0:
        continue
    print(i)

print("----------task 3--------")
for i in range(6):
    print(f"Loop {i}")
else:
    print("Loop ended properly")

print("----task 4------")
for i in range(1,6):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()

print("Challenge")
password = "1234"
for i in range(3):
    passw = input("enter a password: ")
    if passw == password:
        print("Access granted")
        break
else: 
    print("Access Denied")