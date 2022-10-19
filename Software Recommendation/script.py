import data as dt
import start as st
from linked_list import SLL

st.start()

def insert_genres():
    movie_genre_list = SLL()
    for movie_genre in dt.genre:
        movie_genre_list.insert_beginning(movie_genre)
    return movie_genre_list 

def insert_movies():
    movie_list = SLL()
    for movie_genre in dt.genre:
        movie_sublist = SLL()
        for movie in dt.movies:
            if movie[0] == movie_genre:
                movie_sublist.insert_beginning(movie)
        movie_list.insert_beginning(movie_sublist)
    return movie_list

my_genre_list = insert_genres()
my_movie_list = insert_movies()

selected_movie_genre = ""

while len(selected_movie_genre) == 0:
    user_input = str(input("\nWhat genre of movies would you like to watch?\nType the beginning of that movie genre and press enter to see if "
        "it's here.\n")).lower()

    matching_genres = []
    genre_of_movies = my_genre_list.get_head_node()
    while genre_of_movies is not None:
        if str(genre_of_movies.get_value()).startswith(user_input):
            matching_genres.append(genre_of_movies.get_value())
        genre_of_movies = genre_of_movies.get_next_node()

    for genre in matching_genres:
        print(genre)

    if len(matching_genres) == 1:
        u_input = str(input("\nThe only matching genre for the specified input is " + matching_genres[0] + ". \nDo you want to look at " +
            matching_genres[0] + " movies? Enter y for yes and n for no\n")).lower()

        if u_input == 'y':
            selected_movie_genre = matching_genres[0]
            print('Selected movie genre' + selected_movie_genre)
            movie_list_head = my_movie_list.get_head_node()
            while movie_list_head.get_next_node() is not None:
                sublist = movie_list_head.get_value().get_head_node()
                if sublist.get_value()[0] == selected_movie_genre:
                    while sublist.get_next_node() is not None:
                        print("Title " + sublist.get_value()[1])
                        print("Release year " + sublist.get_value()[2])
                        print("Rating " + sublist.get_value()[3])
                        print("Runtime " + sublist.get_value()[4])
                        sublist = sublist.get_next_node()
                movie_list_head = movie_list_head.get_next_node()

            repeat = str(input("\nDo you want to find other restaurants? Enter y for yes and n for no.\n")).lower()
            if repeat == 'y':
                selected_movie_genre = ""