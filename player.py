import items

#check items instances

class Player:
    def __init__(self):
        self.inventory = [items.Knife(), 'Gold(5)', 'Bread']
        self.x = 1 
        self.y = 2

    def printInventory(self):
        print("Inventory")
        for item in inventory:
            print('*' + str(item))
        bestWeapon = self.mostPowerfulWeapon()
        print("Your best weapon is {}.".format(bestWeapon))
    
    def mostPowerfulWeapon(self):
        maxDamage = 0
        bestWeapon = None
        for item in self.inventory:
            try:
                if item.damage > maxDamage:
                    bestWeapon = item
                    maxDamage = item.damage 
            except AttributeError:
                pass
        return bestWeapon
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)




