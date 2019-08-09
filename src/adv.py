from room import Room
from player import Player
from item import Item

# Declare all the rooms

items = [
    Item("sword", "sharp as can be."),
    Item("shovel", "Might be better for digging"),
    Item("rifle", "watch where you are shooting"),
    Item("flashlight", "bright as the sun"),
    Item("knife", "nice ole butterknife")
]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items[0]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items[1]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items[2]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items[3]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items[4]]),
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
    print("----------------------------------")
    print(player.room.roomname)
    print("DESC:", player.room.desc)
    print("----------------------------------")
    print("Inventory:", player.items)
    print("----------------------------------")
    if player.room.roomname == "Outside Cave Entrance":

        print("ITEMS: sword, sharp as can be")

    print("What Direction would you like to go?")
    direction = input("ENTER DIRECTION(N S E W or Q to quit): ").lower()
    if direction == "q":
        pi = "q"
        print("GameOver")
    elif player.room.roomname == "Outside Cave Entrance":
        if direction == "n":
            player.room.roomname = room['outside'].n_to
            player.room.items = player.room.items
        elif direction == "p":
            player.items.append("sword")
        elif direction != "n" and direction != "p":
            print('MESSAGE: PICK A DIFFERENT DIRECTION')
    elif player.room.roomname == room['outside'].n_to:
        if direction == "s":
            player.room.roomname = "Outside Cave Entrance"
        elif direction == "n":
            player.room.roomname = room['foyer'].n_to
        elif direction == "e":
            player.room.roomname = room['foyer'].e_to
        else:
            print('MESSAGE: PICK A DIFFERENT DIRECTION')
    elif player.room.roomname == room['foyer'].n_to:
        if direction == "s":
            player.room.roomname = room['overlook'].s_to
        else:
            print('MESSAGE: PICK A DIFFERENT DIRECTION')
    elif player.room.roomname == room['foyer'].e_to:
        if direction == "w":
            player.room.roomname = room['narrow'].w_to
        elif direction == "n":
            player.room.roomname = room['narrow'].n_to
        else:
            print('MESSAGE: PICK A DIFFERENT DIRECTION')
    elif player.room.roomname == room['narrow'].n_to:
        if direction == "s":
            player.room.roomname = room['narrow'].s_to
        else:
            print('MESSAGE: PICK A DIFFERENT DIRECTION')
