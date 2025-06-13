print("challenge 6: Sandwich builder")
#create a function make_sandwich() that takes any number of ingredients
#using *args and returns a summary of what's in the sandwich.

def make_sandwich(*ingre):
    ingredient = ", ".join(ingre)
    return f"Your sandwich is made up of: {ingredient}"

print(make_sandwich("bread", "cheese", "tomato", "lettuce"))

print("\nChallenge 7: Event RSVP Tracker")
#build a function rsvp() that accepts the name of the guest and any 
#number of keyword arguments for preferences (like food, seat, drink). use
#**kwargs

def rsvp(name, **preferences):
    print(f"{name} has RSVP's with preferences:")
    for key, value in preferences.items():
        print(f"{key}: {value}")

rsvp("Dibash", food="Vegetarian", seat="Window", drink="Juice")

print("\nchallenge 8: Custom Alert system")
#create create_alert(alert_type) which returns a different alert
#function (email_alert, sms_alert, push_alert) depending on what you
#pass

def create_alert(alert_type):
    def email_alert(msg): return f"Email: {msg}"
    def sms_alert(msg): return f"SMS: {msg}"
    def push_alert(msg): return f"Push Notification: {msg}"

    if alert_type == "email":
        return email_alert
    elif alert_type== "sms":
        return sms_alert
    elif alert_type == "push":
        return push_alert
    else:
        return lambda msg: f"Unknown alert: {msg}"

alert = create_alert("push")
print(alert("Your order has shipped!"))

print("\nchallenge - 9 : expense logger app")
#write log_expenses(name, *expenses, **meta) where *expenses are 
# numbers and **meta includes data, cateogory, etc.

def log_expenses(name, *expenses, **meta):
    total = sum(expenses)
    print(f"{name}'s total expenses: {total}")
    for k, v in meta.items():
        print(f"{k}: {v}")

log_expenses("Dibash", 120, 80, 45, category="Shopping", date="June 8")

print("\nchallenge 10: Guru calculator with history")
#create a function calculator_loger() that returns a function to add
#numbers, but also keeps a history of results.

def calculator_logger():
    history= []

    def calculator(*num):
        result = sum(num)
        history.append(result)
        return result, history
    return calculator

calc = calculator_logger()
print(calc(1, 2, 3))
print(calc(4, 5))

