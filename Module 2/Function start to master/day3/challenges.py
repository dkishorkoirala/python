print("Challenge1 personalized workout plan")

def wp(name, morning="Jogging", afternoon= "Yoga", evening= "Stretching"):
    return f"{name}'s Workout Plan: Morning- {morning}, Afternoon- {afternoon}, Evening- {evening}"

print(wp("Dibash"))
print(wp(name= "Kishor", morning="Yoga", afternoon= "Stretching", evening= "Jogging"))

print("\nChallenge 2 : movie night plan")

def mn (name, movie = "Inception", scnaks= "Popcorn", drinks= "Cola"):
    return f"{name}'s Movie night: Watching {movie} with {scnaks} and {drinks}"

print(mn("Dibash"))
print(mn(name= "Kishor", movie="Titanic", scnaks= "Pizza", drinks= "Fanta"))

print("\nchallenge 3: Study Schedule Generator")
def ss(name, subject= "Python", duration="3 hours", time = "12 pm"):
    return f"{name}'s Study Schedule: Studying {subject} for {duration} at {time}"

print(ss("Dibash"))
print(ss(name= "Kishor", subject= "Web development", duration="2 hours", time= "10 am"))

print("\nbonus : Guruji feedback BOT")

def gf(name, effort):
    if effort >= 9:
        return f"{name}, you're a True yogi of code"
    elif effort >= 5:
        return f"{name}, you can do better keep the heat on <3"
    else:
        return f"{name}, Even the slowest walker is also the winner dont forget to walk."

name = input("Enter Your name: ")
effort = int(input("Enter your effort level: "))
print(gf(name, effort))

print("\nChallenge 4: Build a travel itinerary Function")
def tm(name, city = "kathmandu", days = 3, activities = "Temple Visit"):
    return f"{name}'s Travel Plan: Visiting {city}, for {days} days with {activities} activity"

print(tm("Dibash"))
print(tm(name= "Kishor", city="Pokhara", days= 5, activities="Hike"))

print("\nChallenge 5: Build a simple tax calculator")
def tx(income, tax_rate= 0.15):
    tax = income * tax_rate
    return f"Your tax for {income} with rate of {tax_rate} is: {tax:.2f}"

income = int(input("Enter tax amount: "))
print(tx(income))
income = int(input("Enter tax amount: "))
rate = float(input("Tax rate in decimal value: "))
print(tx(income, rate))


print("\nChallenge 6: Build a Greeting Generator Based on Time")
def gu(name, time = "morning"):
    if time == "morning":
        return f"Good morning {name}!"
    elif time == "afternoon":
        return f"Good afternoon {name}!"
    elif time == "evening":
        return f"Good evening {name}!"
    else:
        return f"Hello {name}!"

name = input("Enter Your name: ").capitalize()
time = input("Enter time of day: ").strip().lower()
print(gu(name, time))

print("\nchallenge 7 :Mood-based Playlist Generator")
def mp(name, mood= "happy"):
    if mood == "happy":
        return f"{name}'s Playlist: playing upbeats pop and dance tracks!"
    elif mood == "sad":
        return f"{name}'s Playlist: playing mellow and calming music to lift your mood"
    elif mood == "angry":
        return f"{name}'s Playlist: playing intense , rock and energetic tracks to get pumped up"
    else:
        return f"{name}'s Playlist: playing a mix of all genres to keep you entertained"

n = input("Enter your name: ").capitalize()
m = input("Enter your mood(happy/sad/angry or anything): ").strip().lower()
print(mp(n, m))