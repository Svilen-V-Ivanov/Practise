class User:
    MIN_AGE = 6

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_AGE:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        value = ''
        value += f"Username: {self.username}, Age: {self.age}\n"
        value += "Liked movies:\n"

        if not self.movies_liked:
            value += "No movies liked.\n"
        else:
            for movie in self.movies_liked:
                value += f"{movie.details()}\n"

        value += "Owned movies:\n"

        if not self.movies_owned:
            value += "No movies owned.\n"
        else:
            for movie in self.movies_owned:
                value += f"{movie.details()}\n"

        return value.strip()
