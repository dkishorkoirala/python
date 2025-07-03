import os
from datetime import datetime

m = input("Enter any message: ")
time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

message = f"{time_stamp} - {m}\n"

if os.path.exists("daily_logs.txt"):
    file = open("daily_logs.txt", "a")

else:
    file = open("daily_logs.txt", "w")

file.write(message)
file.close()
print("Writing successful!!!")