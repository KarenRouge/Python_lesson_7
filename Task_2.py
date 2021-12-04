from abc import ABC


class Clothes(ABC):

    def __init__(self, number):
        self.number = number


    def fabric(self):
        pass

    def __str__(self):
        return str(self.number)


class Suit(Clothes):

    @property
    def fabric(self):
        fabric = self.number * 2 + 0.3
        return round(fabric, 2)


class Coat(Clothes):

    @property
    def fabric(self):
        fabric = self.number / 6.5 + 0.5
        return round(fabric, 2)

new_coat = Coat(42)
new_suit = Suit(173)

print(f"Количество ткани для пальто: {new_coat.fabric}")
print(f"Количество ткани для пальто: {new_suit.fabric}")