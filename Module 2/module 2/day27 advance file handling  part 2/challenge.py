from datetime import datetime

mess = input("Enter any message: ")
ts = datetime.now().strftime("%Y-%m-%d  %H-%M-%S")
log = f"{ts} - {mess}\n"

with open("logbook.txt", "a") as f:
    f.write(log)
print("Log saved...")