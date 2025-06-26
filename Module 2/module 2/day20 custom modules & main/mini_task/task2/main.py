from math_plus import square, cube

while True:
    print("\nOPTION:")
    print("1. Find Square\n2. Find Cube\n3. Exit")

    choose = int(input("Enter your choice: "))
    if choose == 1:
        number = int(input("\nEnter number to find square: "))
        square(number)
    elif choose == 2:
        number = int(input("\nEnter the number to find cube: "))
        cube(number)
    elif choose == 3:
        print("\nThank your for choosing us...")
        break
    else:
        print("\nPlease enter valid option...")

