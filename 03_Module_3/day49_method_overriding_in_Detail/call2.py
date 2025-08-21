class Payment:
    def process(self):
        print("Processing Payment...")


class CreditCardPayment(Payment):
    def process(self):
        print("Processing Credit Card Payment")


class PaypalPayment(Payment):
    def process(self):
        print("Processing Paypal Payment")


class securePaypalPayment(PaypalPayment):
    def process(self):
        super().process()
        print("Verifying user before Paypal Payment")


for n in [Payment, CreditCardPayment, PaypalPayment, securePaypalPayment]:
    n().process()
