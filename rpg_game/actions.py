from map import ship
from enemies import enemies

"""Alta 3 RPG Final Project
   Patrick Haggerty"""
   #Actions scripts for the game

currentLocation = 'Starboard Passageway'
previousLocation = ''
inventory = []

def showInstructions():
    
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    Spooky Spaceship
    ========
    You wake up in an unknown room onboard the USG Reliant.

    Commands:
      go [direction](forward, aft, starboard, port)
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


def go(move):
    global currentLocation
    global previousLocation
    # if they type 'go' first
        # check that they are allowed wherever they want to go
    if move[1] in ship[currentLocation]:
         # set the current room to the new room
        previousLocation = currentLocation
        currentLocation = ship[currentLocation][move[1]]
        # there is no door (link) to the new room
        if(ship[currentLocation]['enemies']):
            combat(enemies[ship[currentLocation]['enemies']])
    else:
        print('You can\'t go that way!')


def get(move):
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

def combat(enemy):
    global currentLocation
    global previousLocation
    playerHealth = 50
    eDescription = enemy['description']
    eHealth = enemy['health']
    eDamage = enemy['damage']
    print(f'You look and see a {ship[currentLocation]["enemies"]} in the room.')
    print(eDescription)

    while eHealth > 0:
        print('What would you like to do? \n[attack] \n[use] \n[run]')
        action = ''
        while action == '':
            action = input('>')
        action = action.lower().split(" ", 1)

        # if they type 'go' first
        if action[0] == 'run':
            currentLocation = previousLocation
            return

        # if they type 'get' first
        if action[0] == 'attack':
            eHealth -= 5
            print('You attack the alien')
            print(f'The aliens health is now {eHealth}')
            playerHealth -= eDamage
            print(f'The alien attacks you, your health is now {playerHealth}')
    print('You killed the alien. It lies dead on the floor.')
    ship[currentLocation]['enemies'] = ''