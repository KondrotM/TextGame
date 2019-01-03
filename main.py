import rooms
import items
import enemies

import random
import time

cavern = [[rooms.wall,rooms.spawn,rooms.wall,rooms.wall],[rooms.sword,rooms.enemyC,rooms.wall,rooms.wall],[rooms.wall,rooms.enemyC,rooms.enemyC,rooms.potion],[rooms.enemyC,rooms.switch,rooms.wall,rooms.wall,rooms.wall]]
level = cavern                                           #rooms.sword                                                                            #rooms.potion


class Player:
    def __init__(self,health,maxhealth, defense, strength, speed, level, exp, inventory, equipment, alive,x,y,memory):
        self.health = health
        self.maxhealth = maxhealth
        self.defense = defense
        self.strength = strength
        self.speed = speed
        self.level = level
        self.exp = exp
        self.inventory = inventory
        self.equipment = equipment
        self.alive = alive
        self.x = x
        self.y = y
        self.memory = memory

    def take(self,item):
        room = level[player.y][player.x]
        if item in room.inventory:
            player.inventory.append(item)
            time.sleep(.67)
            print("TOOK",item.name.upper())
            room.inventory.remove(item)
        else:
            time.sleep(.67)
            print("NOTHING HAPPENS")

    def drop(self,item):
        room = level[player.y][player.x]
        if item in player.inventory:
            player.inventory.remove(item)
            time.sleep(.67)
            print("DROPPED",item.name.upper())
            room.inventory.append(item)
        else:
            time.sleep(.67)
            print("NOTHING HAPPENS")

    def getchoice(self):
        time.sleep(.67)
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
                enemyNo = random.randint(0,len(rooms.enemyC.enemieslist)-1)
                battle(player, rooms.enemyC.enemieslist[enemyNo])
        #if pos == "switch":
            #rooms.switch()

    def equip(self,item):
        if item.type == "weapon":
            player.strength -= player.equipment[0].strength
            player.strength += item.strength
            player.equipment[0] = item
            time.sleep(.67)
            print("EQUIPPED", item.name)
        elif item.type == "armour":
            player.defense -= player.equipment[0].defense
            player.defense += item.defense
            player.equipment[1] = item
            time.sleep(.67)
            print("EQUIPPED", item.name)
        else:
            time.sleep(.67)
            print("YOU CAN'T EQUIP THAT")

    def finddirections(self):
        truedirs = []
        try:
            direction = level[player.y+1][player.x]
            if direction != rooms.wall:
                truedirs.append("NORTH")
        except:
            pass
        try:
            direction = level[player.y][player.x+1]
            if direction != rooms.wall:
                truedirs.append("EAST")
        except:
            pass
        try:
            direction = level[player.y-1][player.x]
            if direction != rooms.wall:
                if player.y != 0:
                    truedirs.append("SOUTH")
        except:
            pass
        try:
            direction = level[player.y][player.x-1]
            if direction != rooms.wall:
                truedirs.append("WEST")
        except:
            pass
        return truedirs

    def getequip(self):
        time.sleep(.67)
        print("YOU EQUIP:")
        for i in player.equipment:
            if i.type == "weapon":
                print(" *", i.name.upper(),", +",i.strength,"STR")
            if i.type == "armour":
                print(" *", i.name.upper(),", +",i.defense,"DEF")
        time.sleep(.67)

    def move(self,option):
        oldpos = [player.y, player.x]
        oldroom = level[player.y][player.x]
        validmove = True
        if "n" in option:
            player.y += 1
        if "e" in option:
            player.x += 1
        if "s" in option:
            player.y -= 1
        if "w" in option:
            player.x -= 1

        try:
                if level[player.y][player.x] == rooms.wall or player.x < 0 or player.y < 0:
                    player.y = oldpos[0]
                    player.x = oldpos[1]
                    time.sleep(.67)
                    print("YOU CAN'T MOVE THERE")
                    #print(level[player.y][player.x])  # debug
                    print(player.x,player.y)  # debug
                    validmove = False
                    player.nturn()
        except IndexError:
            player.y = oldpos[0]
            player.x = oldpos[1]
            time.sleep(.67)
            print("YOU CAN'T MOVE THERE")
            validmove = False
            player.nturn()

        pos = level[player.y][player.x]
        time.sleep(.67)
        print("YOU ENTER", pos.name)

        if validmove:
            if oldroom.type == "temp":
                oldroom.inventory = []

            if pos == rooms.enemyC:
                if random.randint(0, 100) > 50:
                    enemyNo = random.randint(0, len(rooms.enemyC.enemieslist) - 1)
                    battle(player, rooms.enemyC.enemieslist[enemyNo])



    def drink(self,item):
        if item.name == "potion":
            if items.potionH in player.inventory:
                player.health += 20
                if player.health > player.maxhealth:
                    player.health = player.maxhealth
                player.inventory.remove(items.potionH)
                time.sleep(.67)
                print("DRANK POTION")
                time.sleep(.67)
                print("20 HEALTH RESTORED")
            else:
                time.sleep(.67)
                print("YOU HAVE NO POTIONS TO DRINK")
        else:
            time.sleep(.67)
            print("YOU CAN'T DRINK THAT")

    def getvalidchoices(self):
        directions = ["n","s","e","w"]
        oneWord = ["inventory","stats","inv"]
        twoWord = ["inspect","flip","take","drop","drink","equip"]
        invchoices = []
        for i in player.inventory:
            invchoices.append(i)
        validchoices = [directions,oneWord,twoWord,invchoices]
        return validchoices

    def nturn(self):
        cRoom = level[player.y][player.x]
        option = player.getchoice()
        validchoices = player.getvalidchoices()
        itemdict = {
            "plank": items.sword,
            "potion": items.potionH,
            "rags": items.armour,
            "sword": items.sword2,
            "armour": items.armour2,
            "torch": items.torch,
#            "room": level[[player.y],[player.x]]
        }
        choicesmade = 0
        while choicesmade != 1:  # checks if only one valid argument is given.
            for i in option:
                if i in validchoices[0] or i in validchoices[1] or i in validchoices[2]:
                    choicesmade += 1
            if choicesmade > 1:
                time.sleep(.67)
                print("TOO MANY TASKS")
            if choicesmade == 0:
                time.sleep(.67)
                print("NOTHING HAPPENS")

        for i in option:
            if i in validchoices[0]:
                player.move(i)

        if "flip" in option and cRoom == rooms.switch:
            player.memory[0] = rooms.switch(option,player.memory[0])

        if "equipment" in option:
            player.getequip()

        if "stats" in option:
            player.printstats()

        if "inventory" in option:
            time.sleep(.67)
            print("THE CONTENTS OF YOUR INVENTORY")
            getinv(player.inventory)

        if "inspect" in option:
            for i in range(option.__len__()):
                if option[i] == "inspect":
                    try:
                        player.inspect(option[i+1])
                    except:
                        time.sleep(.67)
                        print("YOU CAN'T DO THAT")
        if "drink" in option:
            for i in range(option.__len__()):
                if option[i] == "drink":
                    try:
                        player.drink(itemdict[option[i+1]])
                    except:
                        time.sleep(.67)
                        print("YOU CAN'T DO THAT")
        if "drop" in option:
            for i in range(option.__len__()):
                if option[i] == "drop":
                    try:
                        player.drop(itemdict[option[i+1]])
                    except:
                        time.sleep(.67)
                        print("YOU CAN'T DO THAT")

        if "equip" in option:
            for i in range(option.__len__()):
                if option[i] == "equip":
                    if option[i+1] in itemdict:
                        player.equip(itemdict[option[i+1]])
                    else:
                        time.sleep(.67)
                        print("YOU CAN'T DO THAT")

        if "take" in option:
            for i in range(option.__len__()):
                if option[i] == "take":
                    if option[i+1] in itemdict:
                        player.take(itemdict[option[i+1]])
                    else:
                        time.sleep(.67)
                        print("YOU CAN'T DO THAT")

    def inspect(self, item):
        item = item.lower()
        if item == "room":
            item = level[player.y][player.x]
            for i in item.desc:
                print(i)
                time.sleep(1)
            directions = player.finddirections()
            time.sleep(.33)
            print()
            print("YOU CAN MOVE", directions)
            if item.inventory != []:
                time.sleep(.67)
                print()
                print("THERE ARE ITEMS ON THE GROUND:")
                time.sleep(.67)
                getinv(item.inventory)
        else:
            itemdict = {
                "plank": items.sword,
                "potion": items.potionH,
                "rags": items.armour,
                "sword": items.sword2,
                "armour": items.armour2,
                "torch": items.torch
            }

            print(itemdict[item].desc)


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
        print("HEALTH RESTORED && INCREASED")
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
        player.maxhealth += 10
        player.health = player.maxhealth


def battle(player, enemy):
        time.sleep(.67)
        print("YOU HAVE ENCOUNTERED AN",enemy.name)
        time.sleep(.67)
        input("PREPARE FOR BATTLE")
        choices = ["INSPECT","SLASH","CHOP","LUNGE"]
        pHealth = player.health
        eHealth = enemy.health
        while eHealth > 0 and pHealth > 0:
            turn = True
            while turn:
                choice = ""
                while choice not in choices:
                    print(choices)
                    time.sleep(.67)
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
                    if eHealth < 0:
                        eHealth = 0
                    time.sleep(.67)
                    print("ENEMY TOOK ",damage," DAMAGE")
                    time.sleep(.67)
                    print("ENEMY HAS ",eHealth," HEALTH LEFT")
                    turn = False
        if eHealth <= 0:
            time.sleep(1)
            print("VICTORY")
            player.health = pHealth
            player.exp += enemy.exp
            if player.exp >= 45+(player.level*5):
                time.sleep(.67)
                print("LEVEL UP")
                player.level += 1
                player.exp -= 45+(player.level*5)
                player.upgrade()
                player.printstats()
            else:
                time.sleep(.67)
                print("YOU HAVE GAINED ", enemy.exp, " EXP")
                time.sleep(.67)
                print("YOU HAVE ", player.exp, "/", 45+(player.level*5), "EXP")
        else:
            time.sleep(.67)
            print("---ENEMY TURN---")
            multiplier = random.randint(80, 120) / 100
            damage = enemy.strength * multiplier
            pHealth -= damage
            time.sleep(.67)
            print("THE ", enemy.name, " HITS YOU FOR ", damage, " DAMAGE")
            time.sleep(.67)
            print("YOU HAVE ", pHealth, " HEALTH REMAINING")
            time.sleep(.67)
        if pHealth <= 0:
            time.sleep(1)
            print("YOU ARE DEAD")
            player.alive = False


def getinv(inventory):
    for i in inventory:
        print(" *",i.name)


player = Player(100,100,11,12,10,1,0,[items.potionH,items.sword2],[items.sword,items.armour],True,1,0,[0])

while player.alive:
    player.nturn()
#    time.sleep(.67)


#player.attack(orc.name)
#print(orc.desc)
