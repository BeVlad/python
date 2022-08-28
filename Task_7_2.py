from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def get_coat_consumption(self):
        pass

    @abstractmethod
    def get_suit_consumption(self):
        pass

    def get_total_consumption(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.coat_consumption = self.v / 6.5 + 0.5
        self.suit_consumption = self.h * 2 + 0.3

    def get_coat_consumption(self):
        return str(f'Fabric consumption per coat: {self.coat_consumption:.2f}')

    def get_suit_consumption(self):
        return str(f'Fabric consumption per suit: {self.suit_consumption:.2f}')

    @property
    def get_total_consumption(self):
        return str(f'Total: {self.coat_consumption + self.suit_consumption:.2f}')


clothes = Clothes(8, 103)

print(clothes.get_coat_consumption())
print(clothes.get_suit_consumption())
print(clothes.get_total_consumption)