from map import ship
from controller import gameLoop

currentLocation = 'Starboard Passageway'
inventory = []

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    You wake up in an unknown room onboard the USG Reliant.

    Commands:
      go [direction]
      get [item]
    ''')


def showStatus():
    """determine the current status of the player"""
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentLocation,
          '\n' + ship[currentLocation]['description'])
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in ship[currentLocation]:
        print('You see a ' + ship[currentLocation]['item'])
    print("---------------------------")


def go():
    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in ship[currentLocation]:
            # set the current room to the new room
            currentLocation = ship[currentLocation][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')


def get():
    # if the room contains an item, and the item is the one they want to get
    if "item" in ship[currentLocation] and move[1] in ship[currentLocation]['item']:
        # add the item to their inventory
        inventory += [move[1]]
        # display a helpful message
        print(move[1] + ' got!')
        # delete the item from the room
        del ship[currentLocation]['item']
    # otherwise, if the item isn't there to get
    else:
        # tell them they can't get it
        print('Can\'t get ' + move[1] + '!')
