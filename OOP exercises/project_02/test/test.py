from project_02.movie import Movie
from unittest import main, TestCase


class MovieTests(TestCase):
    NAME = 'JAWS'
    YEAR = 1999
    OTHER_YEAR = 2001
    RATING = 8.5
    ACTOR = 'John Martin'
    SECOND_ACTOR = 'Jane Doe'

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test__if_correct_data_is_given__correctly_creates_object(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test__if_empty_name_is_given__raises_correct_error(self):
        name = ''
        expected_outcome = "Name cannot be an empty string!"

        with self.assertRaises(ValueError) as error:
            self.movie.name = name
        self.assertEqual(expected_outcome, str(error.exception))

    def test__if_invalid_year_is_given__raises_correct_error(self):
        expected_outcome = "Year is not valid!"
        with self.assertRaises(ValueError) as error:
            self.movie.year = 1880

        self.assertEqual(expected_outcome, str(error.exception))

    def test__add_actor__if_actor_not_in_list__expect_correct_output(self):
        expected_output = [self.ACTOR]
        self.movie.add_actor(self.ACTOR)

        self.assertEqual(expected_output, self.movie.actors)

    def test__add_actor__if_actor_not_in_empty_list__expect_correct_output(self):
        expected_output = [self.ACTOR, self.SECOND_ACTOR]
        self.movie.actors = [self.ACTOR]
        self.movie.add_actor(self.SECOND_ACTOR)

        self.assertEqual(expected_output, self.movie.actors)

    def test__add_actor__if_actor_in_list__expect_correct_output(self):
        self.movie.actors = [self.ACTOR]
        expected_outcome = f"{self.ACTOR} is already added in the list of actors!"
        actual_outcome = self.movie.add_actor(self.ACTOR)

        self.assertEqual(expected_outcome, actual_outcome)

    def test__if_comparing_and_first_movie_has_higher_score__expect_correct_output(self):
        other_movie = Movie('JAWS 2', self.OTHER_YEAR, 7.5)
        expected_outcome = f'"{self.movie.name}" is better than "{other_movie.name}"'
        actual_outcome = self.movie > other_movie
        self.assertEqual(expected_outcome, actual_outcome)

    def test_if_comparing_and_second_movie_has_higher_rating__expect_correct_output(self):
        other_movie = Movie('JAWS 2', self.OTHER_YEAR, 9.5)
        expected_outcome = f'"{other_movie.name}" is better than "{self.movie.name}"'
        actual_outcome = self.movie > other_movie

        self.assertEqual(expected_outcome, actual_outcome)

    def test__if_repr_is_called_and_actors__creates_correct_output(self):
        actors = [self.ACTOR, self.SECOND_ACTOR]
        self.movie.actors = actors
        expected_outcome = f"Name: {self.NAME}\n" \
                           f"Year of Release: {self.YEAR}\n" \
                           f"Rating: {self.RATING:.2f}\n" \
                           f"Cast: {', '.join(actors)}"
        actual_outcome = repr(self.movie)

        self.assertEqual(expected_outcome, actual_outcome)
