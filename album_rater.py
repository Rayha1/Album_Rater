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
    

def remove(index):
    """
    Deletes the key of the dictionary 
    """
    del albums[index] 
    # Does not change the id order of the dictionary list
    # There's an error when adding a new album, needs to be fixed 

def edit():
    """
    User can updates the details of album 
    """
    pass

def rate(index):
    """
    Updates rating dictionary with user's input 
    """
    albums[index]["rating"] = input('Please rate the album:')
    
def index():
    """
    Gets index of album selected by user and returns it 
    """
    index = int(input("Enter id of album: "))
    return index

def suggest():
    """
    Suggests another album based on the highest rating album's genre 
    """
    pass
    
def menu():
    """
    Loops menu 
    """
    menu = True
    while menu:
        option = input("\nAlbum rater"
                       "\n1) Add an album"
                       "\n2) Edit an album"
                       "\n3) Delete an album"
                       "\n4) Rate an album"
                       "\n5) Get a recommendation"
                       "\n6) Print albums"
                       "\n0) QUIT"
                       "\nEnter a option: ")
        if option == '1':
            add()
        elif option == '2':
            edit()
        elif option == '3':
            remove(index())
        elif option == '4':
            rate(index())
        elif option == '5':
            suggest()
        elif option == '6':
            print_dictionary(albums)
        elif option == '0':
            menu = False
        else:
            print("\nInvalid option")

if __name__ == "__main__":
    # Album Dictionary 
    albums = {1:{"title":"Album1", "artist": "Artist1", "genre": "pop", "rating":""},
              2:{"title":"Album2", "artist": "Artist2", "genre": "pop", "rating":""},
              3:{"title":"Album3", "artist": "Artist3", "genre": "rock", "rating":""},
              4:{"title":"Album4", "artist": "Artist4", "genre": "rock", "rating":""},
              5:{"title":"Album5", "artist": "Artist5", "genre": "jazz", "rating":""},
              6:{"title":"Album6", "artist": "Artist6", "genre": "jazz", "rating":""}}
    print_dictionary(albums)

    # Calls menu 
    menu()
