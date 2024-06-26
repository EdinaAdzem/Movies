import json


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.
    The function loads the information from the JSON
    file and returns the data.
    """
    with open('data.json', 'r') as handle:
        movies_data = json.load(handle)
    return movies_data


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open('data.json', 'w') as handle:
        json.dump(movies, handle, indent=4)


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    if title in movies:
        print(f"Movie '{title}' already exists!")
        return

    movies[title] = {"year": year, "rating": rating}
    save_movies(movies)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)
    else:
        print(f"Movie '{title}' is not in the database.")


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    if title in movies:
        movies[title]["rating"] = rating
        save_movies(movies)  # Save the updated movies database to file
    else:
        print(f"The movie '{title}' is not in the database.")
