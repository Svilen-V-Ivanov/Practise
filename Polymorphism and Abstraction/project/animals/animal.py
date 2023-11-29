from abc import ABC, abstractmethod


class Animal(ABC):
    VALID_FOOD = ['Meat', 'Vegetable', 'Fruit', 'Seed']
    WEIGHT_INCREASE = 0

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Bird(Animal):
    def __init__(self, name: str, weight: float, wing_size: float):
        self.wing_size = wing_size
        super().__init__(name, weight)

    def make_sound(self):
        pass

    def feed(self, food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name: str, weight: float, living_region: str):
        self.living_region = living_region
        super().__init__(name, weight)

    def make_sound(self):
        pass

    def feed(self, food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"