def div(userinput):
    while True:
        try:
            return float(input(userinput))
        except ValueError:
            print("Please enter valid numbers")
while True:
    try:       
        fnum = div("Enter first number: ")
        snum = div("Enter second number: ")

        result = round(fnum / snum,2)
        print("Result: ",result)
        break
    except ZeroDivisionError:
        print("You cannot divide by zero. Try again.")