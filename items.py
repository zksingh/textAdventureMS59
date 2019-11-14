class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name

class Knife(Weapon):
    def __init__(self):
        self.name = "Knife"
        self.description = "A sturdy blade working as a sturdy starting weapon."
        self.damage = 2
        self.value = 5

class LightSaber(Weapon): 
    def __init__(self):
        self.name = "Light Saber"
        self.description = "A light saber suitable for fighting against the Dark Side and using the Force."
        self.damage = 5 
        self.value = 7

class LaserGun(Weapon): 
    def __init__(self):
        self.name = "Laser Gun"
        self.description = "A gun that shoots hot lasers, suitable for far away enemies and flying things."
        self.damage = 3
        self.value = 4

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

class Bread:
    def __init__(self):
        self.name = "Bread"
        self.hp = 10
        self.value = 10
        
class rawMeat:
    def __init__(self):
        self.name = "Raw Meat"
        self.hp = 20
        self.value = 30

class HealingPotion:
    def __init__(self):
        self.name = "Healing Potion"
        self.hp = 60
        self.value = 50