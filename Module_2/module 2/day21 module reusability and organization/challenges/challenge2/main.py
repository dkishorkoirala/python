from my_toolkit import to_fahrenheit, to_celsius, is_palindrom, count_words, div, mul

while True:
    print("MENU")
    print("1. Temperature Converter\n2. Word Checker\n3. Math Operation\n4. Exit")
    choice= int(input("\nEnter Your choice: "))

    if choice == 1 :
        degree = int(input("\nEnter the temperature you will love to convert from fahrenheit to celsius: "))
        print(to_celsius(degree))

        degree2 = int(input("Enter Temperature to convert to Fahrenheit: "))
        print(to_fahrenheit(degree2))

    elif choice == 2:
        sen = input("Enter a sentence: ")
        print("You entered ",count_words(sen),"words")

        pal = input("Enter word to check palindromic order: ")
        print(is_palindrom(pal))

    elif choice == 3:
        a = int(input("Enter the first number to perform multiplication: "))
        b = int(input("Enter second number to perform multiplication: "))

        print(mul(a, b))

        c = int(input("Enter number to divide : "))
        d = int(input("Enter number to divide(the one to divide): "))
        print(div(c, d))

    elif choice == 4:
        print("Thank you .... please visit again...")
        break
    else:
        print("Invalid choice,.... choose another number...")

