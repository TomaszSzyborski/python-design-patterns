"""
Principle: Single Responsibility Principle

Rule:
A class should have only one reason to change (should have only one responsibility).
Class has one job to do. Each change in requirements for a given functionality can be done by changing just one class.

Example: Correct implementation where DebitCardManager manages card details and AccountManager manages account
balance operations.
"""
from decimal import Decimal
from enum import StrEnum, auto

from exceptions import InsufficientFundsException

ZERO_AMOUNT = Decimal('0')


class CardType(StrEnum):
    DEBIT = auto()
    CREDIT = auto()


class CardManager:
    def __init__(self, card_type: CardType):
        self._card_type: CardType = card_type
        self._card_numbers: list[str] = []

    def validate_card_number(self, card_number: str):
        if card_number in self._card_numbers:
            print("Card number found.")
        else:
            print("Card number not found. Please register your card.")

    def register_new_card(self, card_number: str):
        if card_number in self._card_numbers:
            print("Card number already exists.")
            return
        print("Adding card number to database.")
        self._card_numbers.append(card_number)


class Account:
    def __init__(self):
        self._account_balance: Decimal = Decimal()

    @property
    def balance(self):
        return self._account_balance

    def withdrawal(self, amount: Decimal):
        if (self._account_balance - amount) < ZERO_AMOUNT:
            print(f"Withdrawal cancelled. Insufficient funds on account.")
            raise InsufficientFundsException()
        self._account_balance -= amount
        print(f"Account balance after withdrawal: {self._account_balance}")

    def deposit(self, amount: Decimal):
        if amount <= ZERO_AMOUNT:
            print("Cannot deposit non-positive amount.")
            return
        self._account_balance += amount
        print(f"Account balance after deposit: {self._account_balance}")


class Client:
    def __init__(self, name):
        self.name = name
        self._account = Account()
        self.credit_cards = CardManager(CardType.CREDIT)
        self.debit_cards = CardManager(CardType.DEBIT)


if __name__ == '__main__':
    bam = Account()
    bam.deposit(Decimal(10))
    print(bam._account_balance)

    bam.withdrawal(Decimal(10))
    print(bam._account_balance)
    print(Decimal('0.2'))
