class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    #This autoincrements the user id for the future user, since it returns the id for the current user before increment
    @staticmethod
    def get_next_id():
        result = Customer.id
        Customer.id += 1
        return result

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"