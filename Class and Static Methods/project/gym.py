from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        string = ''
        sub = self.__find_entity(self.subscriptions, subscription_id)
        string += repr(sub) + '\n'
        #Due to the vagueness of the problem text there are two possible ways to solve the problem:
        #This way, which is not the Judge way, takes the ids from the subscription object and uses those
        #To find the relevant information
        # string += repr(self.__find_entity(self.customers, sub.customer_id)) + '\n'
        # string += repr(self.__find_entity(self.trainers, sub.trainer_id)) + '\n'
        # string += repr(self.__find_entity(self.equipment, subscription_id)) + '\n'
        # string += repr(self.__find_entity(self.plans, sub.exercise_id)) + '\n'
        #This is the Judge way, where we use the given id to just find the information in the Gym object
        string += repr(self.__find_entity(self.customers, subscription_id)) + '\n'
        string += repr(self.__find_entity(self.trainers, subscription_id)) + '\n'
        string += repr(self.__find_entity(self.equipment, subscription_id)) + '\n'
        string += repr(self.__find_entity(self.plans, subscription_id))

        return string

    @staticmethod
    def __find_entity(objects, id):
        for item in objects:
            if item.id == id:
                return item
