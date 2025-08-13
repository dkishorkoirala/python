class Sender:
    def set_name(self, sender_name):
        self.sender_name = sender_name

    def send_message(self, receiver):
        print(f"{self.sender_name} is sending a message to {receiver.receiver_name}")

class Receiver:
    def set_name(self, receiver_name):
        self.receiver_name = receiver_name

    def read(self):
        print(f"{self.receiver_name} is reading the message")

s1 = Sender()
s1.set_name("Ram")

r1 = Receiver()
r1.set_name("Shyam")


r2 =Receiver()
r2.set_name("Hari")

s1.send_message(r1)
r1.read()

s1.send_message(r2)
r2.read()