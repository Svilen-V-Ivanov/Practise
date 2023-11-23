from project_01.worker import Worker


class Vet(Worker):
    def __int__(self, name: str, age: int, salary: int):
        super().__init__(name, age, salary)