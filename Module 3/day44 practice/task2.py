class Ticket:
    ticket_id_counter = 0

    def __init__(self):
        Ticket.ticket_id_counter += 1
        self.id = Ticket.ticket_id_counter


t1 = Ticket()
t2 = Ticket()
t3 = Ticket()
print(t1.id)
print(t2.id)
print(t3.id)
