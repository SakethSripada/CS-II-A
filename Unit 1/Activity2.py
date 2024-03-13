with open("movies.txt", "r") as file:
    movies = file.readlines()

search_movie = int(input("Do you want to search for a movie? Enter a position number."))
if search_movie > len(movies):
    print("No movie exists at that position")
found_movie = (movies[search_movie-1])
if found_movie:
    print(found_movie)
see_if_movie = input("Type the name of a movie you want to search")
for index, movie in enumerate(movies, start=1):
    found_movie = movie.strip().lower()
    if found_movie == see_if_movie.strip().lower():
        print(f"The movie you entered, {see_if_movie} is present at position {index}!")
    elif not found_movie:
        print("Sorry. Movie does not exist in the file")
