#secret login attempt:

correct= "12345"
attempts = 3

for i in range (attempts):
    entered = input("Enter password: ")
    if entered == correct:
        print("Access granted")
        break
    else:
        print("Wrong Password.")
else: 
    print ( "Access Bloacked")