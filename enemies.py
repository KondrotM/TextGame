
class enemy:
    def __init__(self,name,strength,health,desc):
        self.name = name
        self.strength = strength
        self.health = health
        self.desc = desc

class player:
    def __init__(self,health, defense, strength, speed):
        self.health = health
        self.defense = defense
        self.strength = strength
        self.speed = speed

    def attack(self, other):
        option = input("Select attack:\n *Chop \n *Slash \n *Lunge \n").upper()
        print(option,"on",other)

    def upgrade(self):
        option = ""
        while option not in ("DEFENSE","STRENGTH","SPEED","DEF","STR","SPD"):
            option = input("CHOOSE WHAT STAT TO UPGRADE \n *DEFENSE \n *STRENGTH \n *SPEED \n").upper()
            if option == "DEFENSE" or "DEF":
                player.defense += 1
            elif option == "STRENGTH" or "STR":
                player.strength += 1
            elif option == "SPEED" or "SPD  ":
                player.speed += 1





player=player(10,10,10,10)
orc=enemy("orc",5,10,"A fierce orc")
#player.attack(orc.name)
player.upgrade()
print(player.defense)
print(orc.desc)
