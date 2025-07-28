class Tickets:
    tickets_counter = 1

    def __init__(self):
        self.number = Tickets.tickets_counter
        Tickets.tickets_counter += 1


t1 = Tickets()
t2 = Tickets()
print(t1.number)
print(t2.number)
