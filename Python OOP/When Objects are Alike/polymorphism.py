class PaymentProcessor:
    def process_payment(self, amount: float):
        raise NotImplementedError("Subclasses must implement this method")


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing ${amount:.2f} via Credit Card.")


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing ${amount:.2f} via PayPal.")


# A single function that handles any PaymentProcessor child class
def checkout(processor: PaymentProcessor, amount: float):
    processor.process_payment(amount)


checkout(CreditCardProcessor(), 49.99)
checkout(PayPalProcessor(), 15.00)
