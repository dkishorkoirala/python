print("challenge 1: flexible shopping list")
#write a function shopping_list() that takes any number of items and 
#return them as list

def shopping_list(*items):
    return list(items)

print(shopping_list("milk", "Eggs", "Rice"))

print("\nchallenge 2: personalized Email Generator")
#create a fucntion email_template() that accepts keyword details like
#name, product, and delivery_date and formats a message.

def email_temlate(**kwargs):
    name = kwargs.get("name", "customer")
    producer = kwargs.get("producer", "Producer")
    deliver_date = kwargs.get("delivery_date", "date")

    return f"Hello {name},\nYour {producer} will be delivered by {deliver_date}."
   
print(email_temlate(name = "Dibash", producer="Laptop", deliver_date= "June 15"))


print("\nchallenge 3: Advanced calculator with *args")
#create a function multiply_all() that multiplies all numbers passed
#using *args

def multiply_all(*args):
    total = 1
    for num in args:
        total *= num
    return total

print(multiply_all(2, 3, 4))

print("\nchallenge 4: fitness progress tracker")
#create a track_progress() function that takes name and any number of keywords stats like 
#pushups= 50 , squarts = 70 and print them.

def track_progress(**kwargs):
    name = kwargs.get("name", "Customer")
    pushups = kwargs.get("pushups", "please enter pushups")
    squats = kwargs.get("squats", "please enter squats")
    running_km = kwargs.get("running_km", "Please enter running km")
    
    return f"{name}'s progress:\nPushups: {pushups}\nSquats: {squats}\nrunning_km: {running_km}"

print(track_progress(name="Kishor", pushups=50, squats=70, running_km=2))


print("\nChallenge 5: Combine *args + **kwargs")\
#write a function log_user_activity() that takes a username , 
#any number of actions (*args), and details like device , location(**kwargs)

def log_user_activity(username, *args, **kwargs):
    actions = ", ".join(args)
    print(f"{username} did: {actions}")
            

    print("Details:")
    device = kwargs.get("device", "deviceName")
    location = kwargs.get("location", "location not found")
    return f"device: {device}\nLocation: {location}"

print(log_user_activity("Dibash", "Logged In", "Viewed Course", device="Laptop", location="Nepal"))


print("\nbonus guru-level: function that returns another function")
def choose_math_op(operation):
    def add(a, b): return a+ b
    def sub (a,b ): return a-b
    def mul (a,b ): return a*b

    if operation == "add":
        return add
    elif operation == "sub":
        return sub
    elif operation == "mul":
        return mul
my_op = choose_math_op("mul")
print(my_op(3,4))