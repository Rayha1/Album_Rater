##
# album_rater.py
# made with collaboration with Rayha :))

# make a album rater program
# an album contains a title, artist, genre and rating
# you should allow the user to add, edit, delete and rate the album
# when you rate an album, your program should recomend another album
#(any album of the same genre)
# you must make this program modular (functions)
# you should use version control
# you SHOULD make this program robust
# YOU MUST HAVE FUN BUILDING THIS :)

def print_dictionary(dictionary):
    """
    Prints the album details in the dictionary tidy
    """
    for id, song in albums.items():
        print("ID:{}\ttitle:{}\tartist:{}\tgenre:{}\trating:{}"
              .format(id, song["title"],song["artist"], song["genre"],
              song["rating"]))

def add():
    """
    User adds new album details into the dictionary using update 
    """
    title = input("please enter the album name: ")
    artist = input("please enter the name of the artist: ")
    genre = input("please enter the song genre: ")
    num = len(albums)
    albums.update({num:{"title": title, "artist": artist, "genre": genre,
                        "rating": "" }})
    pass

def remove():
    """
    User removes an album from the dictionary 
    """
    pass

def edit():
    """
    User can updates all the details of album 
    """
    pass

def rate():
    """
    User rates each album in the dictionary
    """
    albums[index]["rating"] = input('please rate the album:')

def suggest():
    """
    Suggests another album based on the highest rating album's genre 
    """
    pass
    


if __name__ == "__main__":
    albums = {1:{"title":"Album1", "artist": "Artist1", "genre": "pop", "rating":""},
              2:{"title":"Album2", "artist": "Artist2", "genre": "pop", "rating":""},
              3:{"title":"Album3", "artist": "Artist3", "genre": "rock", "rating":""},
              4:{"title":"Album4", "artist": "Artist4", "genre": "rock", "rating":""},
              5:{"title":"Album5", "artist": "Artist5", "genre": "jazz", "rating":""},
              6:{"title":"Album6", "artist": "Artist6", "genre": "jazz", "rating":""}}
    print_dictionary(albums)
