print("practiced exercises of day 3")
print("String length and first character")
word = input("Enter any word: ")

print(len(word), "is the length of the word and first character is", word[0])

print("\nReverse input")
name = input("Enter any word you wanna reverse: ")
print(name[::-1], "is the reverse of the word")

print("\nCapitalized and reverse")
ok = input("Enter any word to capitalize and dont forget the word 'Hello' to replace with thank you: ")

print(ok.capitalize(),"is the capitalized word and", ok.replace("Hello", "Thank you"))

print("\nAge to srting")
age = int(input("Enter your age: "))
print("You are", str(age), "years old")

print("\nUsername Generator")
firstname= input("Enter first name: ")
lastname = input("Enter last name: ")

print("The username is:",firstname.lower()+"."+lastname.lower())

print("\nInitials Extractor")
uname = input("Enter Full name:")
space_index = uname.find(" ")
first_initial = uname[0].upper()
last_initial = uname[space_index+1].upper()
print("Initials:", first_initial + last_initial)

print("\nsimple string analyzer")
string = input("Enter any string:")

print(len(string),"is the number of characters used")
print("Contains 'Python'?:", "Python" in string)

print ("\nAge in days")
uage = int(input("Enter age in years: "))
print("You are", uage*365, "days old(approx).")


print("\nNumber to words")
num = int(input("Enter any number: "))
#dont know logic behind
print("Sorry, we’ll build this once we learn loops!")


print("\nChallenge")
fname = input ("Enter name: ")
city = input("Enter city: ")
proff = input("Enter your profession: ")
print("Hello", fname +"! You are a " + proff + " from " + city + ".")