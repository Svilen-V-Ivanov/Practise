from project.customer import Customer
from project.dvd import DVD


def find_object(id, list):
    for person in list:
        if person.id == id:
            return person

    return None


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        person = find_object(customer_id, self.customers)
        dvd = find_object(dvd_id, self.dvds)

        #This if check might be unnecessary
        if person and dvd:
            for item in person.rented_dvds:
                if item.id == dvd_id:
                    return f"{person.name} has already rented {item.name}"

            if dvd.is_rented:
                return "DVD is already rented"

            if person.age < dvd.age_restriction:
                return f"{person.name} should be at least {dvd.age_restriction} to rent this movie"

            person.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{person.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        person = find_object(customer_id, self.customers)
        dvd = find_object(dvd_id, self.dvds)

        if person and dvd:
            for dvd in person.rented_dvds:
                if dvd.id == dvd_id:
                    dvd.is_rented = False
                    person.rented_dvds.remove(dvd)
                    self.dvds.append(dvd)
                    return f"{person.name} has successfully returned {dvd.name}"

            return f"{person.name} does not have that DVD"

    def __repr__(self):
        string = ''
        for person in self.customers:
            result = person.__repr__()
            string += result + '\n'

        for dvd in self.dvds:
            result = dvd.__repr__()
            string += result + '\n'

        return string.strip()
