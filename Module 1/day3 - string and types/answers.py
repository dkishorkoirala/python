print("1. Username Generator")
fname = input("enter first name: ")
lname = input("enter last name: ")

print("your username is: ", fname.lower() +"."+lname.lower())

print("2. Initials extractor")
username = input("Enter full name: ")
parts = username.split()
initials = ""
for part in parts:
    initials += part[0].upper()
print("Initials:", initials)

print("3. Age in days converter")
age = int(input("Enter the age in years: "))
days = age * 365
print("Age in days(roughly): ", days)

print("4. Reverse my name")
name = input("Enter your name: ")
print("Your name in reverse order: ", name[::-1])

print("5. Word Counter")
sen = input("Enter a sentence: ")
print("Number of words in the sentence: ", len(sen.split()))

print("6. simple chatbot greeting")
un = input("Enter your name: ")
feel = input("Enter how you feeling: ")
print(f"Hi {un.capitalize()}! I'm glad you're feeling {feel.lower()} today.")

print ("7. vowel counter.")
text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for v in vowels:
    count += text.count(v)
print("Total vowels:", count)

print ("8. Title casing.")
cs= input("Enter a sentence: ")
print("Title case: ", cs.title())

print("9. Temperature conversion.")
c = float(input("Enter temperature in celsius: "))
f = (c * 9/5) + 32
print("Temperature in fahrenheit: ", f)

print("10. FUnny sring formatter.")
name = input("Enter your name: ")
fc = input("Enter your favorite color: ")
animal = input("Enter any animal: ")

print(f"Once upon a time, {name} saw a {fc} {animal} dancing in the rain.")