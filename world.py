import enemies
import random

class MapTile: #create maptile class base class of which we will create other tiles from
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def introText(self):
        raise NotImplementedError("Create a subclass instead!")
    
    def modifyPlayer(self, player):
        pass

class StartTile(MapTile): #create the start tile of the world 
    def introText(self):
        return """
        Welcome to the Field, you're playing zone and survival escapade. You have 
        only one chance to survive this place. Kill or be killed. Don't trust anyone
        and rely only on yourself. Now to begin, there are four areas of the Field:
        The Northern Corridors, The Southern Corridors, The East Wall, and The West Wall. 
        """
class BoringTile(MapTile):
    def introText(self):
        return """
        This is a very boring part of the cave.
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random #to randomly place enemies along the tiles
        if r < 0.50:
            self.enemies = enemies.GiantRobot() #place a giant robot every .50 
            self.aliveText = "The ground beneath your feet rumbles."  
            "You look up to a giant mechnical arm swing at you!" 
            "You jump out of the way just in the nick of time." 
            "But the giant robot has not stopped its pursuit"
            self.deadText = "Sparks fly from the broken wires of the dead giant robot strewn across the ground in pieces."
        
        elif r < 0.80:
            self.enemies = enemies.StormTrooper() #place storm trooper 
            self.aliveText = "You hear marching coming from the distance." 
            "You look up to see a familiar white suit and helmet...the Storm Troopers have arrived!"
            self.deadText = "Broken laser guns, white suits, and helmets are sprawled across the ground."
            "The Storm Troopers are dead, for now."

        elif r < 0.95:
            self.enemies = enemies.TRexDino() #place TRex
            self.aliveText = "A loud scream rolls through the Field." 
            "The stomping gets louder and faster followed by another scream..."
            "You look up to see a TRex running towards you in the distance!"
            self.deadText = "The blood of the TRex rolls down the ground and the dead TRex's body rots beneath you."
        
        else:
            self.enemies = enemies.LaserDrone() #place Laser Drones
            self.aliveText = "A hot laser burns the ground in front of your feet."
            "Startled, you look up to see a Laser Drone coming right for you shooting at you!"
            self.deadText = "The punctured Laser Drone lies on the ground, broken and unresponsive."
        
        super().__init__(x,y)

    def introText(self): # set the text to the right one according to if they are dead or alive
        text = self.aliveText if self.enemies.isAlive() else self.deadText
        return text
        
    def modifyPlayer(self, player): #update the player hp accordingly as player fights enemy
        if self.enemies.isAlive():
            player.hp = player.hp - self.enemies.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemies.damage, player.hp))


class VictoryTile(MapTile):
    def modifyPlayer(self, player): #update player if they win game
        player.victory = True

    def introText(self):
        return """
        The Field around suddenly becomes quiet. You look up and see the sky begin to disintegrate...
        ...and a door appears where the Eastern Walls once were.

        You walk towards it. Carved into the wood is the word 'Exit'. You've done it!

        You survived the Field. Congratulations player!
        """
    
class FindMoneyTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1,50) #set the money amount to a random number
        self.goldClaimed = False
        super().__init__(x, y)
        
    def modifyPlayer(self, player):
        if not self.goldClaimed:
            self.goldClaimed = True
            player.gold = player.gold + self.gold 
            print("{} gold added to your inventory.".format(self.gold))
    
    def introText(self):
        if self.goldClaimed:
            "Nothing in this part of the Field. Move on."
        else:
            return """
            Someone must have dropped some money. You pick it up.
            """

#Taken from source code of Make your own python text adventure by Philip Johnson 2018...will probably remove later

world_map = [
    [None,VictoryTile(1,0),None],
    [None,BoringTile(1,1),None],
    [BoringTile(0,2),StartTile(1,2),BoringTile(2,2)],
    [None,BoringTile(1,3),None]
]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None




