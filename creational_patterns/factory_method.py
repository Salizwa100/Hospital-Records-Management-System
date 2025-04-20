
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Credit Card processed: ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"PayPal processed: ${amount}")

class PaymentFactory(ABC):
    @abstractmethod
    def create_processor(self):
        pass

class CreditCardFactory(PaymentFactory):
    def create_processor(self):
        return CreditCardProcessor()
