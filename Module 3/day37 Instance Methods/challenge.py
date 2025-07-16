class Bot:
    def introduce(self):
        print(f"I am {self.name} and I will help you with {self.task}")

b1 = Bot()
b2 = Bot()

b1.name= "Alexa"
b2.name = "Google Assistant"

b1.task="Counting things"
b2.task="Finding things"

b1.introduce()
b2.introduce()