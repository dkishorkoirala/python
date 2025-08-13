username = "admin"
password = "admin@123"

try: 
    u = input("Enter username: ")
    p = input("Entere password: ")

    if not u or not p:
        raise ValueError("Username or password cannot be blank")
    
    if username == u and p == password:
        print("Login successful!")
    elif username == u and p != password:
        print("incorrect password")
    elif username != u and password == p:
        print("Check username")
    else:
        print("Incorrect credentials")
except ValueError as ve:
    print("Error:", ve)
except :
    print("something went wrong")
finally:
    print("End of attempt")