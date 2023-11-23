from project_01.caretaker import Caretaker
from project_01.cheetah import Cheetah
from project_01.keeper import Keeper
from project_01.lion import Lion
from project_01.tiger import Tiger
from project_01.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum = 0

        for worker in self.workers:
            sum += worker.salary

        if sum > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= sum

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum = 0

        for animal in self.animals:
            sum += animal.money_for_care

        if sum > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= sum

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        string = f"You have {len(self.animals)} animals\n"

        lions = [repr(x) for x in self.animals if isinstance(x, Lion)]
        string += f"----- {len(lions)} Lions:\n"
        string += '\n'.join(str(x) for x in lions) + '\n'

        tigers = [repr(x) for x in self.animals if isinstance(x, Tiger)]
        string += f"----- {len(tigers)} Tigers:\n"
        string += '\n'.join(str(x) for x in tigers) + '\n'

        cheetahs = [repr(x) for x in self.animals if isinstance(x, Cheetah)]
        string += f"----- {len(cheetahs)} Cheetahs:\n"
        string += '\n'.join(str(x) for x in cheetahs)

        return string.strip()

    def workers_status(self):
        string = f"You have {len(self.workers)} workers\n"

        keepers = [repr(x) for x in self.workers if isinstance(x, Keeper)]
        string += f"----- {len(keepers)} Keepers:\n"
        string += '\n'.join(str(x) for x in keepers) + '\n'

        caretakers = [repr(x) for x in self.workers if isinstance(x, Caretaker)]
        string += f"----- {len(caretakers)} Caretakers:\n"
        string += '\n'.join(str(x) for x in caretakers) + '\n'

        vets = [repr(x) for x in self.workers if isinstance(x, Vet)]
        string += f"----- {len(vets)} Vets:\n"
        string += '\n'.join(str(x) for x in vets)

        return string.strip()
