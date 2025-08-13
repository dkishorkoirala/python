#task 1:
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number...")
else:
    if x % 2 == 0 :
        print("Even")
    else:
        print("Odd")

#task 2:
try:
    file = open("intro.txt", "r" )
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    #file.close()
    print("file closed successfully")

#task 3:
try:
    x = int(input("Enter a number: "))
    try:
        y = int(input("Enter second number: "))
        print(x/y)
    except ValueError:
        print("not a number")
    except ZeroDivisionError:
        print("Number cannot be zero")
except ValueError:
    print("not a valid number")
except:
    print("something went wrong")