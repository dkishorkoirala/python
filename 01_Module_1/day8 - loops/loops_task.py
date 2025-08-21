print("For loop tasks")
for i in range(1, 11):
    print(i)

print("square till 5")
for i in range (1,6):
    print(i**2)

print("each letter in python")
word = "Python"
for letter in word:
    print(letter)

print("while loop tasks")
counter = 10
while counter > 0:
    print(counter)
    counter-=1

num = 5
while True:
    number = int(input("Enter a number: "))
    if number == num:
        print("Walla you right")
        break

print("challenge 1")
for i in range(10, 0,-1):
    print(i)
print("Blast Off!")


print("challenge - 2")

num = int(input("Enter any number: "))
sum = 0
for i in range(1, num+1):
    sum += i
    print(sum)