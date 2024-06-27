# Movies Database Project
The Movies Database Project is a Python-based application designed to manage and display information about movies. Users can add, delete, update, and search for movies, as well as view various statistics and generate a website displaying the movie collection. The application fetches movie data from the OMDB API and stores it in a local JSON file.

# Features
 - List Movies: Display all movies in the database.
 - Add Movie: Add a new movie by fetching data from the OMDB API.
 - Delete Movie: Remove a movie from the database.
 - Update Movie: Update the rating and add notes to a movie.
 - Statistics: View average, median, highest, and lowest ratings.
 - Random Movie: Display a randomly selected movie.
 - Search Movie: Find movies by name.
 - Sort Movies by Rating: Display movies sorted by their ratings.
 - Generate Website: Create a static HTML page showcasing the movie collection.

# How to Run
Ensure Python is installed on your system.
Install required dependencies: requests, matplotlib, statistics.
Run the movies.py script to start the application. {python movies.py}

# Usage
Upon running the script, a menu will be displayed with options to manage the movies database. Users can interact with the application via command-line inputs to perform various operations.

 # Additional Details
The project uses the OMDB API to fetch movie data.
Movie information is stored in a local JSON file (data.json).
The generated website includes movie posters and links to their IMDb pages, with notes displayed on hover.

# Dependencies
 - Python 3.x
 - requests
 - matplotlib
 - statistics
