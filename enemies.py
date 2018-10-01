
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
        option = input("SELECT ATTACK:\n *CHOP \n *SLASH \n *LUNGE \n").upper()
        print(option,"on",other)

    def printstats(self):
        print("YOUR STATS:")
        print("HEALTH:", player.health)
        print("DEFENSE:", player.defense)
        print("STRENGTH:", player.strength)
        print("SPEED:", player.speed)

    def upgrade(self):
        option = ""
        while option not in ("DEFENSE","STRENGTH","SPEED","DEF","STR","SPD"):
            option = input("CHOOSE WHAT STAT TO UPGRADE \n *DEFENSE \n *STRENGTH \n *SPEED \n").upper()
            if option in ("DEFENSE","DEF"):
                player.defense += 1
            elif option in ("STRENGTH","STR"):
                player.strength += 1
            elif option in ("SPEED","SPD"):
                player.speed += 1
            else:
                print("INVALID OPTION")
        player.health += 1




player=player(10,10,10,10)
orc=enemy("orc",5,10,"A fierce orc")
#player.attack(orc.name)
player.upgrade()
player.printstats()
#print(orc.desc)
