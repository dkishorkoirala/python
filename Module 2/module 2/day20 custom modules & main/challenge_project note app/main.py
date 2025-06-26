from note import add_note
from display import show_note

while True:
    print("\nMENU")
    print("1. Add note\n2. View note\n3. Exit")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        note = input("Enter your note: ")
        add_note(note)
    
    elif choice == 2:
        show_note()
    
    elif choice == 3:
        print("Thank you for using our service....")
        break
    else:
        print("Enter valid option...Try again")
        