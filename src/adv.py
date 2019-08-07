from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.\
name = input("Enter Your Name: ")


player = Player(name, room["outside"])

# Write a loop that:

#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

#
# If the user enters "q", quit the game.
pi = ""

while pi != "q":
    print("NAME", player.name)
    print("ROOM", player.room.roomname)

    print("What Direction would you like to go?")
    direction = input("ENTER DIRECTION(N S E W or Q to quit): ").lower()
    if direction == "q":
        pi = "q"
        print("GameOver")
    elif player.room.roomname == "Outside Cave Entrance":
        if direction == "n":
            player.room.roomname = "foyer"
        elif direction != "n":
            print('MESSAGE: PICK A DIFFERENT DIRECTION')
    elif player.room.roomname == "foyer":
        if direction == "s":
            player.room.roomname = "Outside Cave Entrance"
        elif direction == "n":
            player.room.roomname = "overlook"
        elif direction == "e":
            player.room.roomname = "narrow"
        else:
            print('MESSAGE: PICK A DIFFERENT DIRECTION')
    elif player.room.roomname == "overlook":
        if direction == "s":
            player.room.roomname = "foyer"
        else:
            print('MESSAGE: PICK A DIFFERENT DIRECTION')
    elif player.room.roomname == "narrow":
        if direction == "w":
            player.room.roomname = "foyer"
        elif direction == "n":
            player.room.roomname = "treasure"
        else:
            print('MESSAGE: PICK A DIFFERENT DIRECTION')
    elif player.room.roomname == "treasure":
        if direction == "s":
            player.room.roomname = "narrow"
        else:
            print('MESSAGE: PICK A DIFFERENT DIRECTION')
