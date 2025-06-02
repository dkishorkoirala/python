print("1. Smart ATM")

balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice =int(input("Enter you option: "))

    if choice == 1:
        print("Your balance is: ", balance)
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print("Amount deposited successfully, Your current balance is: ", balance)
    elif choice == 3:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
            
        else: 
            balance -= amount
            print(f"Withdrawl successful of amount {amount}, Your current balance is: {balance}")
    elif choice == 4:
        print("Thank you for using our Smart ATM")
        break
    else:
        print("Invalid option, please choose a valid option")


print ("2. Unique word counter")
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Number of unique words: ", len(unique_words))
print(unique_words)
    
print("3. multiplication Table Generator")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

print("4. Top Grade Students")
students = []
for i in range(3):
    name = input("Enter student name: ")
    grade = input("Enter student grade: ").upper()
    student = {
        "name": name,
        "grade": grade
    }
    students.append(student)
for student in students:
    if student["grade"] in ["A" ,"B"]:
        print(student)

print("5. Secret login attempts")
password = "1234"
for i in range(3):
    pas = input("Enter a password: ")
    if pas == password:
        print("Welcome!")
        break
else:
    print("Access denied")

print("6. Number guessing game")
num = 7
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    else:
        print("Correct!")
        break