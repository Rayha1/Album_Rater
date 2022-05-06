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

    # Checks if there aren't albums in the dictionary
    if len(albums) < 1:
        print("\nYOU HAVE NO ALBUMS")
        print("press 1 to add an album")

    # For values and keys in dictionary prints out organised
    for id, song in albums.items():
        print("ID:{}\ttitle:{}\tartist:{}\tgenre:{}\trating:{}"
              .format(id, song["title"], song["artist"], song["genre"],
                      song["rating"]))


def add():
    """
    Takes user input album details as variables
    Updates into the dictionary
    """

    ADDED_ALBUM = 1

    # Gets user input of album details into variables
    title = check(input("please enter the album name: ")).title()
    artist = check(input("please enter the name of the artist: ")).title()
    genre = check(input("please enter the song genre: ")).title()

    # Finds the number ID
    num = len(albums) + ADDED_ALBUM

    # Updates into the dictionary
    albums.update({num: {"title": title, "artist": artist, "genre": genre,
                         "rating": ""}})

    print("Sucessfully added album")
    print("\n{} has been added to the album list!".format(title))


def check(length):
    """
    Checks the length of input and returns
    """

    NO_INPUT = 0
    while True:
        # Checks the length of the input for input
        if len(length) > NO_INPUT:
            return length
        else:
            # Error message because no input
            print("you have entered nothing")
            length = input("Please enter something:")


def remove(index):
    """
    Takes in the id index as the key
    Deletes the key of the dictionary
    """

    # deletes the index from the dictionary
    del albums[index]
    print("Sucessfully removed album ID {}".format(index))


def edit(index):
    """
    User can updates the details of album
    """

    # Gets user input of fixed album details as variables
    title = input("please enter the fixed album name: ").title()
    artist = input("please enter the fixed name of the artist: ").title()
    genre = input("please enter the fixed song genre: ").title()

    # Updates into dictionary
    albums.update({index: {"title": title, "artist": artist,
                           "genre": genre, "rating": ""}})

    print("Album {} has been edited".format(index))


def rate(index):
    """
    Takes in index of the selected album
    Updates the rating that album in the dictionary
    """

    RATING_MIN = 1
    RATING_MAX = 10

    user_rating = True
    # Loop
    while user_rating:

        # Asks for user input rating
        rating = int(input('Please rate the album out of 10:'))

        # Checks if rating isn't in range from 1-10
        if rating < RATING_MIN or rating > RATING_MAX:
            print("Rating must be from 1-10")

        else:
            # Adds the rating into dictionary
            albums[index]["rating"] = rating

            print("Rating added")
            print("You have rated album ID {}, {}".format(index, rating))

            # Breaks loop
            user_rating = False

    # Suggests another album to user
    genre = albums[index]["genre"]
    flag = True
    suggest(genre, flag)


def index():
    """
    Gets user input index of album selected
    Returns it
    """

    # Loop
    while True:
        try:

            # Gets user input of album id and stores as index
            index = int(input("Enter id of album: ")
                        )
            # Checks if it is a valid id in the dictionary
            if index in albums:
                return index

            # Album Id isn't in dictionary
            else:
                print("Please enter the ID(number)of album")

        except ValueError:
            print("Invalid input. Please enter the ID(number)of album")


def suggest(reccomend, flag):
    """
    Suggests another album the the same genere as the one rated
    """

    suggesting = flag
    while suggesting:

        # Loops through the indexs and generes in albums dictionary
        for index, genre in albums.items():

            # If genre matches the one rated
            if albums[index]["genre"] == reccomend:

                # Stores the album matching the genre as the recommendation
                reccomendation = albums[index]["title"]
                suggesting = False
                recc = True

    if recc is True:

        # Suggests the recomended album
        print("You might like album {}".format(reccomendation))

    else:
        # No genre of the same rated
        print("This song has a genre not on the list\n"
              "So we cannot reccomend you anyhting")


def menu():
    """
    Prints out menu
    """

    # Prints out menu tidy
    print("\nAlbum rater"
          "\n1) Add an album"
          "\n2) Edit an album"
          "\n3) Delete an album"
          "\n4) Rate an album"
          "\n5) Print albums"
          "\n0) QUIT")


# Main Routine
if __name__ == "__main__":

    # Album Dictionary
    albums = {}

    # Checks if there are albums in dictionary
    ALBUM_MIN = 0

    # Prints album details nicely
    print_albums(albums)

    program = True
    # Loops menu/program
    while program:

        # Calls menu
        menu()

        # Asks user for input for what to do
        option = input("\nPlease enter a number option from the menu: ")

        if option == '1':
            # User adds a album
            add()

        elif option == '2':
            # If dictionary has albums, takes the id and edits it
            if len(albums) > ALBUM_MIN:
                num = index()
                edit(num)

            # If dictionary empty
            else:
                print("\nYOU HAVE NO ALBUMS")
                print("press 1 to add an album")

        elif option == '3':
            # If there are albums and removes it
            if len(albums) > ALBUM_MIN:
                num = index()
                remove(num)

            # If dictionary empty
            else:
                print("\nYOU HAVE NO ALBUMS")
                print("press 1 to add an album")

        elif option == '4':
            # Takes in index of a album and user rates it
            if len(albums) > ALBUM_MIN:
                num = index()
                rate(num)

            # If dictionary empty
            else:
                print("\nYOU HAVE NO ALBUMS")
                print("press 1 to add an album")

        elif option == '5':
            # Prints out album details nicely
            print_albums(albums)

        elif option == '0':
            # Breaks loop/menu
            print("Thankyou for using album rater :) goodbye")
            program = False

        else:
            # Invalid input
            print("\nInvalid option, please select from the menu")
