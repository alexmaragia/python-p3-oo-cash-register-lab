#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._total = 0
        self.items = []
        self.last_transaction = 0
        self._discount = discount

    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self._total += item_total
        self.items.extend([title] * quantity)
        self.last_transaction = item_total

    def apply_discount(self):
        if self._discount > 0:
            discount_amount = self._total * (self._discount / 100)
            discounted_total = self._total - discount_amount
            self._total = discounted_total
            print(f"After the discount, the total comes to ${int(self._total)}.")
        else:
            print("There is no discount to apply.")
        return int(self._total)

    def void_last_transaction(self):
        if self.items:
            self._total -= self.last_transaction
            removed_item = self.items[-1]
            self.items = [item for item in self.items if item != removed_item]
            if self.items:
                self.last_transaction = 0  # Reset last transaction
            else:
                self.last_transaction = 0
                self._total = 0.0  # Set total to 0.0 if all items removed

    @property
    def total(self):
        return int(self._total) if self._total % 1 == 0 else self._total

    @total.setter
    def total(self, value):
        self._total = value

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value