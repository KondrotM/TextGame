import random

map = [["x","spawn","x","x"],["sword","enemy","x","x"],["x","enemy","enemy","potion"],["x","puzzle","x","x","x"]]

class Enemy:
    def __init__(self,name,strength,health,desc,weakness,exp):
        self.name = name
        self.strength = strength
        self.health = health
        self.desc = desc
        self.weakness = weakness
        self.exp = exp

class Room:
    def __init__(self,name,style,x,y):
        self.name = name
        self.style = style
        self.x = x
        self.y = y


class Player:
    def __init__(self,health, defense, strength, speed, level, exp, alive,x,y):
        self.health = health
        self.defense = defense
        self.strength = strength
        self.speed = speed
        self.level = level
        self.exp = exp
        self.alive = alive
        self.x = x
        self.y = y

    def move(self):
        option = ""
        oldpos = [player.y,player.x]
        while option not in ["n","e","s","w"]: #while option not in Room.choices.
            #rooms and enemies should probably have their own .py files and i import them later
            option = input("CHOOSE WHAT TO DO")
            option=option.lower()
            if option == "n":
                player.y += 1
            if option == "e":
                player.x += 1
            if option == "s":
                player.y -= 1
            if option == "w":
                player.x -= 1

            try:
                    if map[player.y][player.x] == "x" or player.x < 0 or player.y < 0:
                        player.y = oldpos[0]
                        player.x = oldpos[1]
                        print("YOU CAN'T MOVE THERE")
                        option = ""
                        print(map[player.y][player.x]) #debug
                        print(player.x,player.y) #debug
            except IndexError:
                player.y = oldpos[0]
                player.x = oldpos[1]
                print("YOU CAN'T MOVE THERE")
                option = ""
                print(map[player.y][player.x]) #debug
                print(player.x, player.y) #debug

        print(map[player.y][player.x])
        print(player.x, player.y)


#checkvalidposition
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


def battle(player, enemy):
        choices = ["INSPECT","SLASH","CHOP","LUNGE"]
        print("YOU HAVE ENCOUNTERED AN",enemy.name)
        pHealth = player.health * 10
        while enemy.health > 0 and pHealth > 0:
            turn = True
            while turn:
                choice = ""
                while choice not in choices:
                    print(choices)
                    choice = input("CHOOSE YOUR ACTION \n")
                    choice = choice.upper()
                if choice == "INSPECT":
                    print(orc.desc)
                    turn = False
                if choice in ["SLASH","CHOP","LUNGE"]:
                    multiplier = random.randint(80,120)/100
                    damage = player.strength*multiplier
                    if choice == enemy.weakness:
                        damage = damage*1.5
                    damage = round(damage,2)
                    enemy.health = enemy.health - damage
                    enemy.health = round(enemy.health,2)
                    print("ENEMY TOOK ",damage," DAMAGE")
                    print("ENEMY HAS ",enemy.health," HEALTH LEFT")
                    turn = False
            print("---ENEMY TURN---")
            multiplier = random.randint(80, 120) / 100
            damage = enemy.strength * multiplier
            pHealth -= damage
            print("THE ",enemy.name," HITS YOU FOR ",damage," DAMAGE")
            print("YOU HAVE ",pHealth," HEALTH REMAINING")
        if pHealth <= 0:
            print("YOU ARE DEAD")
            player.alive = False
        elif enemy.health <= 0:
            print("VICTORY")
            player.exp += enemy.exp
            if player.exp >= 45+(player.level*5):
                print("LEVEL UP")
                player.level += 1
                player.exp -= 45+(player.level*5)
                player.upgrade()
                player.printstats()
            else:
                print("YOU HAVE GAINED ", enemy.exp, " EXP")
                print("YOU HAVE ", player.exp, "/", 45+(player.level*5), "EXP")



player = Player(10,10,10,10,1,0,True,1,0)
while player.alive:
    player.move()
    print("")
    orc = Enemy("ORC", 5, 50, "A FIERCE ORC. WEAK TO SLASH", "SLASH", 25)
    if map[player.y][player.x] == "enemy":
        input("PREPARE FOR BATTLE")
        battle(player, orc)

#player.attack(orc.name)
#print(orc.desc)
