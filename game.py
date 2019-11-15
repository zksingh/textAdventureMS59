from player import Player #to be implemented 
import world #to be implemented 

def play(): #create game loop 
    print("Escape from Cave Terror!") #change to my title
    player = Player() #create new player instance
    while True: # while true
        room = world.tile_at(player.x, player.y) #create a variable called room and set it to the current location of the player
        print(room.introText()) #print the appropriate tile's intro text
        actionInput = getPlayerCommand() 

        #actions depending on what the user types:
        if actionInput in ['n', 'N']: 
            player.move_north()
        elif actionInput in ['s', 'S']:
            player.move_south()
        elif actionInput in ['w', 'W']:
            player.move_west()
        elif actionInput in ['e', 'E']:
            player.move_east
        else:
            print("Invalid Action try again!")

def getPlayerCommand():
    return input('Action: ')

play()

