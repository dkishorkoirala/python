class Notifier:
    def notify(self):
        print("Sending basic notification...")


class EmailNotifier(Notifier):
    def notify(self):
        super().notify()
        print("Sending email notification...")


class SMSNotifier(Notifier):
    def notify(self):
        super().notify()
        print("Sending SMS notification...")


en = EmailNotifier()
en.notify()
print()
sn = SMSNotifier()
sn.notify()
