import statistics
from random import choice
import matplotlib.pyplot as plt
import movie_storage

MENU = """
********** Movies Database **********
Menu:
0. Exit the Program
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Display Histogram
"""


def main():
    """Main function: contains the main menu operations of the program"""
    while True:
        print(MENU)
        try:
            user_choice = int(input("Enter your choice (0-9): "))

            menu_options = {
                0: exit_program,
                1: lambda: list_movies(movie_storage.get_movies()),
                2: add_movie,
                3: delete_movie,
                4: update_movie,
                5: get_movie_stats,
                6: random_movie_rating,
                7: search_movie,
                8: movie_rating_sort,
                9: display_histogram
            }
            if user_choice in menu_options:
                if user_choice == 5:
                    menu_options[user_choice](movie_storage.get_movies())
                else:
                    menu_options[user_choice]()
            else:
                print("Invalid Choice!!!")
        except ValueError:
            print("Please enter a valid number (between 0 - 9)")


def display_histogram(movies):
    """Function to draw and display a Histagram representation of the movies"""
    ratings = [details["rating"] for details in movies.values()]
    plt.hist(ratings, bins=10, edgecolor='black')
    plt.title('Histogram of Movie Ratings')
    plt.xlabel('Ratings')
    plt.ylabel('Frequency')
    plt.show()


def list_movies(movies):
    """Funtion to list the movies out"""
    for movie, details in movies.items():
        print(f"{movie} - Rating: {details['rating']} - Year: {details['year']}")


def total_movies(movies):
    """Funtion to sum up and list the movies out"""
    return len(movies)


def add_movie():
    """Funtion to add a movie to the list of movies"""
    try:
        movie_input = input("Please enter a movie to be added to the movie list: ")
        rating_input = float(input("Please enter a rating for the movie (1-10): "))
        if rating_input > 10 or rating_input < 1:
            print("Please enter a valid rating between 1 and 10")
            return

        year_input = int(input("Please enter the year of release: "))
        movie_storage.add_movie(movie_input, year_input, rating_input)
        print(f"{movie_input} is the new addition and its rating is: {rating_input}")
        print("Here is the updated list:")
        list_movies(movie_storage.get_movies())  # Display updated list after adding
    except ValueError:
        print("Invalid input! Please enter a valid movie rating and year.")


def delete_movie():
    """Funtion to delete a movie from the list"""
    try:
        delete_movie_input = input("Please enter a movie to be 'deleted' from the movie list: ").strip().lower()
        movie_storage.delete_movie(delete_movie_input)
        print(f"The movie '{delete_movie_input}' has been deleted!")
        print("Here is the updated list:")
        list_movies(movie_storage.get_movies())  # Display updated list to keep me sane
    except KeyError:
        print(f"The movie '{delete_movie_input}' is not in the list.")


def update_movie():
    """ Function to update the rating of a movie """
    try:
        title = input("Enter the movie title to update: ").strip().lower()
        rating = float(input("Enter the new rating (1-10): "))
        if rating < 1 or rating > 10:
            print("Rating should be between 1 and 10.")
            return

        movie_storage.update_movie(title, rating)
        print(f"Movie '{title}' rating updated to {rating}")
        print("Here is the updated list:")
        list_movies(movie_storage.get_movies())  # Display updated list after updating
    except ValueError:
        print("Invalid rating! Please enter a valid movie rating.")


def get_movie_stats(movies):
    """Movie statistics function, gets avg, med, highest and lowest"""
    ratings = [details["rating"] for details in movies.values()]
    # Average
    avg_rating = sum(ratings) / total_movies(movies)
    print(f"The Average Rating is: {avg_rating}")

    # Median
    median_rating = statistics.median(ratings)
    print("The Median Rating:", median_rating)

    # Best Rating
    best_rating = max(ratings)
    print(f"The Best Rating: {best_rating}")

    # Worst rating
    worst_rating = min(ratings)
    print(f"The Worst Rating: {worst_rating}")


def random_movie_rating():
    """ Random movie generation function """
    try:
        movies = movie_storage.get_movies()  # get the movie from movie.storage
        if not movies:
            print("No movies found in the database.")
            return

        random_movie = choice(list(movies.items()))
        print(
            f"Random movie: {random_movie[0]} - Rating: {random_movie[1]['rating']} - Year: {random_movie[1]['year']}")
    except Exception as e:
        print(f"Error: {e}")


def search_movie():
    """ Search movie function, input taken from the user """
    try:
        search_input = input("Enter part of movie name: ")
        movies = movie_storage.get_movies()

        search_results = []  # Initialize an empty list to store search results

        for name in movies.keys():
            if search_input.lower() in name.lower():
                search_results.append(name)

        if search_results:
            print("Result Matching")
            for result in search_results:
                print(result)
        else:
            print("No match was found for the entered movie!")
    except Exception as e:
        print(f"Error: {e}")


def movie_rating_sort():
    """Sort function"""
    try:
        movies = movie_storage.get_movies()
        sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
        print("Here is the sorted list, best first, worst last!")
        for movie, details in sorted_movies:
            print(f"{movie} - Rating: {details['rating']} - Year: {details['year']}")
    except Exception as e:
        print(f"Error: {e}")


def exit_program():
    """EXIT function"""
    print("Bye!")
    quit()


if __name__ == "__main__":
    main()
