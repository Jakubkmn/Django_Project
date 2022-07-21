from data import *
from start import *
from linked_list import SLL

start()

def insert_genres():
    movie_genre_list = SLL()
    for movie_genre in genre:
        movie_genre_list.insert_beginning(movie_genre)
    return movie_genre_list 

def insert_movies():
    movie_list = SLL()
    for movie_genre in genre:
        movie_sublist = SLL()
        for movie in movies:
            if movie[0] == movie_genre:
                movie_sublist.insert_beginning(movie)
        movie_list.insert_beginning(movie_sublist)
    return movie_list

my_genre_list = insert_genres()
my_movie_list = insert_movies()

selected_movie_genre = ""
