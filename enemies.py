class Enemy: #create a new class called enemey so I can reference this object
    def __init__(self): #create empty object type
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self): #create name of enemy
        return self.name
    
    def isAlive(self): #create function to define whether or not enemey is dead or alive
        return self.hp<0 #hp is health meter 
    
class GiantRobot: #create Giant robot that inherits attributes from Enemy class
    def __init__(self):
        self.name = "Giant Robot"
        self.hp = 30
        self.damage = 3 

class StormTrooper:
    def __init__(self):
        self.name = "Storm Trooper"
        self.hp = 20
        self.damage = 2

class TRexDino:
    def __init__(self):
        self.name = "TRex"
        self.hp = 40
        self.damage = 9

class LaserDrone:
    def __init__(self):
        self.name = "Laser Drone"
        self.hp = 10
        self.damage = 5


        