# Warrior Game: A simple text-based game where a warrior can equip different weapons and fight an enemy.
# Download and run this code in a Python environment to play the game.

class Weapon():
    def __init__(self, name, attack, weapon_type):
        self.name = name
        self.attack = attack
        self.weapon_type = weapon_type

    def __str__(self):
        return f"{self.name} ({self.weapon_type}) - Attack: {self.attack}"

class Armor():
    def __init__(self, name, defense, material):
        self.name = name
        self.defense = defense
        self.material = material
    
    def __str__(self):
        return f"{self.name} ({self.material}) - Defense: {self.defense}"
    
class Helmet():
    def __init__(self, name, defense, material):
        self.name = name
        self.defense = defense
        self.material = material
    
    def __str__(self):
        return f"{self.name} ({self.material}) - Defense: {self.defense}"

class Shield():
    def __init__(self, name, defense, material):
        self.name = name
        self.defense = defense
        self.material = material
    
    def __str__(self):
        return f"{self.name} ({self.material}) - Defense: {self.defense}"
    
class Enemy:
    def __init__(self, hp):
        self.hp = hp

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        print(f"Enemy takes {damage} damage! HP remaining: {self.hp}")
        if self.hp == 0:
            print(f"Enemy is defeated!")

class Warrior:
    def __init__(self, armor, helmet, shield):
        self.weapon = None
        self.armor = armor
        self.helmet = helmet
        self.shield = shield

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"Warrior equipped {weapon.name}!")

    def attack(self, enemy: Enemy):
        damage = self.weapon.attack
        print(f"Warrior attacks with {self.weapon.name}!")
        enemy.take_damage(damage)

    def display_status(self):
        print("*"*50)
        print("Warrior Status: ")
        print(f"Weapon: {self.weapon.name}")
        print(f"Armor: {self.armor.name}")
        print(f"Helmet: {self.helmet.name}")
        print(f"Shield: {self.shield.name}")
        print(f"Attack Power: {self.weapon.attack}")
        print("*"*50)

weapons = [
    Weapon("Broadsword", 20, "Sword"),
    Weapon("Battle Axe", 25, "Axe"),
    Weapon("Warhammer", 30, "Hammer"),
    Weapon("Spear", 15, "Polearm")
]

# Create armor pieces
armor = Armor("Chainmail", 25, "Chainmail")
helmet = Helmet("Steel Helmet", 15, "Steel")
shield = Shield("Wooden Shield", 18, "Wood & Metal")

# Create warrior
warrior = Warrior(armor, helmet, shield)

#Equip weapon
print("\nChoose your weapon: ")
for i, weapon in enumerate(weapons):
    print(f"{i+1}. {weapon}")

choice = int(input("Enter your choice (1-4): ")) - 1
warrior.equip_weapon(weapons[choice])

warrior.display_status()

#Create enemy
enemy = Enemy(25)
warrior.attack(enemy)