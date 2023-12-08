from project.assisting_functions import get_user, get_dict_items
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        for person in self.users_collection:
            if person.username == username:
                raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = get_user(username, self.users_collection)

        if not user:
            raise Exception("This user does not exist!")

        if movie.owner != user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = get_user(username, self.users_collection)
        if movie.owner != user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        get_dict_items(movie, kwargs)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = get_user(username, self.users_collection)
        if movie.owner != user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = get_user(username, self.users_collection)
        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = get_user(username, self.users_collection)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        output = '\n'.join(x.details() for x in sorted_movies)

        return output.strip()

    def __str__(self):
        string = ''

        if not self.users_collection:
            string += f"All users: No users.\n"
        else:
            string += f"All users: {', '.join(x.username for x in self.users_collection)}\n"

        if not self.movies_collection:
            string += f"All movies: No movies.\n"
        else:
            string += f"All movies: {', '.join(x.title for x in self.movies_collection)}\n"

        return string.strip()
