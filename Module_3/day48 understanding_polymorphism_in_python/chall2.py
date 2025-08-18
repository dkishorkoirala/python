class Notification:
    def send(self):
        print("Sending notification...")


class EmailNotification(Notification):
    def send(self):
        super().send()
        print("Sending email notification...")


class SMSNotification(Notification):
    def send(self):
        super().send()
        print("Sending SMS notification...")


class PushNotification(Notification):
    def send(self):
        super().send()
        print("Sending Push notification...")


def send_alert(notification):
    notification.send()
    print()


for n in [EmailNotification(), SMSNotification(), PushNotification()]:
    send_alert(n)
