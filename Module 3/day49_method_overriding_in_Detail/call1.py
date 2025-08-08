class Notifier:
    def notify(self):
        print("Base notification")


class EmailNotifier(Notifier):
    def notify(self):
        print("Email Message Sent")


class SMSNotifier(Notifier):
    def notify(self):
        print("SMS Message Sent")


class AppNotifier(Notifier):
    def notify(self):
        super().notify()
        print("App Notification Sent")


for n in [Notifier(), EmailNotifier(), SMSNotifier()]:
    n.notify()

a = AppNotifier()
a.notify()
