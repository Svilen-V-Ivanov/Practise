from project_01.animals.animal import Mammal


class Mouse(Mammal):
    VALID_FOOD = ['Vegetable', 'Fruit']
    WEIGHT_INCREASE = 0.10

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ not in self.VALID_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    VALID_FOOD = ['Meat']
    WEIGHT_INCREASE = 0.40

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ not in self.VALID_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    VALID_FOOD = ['Meat', 'Vegetable']
    WEIGHT_INCREASE = 0.30

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ not in self.VALID_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    VALID_FOOD = ['Meat']
    WEIGHT_INCREASE = 1.00

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ not in self.VALID_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity
