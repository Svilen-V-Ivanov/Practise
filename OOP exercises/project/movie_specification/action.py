from project.assisting_functions import get_details
from project.movie_specification.movie import Movie
from project.user import User


class Action(Movie):
    AGE_RATING = 12

    def __init__(self, title: str, year: int, owner: User, age_restriction=None):
        self.age_restriction = age_restriction if age_restriction else self.AGE_RATING
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        #This specific change might break Judge logic so need to be careful if it should be here
        value = self.AGE_RATING if not value else value
        if value < self.AGE_RATING:
            raise ValueError(f"Action movies must be restricted for audience under {self.AGE_RATING} years!")
        self.__age_restriction = value

    def details(self):
        details = get_details(self.__class__.__name__, self.title, self.year,
                              self.age_restriction, self.likes, self.owner.username)
        return details
