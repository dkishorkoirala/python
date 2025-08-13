print("challenge 1: Counter Factory")
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter1 = make_counter()
print(counter1())
print(counter1())

counter2 = make_counter()
print(counter2())
print(counter2())

print("\nchallenge 2: power generator")
def make_power(base):
    def pow(num):
        return num ** base
    return pow

square = make_power(2)
print(square(5))

cube = make_power(3)
print(cube(2))

print("\nchallenge 3: secret keeper")
def secret_keeper(msg, password):
    def inner(password):
        if password == "open123":
            return f"Message: {msg}"
        else:
            return "Access Denied"
    return inner

my_secret = secret_keeper("the cake is a lie", password="open123")
print(my_secret("wrong"))
print(my_secret("open123"))
    
print("\nmini challenge 4")

def make_tag(tag):
    def wrapper(text):
        return f"<{tag}>{text}</{tag}>"
    return wrapper

bold = make_tag("b")
print(bold("Hello"))

print("\nmini-task: Temperature Converter factory")
def make_converter(to_celsius = True):
    def converter(num):
        if to_celsius == True:
            cel = round((num - 32)  / 1.8, 2)
            return cel
        else:
            fah = round((num * 1.8) + 32, 2)
            return fah
    return converter
    
to_c = make_converter(True)
print("converting to celcius: ",to_c(100))

to_f = make_converter(False)
print("Converting to Farhenheit: ",to_f(0))

print("\nchallenge 4: Running Total")
def running_total():
    total = 0
    def adding(nums):
        nonlocal total
        total += nums
        return total
    return adding

total = running_total()
print(total(5))
print(total(3))
print(total(10))

print("\nchallenge 5: logger factory")
def make_logger(level):
    def loggin(msg):
        print(f"[{level}]: {msg}")
    
    return loggin


info = make_logger("INFO")
error = make_logger("ERROR")

info("All systems normal")  
error("Something went wrong")   

print("\nchallenge 6: access locker")

def locker(correct_password):
    lock_state = "Locked"
    def toggle(input_password):
        nonlocal lock_state
        if input_password == correct_password:
            if lock_state == "Locked":
                lock_state = "Unlocked"
            else:
                lock_state = "Locked"
            return f"{lock_state}"
        else:
            return "Access Denied"
    
    return toggle

door = locker("admin")

print(door("wrong"))     
print(door("admin"))     
print(door("admin"))     