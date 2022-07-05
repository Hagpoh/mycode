#Controller script for the rpg game
import actions

actions.showInstructions()

# loop forever
def gameLoop():
    while True:
        actions.showStatus()

        move = ''
        while move == '':
            move = input('>')
        move = move.lower().split(" ", 1)

        # if they type 'go' first
        if move[0] == 'go':
            actions.go(move)

        # if they type 'get' first
        if move[0] == 'get':
            actions.get(move)