##
# videogame_rater.py
# Rates videogames

def print_dictionary(dictionary):
    """
    Accepts a dictionary, loops through it and prints
    out the game and its rating
    """
    # outer dictionary
    for id, game in dictionary.items():
        print("Id: {} Game: {} \tRating: {}".format(id, game["name"],
                                                    game["rating"]))

if __name__ == "__main__":

    
    videogames = {1:{"name":"Minecraft", "rating":5},
                  2:{"name":"Call of duty", "rating":1},
                  3:{"name":"Angry birds","rating":4},
                  4:{"name":"Splatoon 2", "rating":5},
                  5:{"name":"Animal Crossing", "rating":4}}
    print_dictionary(videogames)

    # add , edit , delete, rate, functions

# Make a album rater program
# An album contains a title, artist, genre and rating
# You should allow the user to add, edit/modify, delte and rate the album
# When your rate a program, your prograum should recommend another album
# (any album of the same genre)
# You must make this program modular (functions)
# you SHOULD make this program robust
# You MUST HAVE FUN BUILDING THIS 
