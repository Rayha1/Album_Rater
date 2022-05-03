##
# album_rater.py
# Album rater program that allows user to add, edit, delete, rate albums
# made with collaboration with Rayha :))
# 03/05/22 


def print_albums(dictionary):
    """
    Takes in the dictionary
    Prints the album details nicely in the dictionary 
    """
    for id, song in albums.items():
        print("ID:{}\ttitle:{}\tartist:{}\tgenre:{}\trating:{}"
              .format(id, song["title"],song["artist"], song["genre"],
              song["rating"]))

def add():
    """
    Takes user input album details as variables
    Updates into the dictionary 
    """
    title = input("please enter the album name: ")
    artist = input("please enter the name of the artist: ")
    genre = input("please enter the song genre: ")
    num = len(albums)
    albums.update({num:{"title": title, "artist": artist, "genre": genre,
                        "rating": "" }})
    

def remove(index):
    """
    Takes in the id index as the key
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
    Takes in index of the selected album
    Updates the rating that album in the dictionary 
    """
    albums[index]["rating"] = input('Please rate the album:')
    
def index():
    """
    Gets user input index of album selected 
    Returns it 
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

        # Prints out menu and asks for user input
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
            # User adds a album
            add()

        elif option == '2':
            # User edits a album 
            edit()
            
        elif option == '3':
            # Takes in index of a album and removes it
            remove(index())
            
        elif option == '4':
            # Takes in index of a album and user rates it
            rate(index())
            
        elif option == '5':
            # Suggests a album(havn't done yet)
            suggest()
            
        elif option == '6':
            # Prints out album details nicely 
            print_albums(albums)
            
        elif option == '0':
            # Breaks loop/menu
            menu = False
            
        else:
            # Invalid input 
            print("\nInvalid option")

# Main Routine
if __name__ == "__main__":
    
    # Album Dictionary 
    albums = {1:{"title":"Album1", "artist": "Artist1", "genre": "pop", "rating":""},
              2:{"title":"Album2", "artist": "Artist2", "genre": "pop", "rating":""},
              3:{"title":"Album3", "artist": "Artist3", "genre": "rock", "rating":""},
              4:{"title":"Album4", "artist": "Artist4", "genre": "rock", "rating":""},
              5:{"title":"Album5", "artist": "Artist5", "genre": "jazz", "rating":""},
              6:{"title":"Album6", "artist": "Artist6", "genre": "jazz", "rating":""}}

    # Prints album details nicely 
    print_albums(albums)

    # Calls menu 
    menu()
