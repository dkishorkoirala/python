from my_tools import square, cube, is_prime, to_celsius, to_fahrenheit, word_count, is_palindrome, word_rev, add_notes, show_notes


while True:
    print("\nMenu:")
    print("1. Math Tools\n2. Temperature Tools\n3. String Tools\n4. Notes\n5. Exit")

    choice = int(input("Enter Your choice: "))

    if choice == 1:
        num = int(input("\nEnter the number to find square: "))
        print("Square: ",square(num))

        num2 = int(input("\nEnter the number to find cube: "))
        print("Cube:", cube(num2))

        num3 = int(input("\nEnter the number to check if its prime: "))
        print("Prime:", is_prime(num3))
    
    elif choice == 2:
        d = int(input("\nEnter fahrenheit degree to convert to degree celsius: "))
        print("TO celsius:",to_celsius(d))

        f = int(input("\nEnter degree celsius to convert to degree fahrenheit: "))
        print("To Fahrenheit:",to_fahrenheit(f))

    elif choice == 3:
        w = input("\nEnter word to count: ")
        print("The number of letters used is:", word_count(w))

        w = input("\nEnter word to check if its palindrome: ")
        print("Palindrome check reslut found:", is_palindrome(w))

        w = input("\nEnter word to find reverse:")
        print("Reverse is:",word_rev(w))

    elif choice == 4:
        check = input("\nDo you want to add notes(yes/no): ").lower()
        if check == "yes":
            notes = input("\nEnter your note: ")
            add_notes(notes)
            print(show_notes())
        else:
            print(show_notes())
    elif choice == 5:
        print("\nThank you for your visit...")
        break
    else:
        print("\nInvalid choice, please try again...")