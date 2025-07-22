class Conenction:
    def __init__(self):
        print("Connected to server")
        
    def __del__(self):
        print("Disconnected")
        
c = Conenction()
d = Conenction()
e = Conenction()

del c 