import tools as t

name = input("Enter your name: ")
print(t.greet(name.capitalize()))

a= int(input("Enter a number: "))
b = int(input("Enter second number: "))

print("Addition of two numbers you entered:", t.add(a,b))
print("Multiplication of two numbers:",t.mul(a,b))

num = int(input("Guess the number(1-100): "))
secret = t.guess()
if num == secret:
    print("Congratulation you guessed correct")
else:
    print("Sorry you guessed wrong")