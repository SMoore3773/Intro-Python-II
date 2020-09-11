from room import Room
from player import Player
from item import Item
import sys
# Declare all the rooms
items = {
        'torch': Item("Torch","A smouldering torch, it gives off a dim light"),
        'candlestick': Item("Candlestick", "Did this kill Colonol Mustard in the kitchen?"),
        'watchglass': Item("Watchglass", "Could have been from pirates"),
        'tapestry': Item("Tapestry", "Mouldy tapestry, usually found in castles. Treasure hunters look at them. Have you seen it? "),
        'deblunes': Item("Coin", "TWO GOLD DEBLUNES! Hey, at least they're better than plastic...")
}
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons", items['torch']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",items['candlestick']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items['watchglass']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items['tapestry']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items['deblunes']),
}
# room['outside'].room_items.append(item['torch'])

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
# print(room)
# Make a new player object that is currently in the 'outside' room.

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

currentRoom = room['outside']
selection = ""
while True:
    
    player = Player("Guybrush", currentRoom, [])
    print(f"{player.name}, in the {currentRoom}")
    selection = input('\nChoose an action: [move] ([n]orth [s]outh [e]ast [w]est) , [i]ventory, [se]arch, [t]ake \n').split(' ')
    verb = selection[0]
    if len(selection) == 2:
        target = selection[1]
    if verb == 'q':
        print("Thank you for playing!")
        break
    if verb == 'se':
        currentRoom.search()
    if verb == 'i':
        player.inventory()
    if verb == 't' and len(selection) == 1:
        print("You flail wildly trying to take everything... maybe if you focused on what you wanted to take you might be more successful...\n")
    if verb == 't' and len(selection) > 1:
        player.take(currentRoom.room_items)
        currentRoom.room_items.on_take()
    if verb == 'move' and len(selection) == 1:
        print("Please choose a valid direction to move")
    if verb == 'move' and len(selection) == 2:
        try:
            
            if target == "n":
                if currentRoom.n_to is None:
                    print("\nYou can't move that way! Try another direction!\n")
                else:
                    currentRoom = currentRoom.n_to
            if target == 's':
                if currentRoom.s_to is None:
                    print("\nYou can't move that way, try another direction\n")
                else:
                    currentRoom = currentRoom.s_to
            if target == 'e':
                if currentRoom.e_to is None:
                    print("\nYou can't move that way, try another direction\n")
                else:
                    currentRoom = currentRoom.e_to
            if target == 'w':
                if currentRoom.w_to is None:
                    print("\nYou can't move that way, try another direction\n")
                else:
                    currentRoom = currentRoom.w_to
 
        except ValueError:
            print("please enter a valid direction to move (n , e, s, w)")
