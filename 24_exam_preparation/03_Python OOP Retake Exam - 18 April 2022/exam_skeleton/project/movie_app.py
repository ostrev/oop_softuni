from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        user = User(username, age)
        if any(u.username == username for u in self.users_collection):
            raise Exception("User already exists!")
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if any(movie.title == m.title for m in self.movies_collection):
            raise Exception("Movie already added to the collection!")
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not any(movie.title == m.title for m in self.movies_collection):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = self.__find_user_by_username(username)
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        movie_title = movie.title
        if not any(movie.title == m.title for m in self.movies_collection):
            raise Exception(f"The movie {movie.title} is not uploaded!")

        user = self.__find_user_by_username(username)
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie_title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_list = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))
        result = ''
        for movie in sorted_list:
            result += movie.details()
            result += '\n'
        return result.strip()

    def __str__(self):
        result = ''
        if self.users_collection:
            result += f"All users: {', '.join(u.username for u in self.users_collection)}\n"
        else:
            result += "All users: No users.\n"
        if self.movies_collection:
            result += f"All movies: {', '.join(m.title for m in self.movies_collection)}\n"
        else:
            result += "All movies: No movies.\n"
        return result

    def __find_user_by_username(self, username):
        try:
            return [u for u in self.users_collection if u.username == username][0]
        except:
            raise Exception("This user does not exist!")
