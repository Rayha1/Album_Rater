##
# album_rater.py
# Album rater program that allows user to add, edit, delete, rate albums
# Made with collaboration with Rayha :))
# 03/05/22 


def print_albums(dictionary):
    """
    Takes in the dictionary
    Prints the album details nicely in the dictionary 
    """
    # For values and keys in dictionary prints out organised
    for id, song in albums.items():
        print("ID:{}\ttitle:{}\tartist:{}\tgenre:{}\trating:{}"
              .format(id, song["title"],song["artist"], song["genre"],
              song["rating"]))

def add():
    """
    Takes user input album details as variables
    Updates into the dictionary 
    """
    # Gets user input of album details into variables
    title = input("please enter the album name: ").title()
    artist = input("please enter the name of the artist: ").title()
    genre = input("please enter the song genre: ").title()

    # Finds the number ID 
    num = len(albums)+1

    # Updates into the dictionary
    albums.update({num:{"title": title, "artist": artist, "genre": genre,
                        "rating": "" }})
    
    print("Sucessfully added album")
    

def remove(index):
    """
    Takes in the id index as the key
    Deletes the key of the dictionary 
    """
    del albums[index]
    print("Sucessfully removed album")

def edit(index):
    """
    User can updates the details of album 
    """
    title = input("please enter the fixed album name: ").title()
    artist = input("please enter the fixed name of the artist: ").title()
    genre = input("please enter the fixed song genre: ").title()
    albums.update({index:{"title": title, "artist": artist,
                          "genre": genre, "rating": "" }})

def rate(index):
    """
    Takes in index of the selected album
    Updates the rating that album in the dictionary 
    """
    user_rating = True
    while user_rating:
        rating = int(input('Please rate the album out of 10:'))

        if rating < 1 or rating > 11:
            print("Rating must be from 1-10")
        else:
            albums[index]["rating"] = rating
            print("Rating added")
            user_rating = False 
    
def index():
    """
    Gets user input index of album selected 
    Returns it 
    """
    while True:
        index = int(input("Enter id of album: "))
        if index in albums:
            return index
        else:
            print("please enter the ID number(number)of an album")

def suggest():
    """
    Suggests another album based on the highest rating album's genre 
    """
    
    pass
    
def menu():
    """
    Prints out menu
    """
    # Prints out menu 
    print("\nAlbum rater"
          "\n1) Add an album"
          "\n2) Edit an album"
          "\n3) Delete an album"
          "\n4) Rate an album"
          "\n5) Get a recommendation"
          "\n6) Print albums"
          "\n0) QUIT")


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

    # Loops menu
    while True:
        
        # Calls menu 
        menu()

        # Asks user for input for what to do 
        option = int(input("\nPlease enter a number option from the menu: "))
        
        if option == 1:
            # User adds a album
            add()

        elif option == 2:
            # User edits a album
            num = index()
            edit(num)

        elif option == 3:
            # Takes in index of a album and removes it
            num = index()
            remove(num)

        elif option == 4:
            # Takes in index of a album and user rates it
            num = index()
            rate(num)

        elif option == 5:
            # Suggests a album(havn't done yet)
            suggest()

        elif option == 6:
            # Prints out album details nicely 
            print_albums(albums)

        elif option == 0:
            # Breaks loop/menu
            print("bye")
            exit()

        else:
            # Invalid input 
            print("\nInvalid option")
