class Logger:
    def log_message(self):
        print("[Base] logging data...")


class FileLogger(Logger):
    def log_message(self):
        super().log_message()
        print("Saving Log to file...")


f1 = FileLogger()
f1.log_message()
