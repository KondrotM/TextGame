import rooms
import enemies

import random

cavern = [[rooms.wall,rooms.spawn,rooms.wall,rooms.wall],[rooms.enemyC,rooms.enemyC,rooms.wall,rooms.wall],[rooms.wall,rooms.enemyC,rooms.enemyC,rooms.enemyC],[rooms.enemyC,"switch",rooms.wall,rooms.wall,rooms.wall]]
level = cavern                                           #rooms.sword                                                                            #rooms.potion


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

    def getchoice(self):
        choice = input("CHOOSE WHAT TO DO").lower()
        inputs = []
        word = ""
        for i in choice:
            if i == " ":
                inputs.append(word)
                word = ""
            else:
                word = word + i
        inputs.append(word)
        return inputs

    def getpos(self):
        pos = level[player.y][player.x]
        if pos == rooms.enemyC:
            if random.randint(0, 100) > 50:
                input("PREPARE FOR BATTLE")
                enemyNo = random.randint(0,len(rooms.enemyC.enemies))
                battle(player, rooms.enemyC.enemies[enemyNo])
        if pos == "switch":
            rooms.switch()

    def move(self):
        option = ""
        oldpos = [player.y,player.x]
        choicesmade = 0
        while choicesmade != 1:  # checks if only one valid argument is given.
            # rooms and enemies should probably have their own .py files and i import them later
            option = player.getchoice()
            for i in option:
                if i in ["n","e","s","w","inspect"]:
                    choicesmade += 1
            if choicesmade > 1:
                print("TOO MANY TASKS")
            if choicesmade == 0:
                print("NOTHING HAPPENS")

        if "n" in option:
            player.y += 1
        if "e" in option:
            player.x += 1
        if "s" in option:
            player.y -= 1
        if "w" in option:
            player.x -= 1
        if "inspect" in option:
            for i in range(option.__len__()):
                if option[i] == "inspect":
                    player.inspect(option[i+1])
        try:
                if level[player.y][player.x] == "x" or player.x < 0 or player.y < 0:
                    player.y = oldpos[0]
                    player.x = oldpos[1]
                    print("YOU CAN'T MOVE THERE")
                    print(level[player.y][player.x])  # debug
                    print(player.x,player.y)  # debug
                    player.move()
        except IndexError:
            player.y = oldpos[0]
            player.x = oldpos[1]
            print("YOU CAN'T MOVE THERE")
            print(level[player.y][player.x])  # debug
            print(player.x, player.y)  # debug
            player.move()

        print(level[player.y][player.x])
        print(player.x, player.y)

    def inspect(self, item):
        item = item.lower()
        if item == "room":
            item = level[player.y][player.x]
            print(item.desc) # make a for loop later, prints whole list
        else:
            print(item.desc)

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
        pHealth = player.health
        eHealth = enemy.health
        while eHealth > 0 and pHealth > 0:
            turn = True
            while turn:
                choice = ""
                while choice not in choices:
                    print(choices)
                    choice = input("CHOOSE YOUR ACTION \n")
                    choice = choice.upper()
                if choice == "INSPECT":
                    print(enemy.desc)
                    turn = False
                if choice in ["SLASH","CHOP","LUNGE"]:
                    multiplier = random.randint(80,120)/100
                    damage = player.strength*multiplier
                    if choice == enemy.weakness:
                        damage = damage*1.5
                    damage = round(damage,2)
                    eHealth -= damage
                    eHealth = round(eHealth,2)
                    print("ENEMY TOOK ",damage," DAMAGE")
                    print("ENEMY HAS ",eHealth," HEALTH LEFT")
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
        elif eHealth <= 0:
            print("VICTORY")
            player.health = pHealth
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


player = Player(100,10,10,10,1,0,True,1,0)

while player.alive:
    player.move()
    player.getpos()

    print("")


#player.attack(orc.name)
#print(orc.desc)
