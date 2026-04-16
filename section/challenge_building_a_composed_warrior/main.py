class Weapon:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

class Warrior:
    def __init__(self, name):
        self.weapon = None
        self.name = name

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def show_weapon(self):
        if self.weapon == None:
            print (f"{self.name} is unarmed") 
        else:
            print (f"{self.name} is holding a {self.weapon.name}")

sword = Weapon("sword", 5)
warrior = Warrior("conan")

warrior.equip_weapon(sword)
warrior.show_weapon()