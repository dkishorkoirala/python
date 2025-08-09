class EnglishGreeter:
    def greet(self):
        print("Hello!")


class SpanishGreeter:
    def greet(self):
        print("¡Hola!")


for greet in [EnglishGreeter(), SpanishGreeter()]:
    greet.greet()
