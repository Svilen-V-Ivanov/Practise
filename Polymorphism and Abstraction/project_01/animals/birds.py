from project_01.animals.animal import Bird


class Owl(Bird):
    VALID_FOOD = ['Meat']
    WEIGHT_INCREASE = 0.25

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ not in self.VALID_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    VALID_FOOD = ['Meat', 'Vegetable', 'Fruit', 'Seed']
    WEIGHT_INCREASE = 0.35

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if food.__class__.__name__ not in self.VALID_FOOD:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += self.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity
