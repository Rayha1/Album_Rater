##
# album_rater.py
# Album rater program that allows user to add, edit, delete, rate albums
# made with collaboration with Sydney :))
##
# made with collaboration with Rayha :))
# 03/05/22 

# make a album rater program
# an album contains a title, artist, genre and rating
# you should allow the user to add, edit, delete and rate the album
# YOU MUST HAVE FUN BUILDING THIS :)


def print_dictionary(dictionary):
    """
    Takes in the dictionary
    Prints the album details nicely in the dictionary 
    Prints the album details in the dictionary tidy
    """
    if len(albums) < 1:
        print("\nYOU HAVE NO ALBUMS")
        print("press 1 to add an album")
    for id, song in albums.items():
        print("ID:{}\ttitle:{}\tartist:{}\tgenre:{}\trating: {}".format(id, song["title"],
                                                                         song["artist"], song["genre"], song["rating"]))

def add():
    """
    Takes user input album details as variables
    Updates into the dictionary 
    User adds new album details into the dictionary using update 
    """
    title = input("please enter the album name: ").strip().title()
    artist = input("please enter the name of the artist: ").srip().title()
    genre = input("please enter the song genre: ").strip().lower()
    num = len(albums)+1
    albums.update({num:{"title": title, "artist": artist, "genre": genre, "rating": "" }})
    print("\n{} has been added to the album list!".format(title))

def remove(index):
    """
    Takes in the id index as the key
    Deletes the key of the dictionary 
    User removes an album from the dictionary 
    """
    del albums[index] 

    
def edit(index):
    """
    User can updates the details of album 
    User can updates all the details of album 
    """
    title = input("please enter the fixed album name: ")
    artist = input("please enter the fixed name of the artist: ")
    genre = input("please enter the fixed song genre: ")
    albums.update({index:{"title": title, "artist": artist, "genre": genre, "rating": "" }})


def rate(index):
    """
    Gets user input index of album selected 
    Returns it 
    User rates each album in the dictionary
    """
    while True:
        rating = int(input('please rate the album from 1 to 10:'))
        if rating < 1 or rating > 10:
            print("invalid number")
        else:
            albums[index]["rating"] = rating
            print("you have rated the album {}".format(rating))
            break
        
    genre = albums[index]["genre"]
    flag = True
    suggest(genre, flag)


def suggest(reccomend, flag):
    """
    Suggests another album based on the highest rating album's genre 
    """
    suggesting = flag
    while suggesting:
        for index, genre in albums.items():
            if albums[index]["genre"] == reccomend:
                reccomendation = albums[index]["title"]
                suggesting = False
                recc = True
                
    if recc == True:
        print("you might like {}".format(reccomendation))
    else:
        print("this song has a genre no on the list\n"
              "so we cannot reccomend you anyhting")
        

def index():
    while True:
        try:
            index = int(input("Enter id of album: "))
            if index in albums:
                return index
        except ValueError:
            print("please enter the ID number(number)of an album")

def menu():
    """
    Loops menu 
    """
    # Prints out menu and asks for user input
    print("\nAlbum rater"
          "\n1) Add an album"
          "\n2) Edit an album"
          "\n3) Delete an album"
          "\n4) Rate an album"
          "\n5) Print albums"
          "\n0) QUIT"
          "\nEnter a option: ")

# Main Routine
if __name__ == "__main__":

    # Album Dictionary 
    albums = {1:{"title":"Album1", "artist": "Artist1", "genre": "pop", "rating":""},
              2:{"title":"Album2", "artist": "Artist2", "genre": "pop", "rating":""},
              3:{"title":"Album3", "artist": "Artist3", "genre": "rock", "rating":""},
              4:{"title":"Album4", "artist": "Artist4", "genre": "rock", "rating":""},
              5:{"title":"Album5", "artist": "Artist5", "genre": "jazz", "rating":""},
              6:{"title":"Album6", "artist": "Artist6", "genre": "jazz", "rating":""}}

    # Calls menu 
    while True:
        menu()
        option = int(input("please enter a number from the menu: "))
        if option == 1:
            # User adds a album
            add()


        elif option == 2:
            # User edits a album
            num = index()
            edit(num)

        elif option == 3:
            # Takes in index of a album and removes it
            if len(albums) > 0:
                num = index()
                remove(num)
            else:
                print("\nYOU HAVE NO ALBUMS")
                print("press 1 to add an album")
                

        elif option == 4:
            # Takes in index of a album and user rates it
            num = index()
            rate(num)

        elif option == 5:
            # Prints out album details nicely 
            print_dictionary(albums)

        elif option == 0:
            # Breaks loop/menu
            print("bye")
            exit()

        else:
            # Invalid input 
            print("\nInvalid option")
