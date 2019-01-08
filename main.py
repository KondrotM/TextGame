import rooms
import items
import pickle
import enemies

import random
import time

cavern = [[rooms.wall,rooms.spawn,rooms.wall,rooms.wall],[rooms.sword,rooms.enemyC,rooms.wall,rooms.wall],[rooms.wall,rooms.enemyC,rooms.enemyC,rooms.potion],[rooms.enemyC,rooms.switch,rooms.passage,rooms.wall]]
level = cavern

class Player:
    def __init__(self,health,maxhealth, defense, strength, speed, level, exp, inventory, equipment, alive,x,y,memory):
        self.health = health    # need two diffrent ones so potions don't overheal
        self.maxhealth = maxhealth
        self.defense = defense  #
        self.strength = strength  # combat stats for battle
        self.speed = speed      #
        self.level = level      # increases with exp
        self.exp = exp          # increases with enemy kills
        self.inventory = inventory  # player's local inventory
        self.equipment = equipment  # equipment grants stat upgrades, while inv doesn't
        self.alive = alive  # a dead player loses the game
        self.x = x  # player co ordinates
        self.y = y
        self.memory = memory  # a list of unique attributes which carry through the game.

    def take(self,item):
        # item is taken from the room's inventory and added to the player's
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
        #item is taken from player's inventory and added to the room's
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
        # splits player's input into an array of words.
        time.sleep(.67)
        print("CHOOSE WHAT TO DO")
        choice = input().lower()
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

    def equip(self,item):
        # item is added to player's equipment, and any stats are added
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
        # checks if the player can move in a certain direction. used to let the player know their options on the map.
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
        # displays player's equipment
        time.sleep(.67)
        print("YOU EQUIP:")
        for i in player.equipment:
            if i.type == "weapon":
                print(" *", i.name.upper(),", +",i.strength,"STR")
            if i.type == "armour":
                print(" *", i.name.upper(),", +",i.defense,"DEF")
        time.sleep(.67)

    def move(self,option):
        # changes the player's position on the level grid.
        oldpos = [player.y, player.x]
        oldroom = level[player.y][player.x]
        validmove = True
        option += " "
        # appends space to each option so only one is recognised
        north = ["north ", "n ", "up ", "u "]
        east = ["east ", "e ", "right ", "r "]
        south = ["south ", "s ", "d "]
        west = ["west ", "w ", "left ", "l "]
        for i in north:
            if option in i:
                player.y += 1
        for i in east:
            if option in i:
                player.x += 1
        for i in south:
            if option in i:
                player.y -= 1
        for i in west:
            if option in i:
                player.x -= 1
        # checks if you are in the final level room
        if level[player.y][player.x] == rooms.passage:
            # player must complete the puzzle first
            if rooms.passage.actions:
                if items.pendant in player.inventory:
                    print("YOU INSERT THE PENDANT INTO THE OPENING ON THE DOOR")
                    time.sleep(1)
                    print("THE DOOR SLOWLY INCHES OPEN")
                    time.sleep(.67)
                    player.inspect("room")
                    choice = input("WOULD YOU LIKE TO LEAVE THE CAVERN? (y/n)\n").lower()
                    if choice in ["yes", "y"]:
                        time.sleep(.67)
                        print("YOU LEAVE THE CAVERN AND RETURN TO YOUR LIFE WITH A TALE TO TELL")
                        time.sleep(1.5)
                        print("GAME WON")
                        quit()
                else:
                    time.sleep(.67)
                    print("THE DOOR IS LOCKED. TRY FIND A KEY (OR PENDANT) TO UNLOCK IT WITH")
                    player.x -= 1
            else:
                time.sleep(.67)
                print("YOU CAN'T MOVE THERE")
                player.x -= 1

        try:
            # checks if the player is in a wall, or out of bounds.
                if level[player.y][player.x] == rooms.wall or player.x < 0 or player.y < 0:
                    player.y = oldpos[0]
                    player.x = oldpos[1]
                    time.sleep(.67)
                    print("YOU CAN'T MOVE THERE")
                    validmove = False
                    player.nturn()
        except IndexError:
            # if the player.x/y > level[x/y], this exception catches it.
            player.y = oldpos[0]
            player.x = oldpos[1]
            time.sleep(.67)
            print("YOU CAN'T MOVE THERE")
            validmove = False
            player.nturn()

        pos = level[player.y][player.x]
        time.sleep(.67)

        if validmove:
            print("YOU ENTER", pos.name)
            # clears previous room's inventory
            if oldroom.type == "temp":
                oldroom.inventory = []

            # checks for hostile room
            if pos == rooms.enemyC:
                if random.randint(0, 100) > 50:
                    enemyNo = random.randint(0, len(rooms.enemyC.enemieslist) - 1)
                    battle(player, rooms.enemyC.enemieslist[enemyNo],level)

    def drink(self,item):
        # player drinks (health) potion to restore health
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
        # gets all possible choices accepted by the game input
        directions = ["north", "n", "up", "u", "west", "w", "left", "l", "south", "s", "down", "d", "east", "e", "right", "r"]
        oneWord = ["inventory", "stats", "inv", "equipment","save"]
        twoWord = ["inspect", "flip", "take", "drop", "drink", "equip"]
        invchoices = []
        for i in player.inventory:
            invchoices.append(i)
        validchoices = [directions,oneWord,twoWord,invchoices]
        return validchoices

    def nturn(self):
        # player's neutral turn
        cRoom = level[player.y][player.x]
        validchoices = player.getvalidchoices()
        # dictionary for when the player specifies the item as a string
        itemdict = {
            "plank": items.sword,
            "potion": items.potionH,
            "rags": items.armour,
            "sword": items.sword2,
            "armour": items.armour2,
            "torch": items.torch,
            "pendant" : items.pendant
        }
        choicesmade = 0
        while choicesmade != 1:  # checks if only one valid argument is given.
            option = player.getchoice()
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
        # checks which of the arguments has been stated and executes it
        if "flip" in option and cRoom == rooms.switch:
            player.memory[0] = rooms.switchp(option,player.memory[0])

        if "save" in option:
            save(player)

        if "equipment" in option:
            player.getequip()

        if "stats" in option:
            player.printstats()

        if "inventory" in option:
            time.sleep(.67)
            print("THE CONTENTS OF YOUR INVENTORY")
            getinv(player.inventory)
        # if a two-word argument was stated, looks also at the next argument given
        if "inspect" in option:
            for i in range(option.__len__()):
                if option[i] == "inspect":
                    try:
                        if option[i+1].lower() == "the":
                            player.inspect([option[i+2]])
                        else:
                            player.inspect(option[i+1])
                    except:
                        time.sleep(.67)
                        print("YOU CAN'T DO THAT")
        if "drink" in option:
            for i in range(option.__len__()):
                if option[i] == "drink":
                    try:
                        if option[i+1].lower() in ["the","a"]:
                            player.drink(itemdict[option[i+2]])
                        else:
                            player.drink(itemdict[option[i+1]])
                    except:
                        time.sleep(.67)
                        print("YOU CAN'T DO THAT")
        if "drop" in option:
            for i in range(option.__len__()):
                if option[i] == "drop":
                    try:
                        if option[i+1].lower() == "the":
                            player.drop(itemdict[option[i+2]])
                        else:
                            player.drop(itemdict[option[i+1]])
                    except:
                        time.sleep(.67)
                        print("YOU CAN'T DO THAT")

        if "equip" in option:
            for i in range(option.__len__()):
                if option[i] == "equip":
                    try:
                        if option[i + 1].lower() == "the":
                            player.equip(itemdict[option[i + 2]])
                        else:
                            player.equip(itemdict[option[i + 1]])
                    except:
                        time.sleep(.67)
                        print("YOU CAN'T DO THAT")

        if "take" in option:
            for i in range(option.__len__()):
                if option[i] == "take":
                    try:
                        if option[i + 1].lower() == "the":
                            player.take(itemdict[option[i + 2]])
                        else:
                            player.take(itemdict[option[i + 1]])
                    except:
                        time.sleep(.67)
                        print("YOU CAN'T DO THAT")

    def inspect(self, item):
        #prints item or room description
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
            # defines itemdict again. in a perfect world, this would only need to be done once.
            itemdict = {
                "plank": items.sword,
                "potion": items.potionH,
                "rags": items.armour,
                "sword": items.sword2,
                "armour": items.armour2,
                "torch": items.torch,
                "pendant": items.pendant
            }
            time.sleep(.67)
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
        # upgrades player's level and stats
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


def battle(player, enemy,level):
    #combat between player and enemy
        time.sleep(.67)
        print("YOU HAVE ENCOUNTERED AN",enemy.name)
        time.sleep(.67)
        input("PREPARE FOR BATTLE")
        choices = ["INSPECT","SLASH","CHOP","LUNGE"]
        pHealth = player.health
        # enemy health transfered to another variable else all future enemies of the same class will have 0 health
        eHealth = enemy.health
        while eHealth > 0 and pHealth > 0:
            turn = True
            while turn:
                choice = ""
                while choice not in choices: # loops choice until a valid argument is given
                    print(choices)
                    time.sleep(.67)
                    choice = input("CHOOSE YOUR ACTION \n")
                    choice = choice.upper()
                if choice == "INSPECT":
                    # inspects enemy, shows their weakness
                    time.sleep(.67)
                    print(enemy.desc)
                    time.sleep(1)
                    print("WEAK TO", enemy.weakness)
                    time.sleep(.67)
                if choice in ["SLASH","CHOP","LUNGE"]:
                    # attacks the enemy, attacking with their weakness amplifies damage
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
            if eHealth > 0:
                time.sleep(.67)
                print("---ENEMY TURN---")
                hitRNG = random.randint(0,100)
                # adds a chance that the enemy misses their hit
                if hitRNG > player.speed:
                    multiplier = random.randint(80, 120) / 100
                    damage = enemy.strength * multiplier
                    damage -= (player.defense/10)
                    pHealth -= damage
                    time.sleep(.67)
                    print("THE ", enemy.name, " HITS YOU FOR ", damage, " DAMAGE")
                    time.sleep(.67)
                    print("YOU HAVE ", pHealth, " HEALTH REMAINING")
                    time.sleep(.67)
                else:
                    time.sleep(.67)
                    print("THE ENEMY MISSED ITS ATTACK")
                    time.sleep(1)
                print("---YOUR TURN---")
                time.sleep(.67)
        if pHealth <= 0:
            # player dies
            time.sleep(1)
            print("YOU ARE DEAD")
            player.alive = False
        if eHealth <= 0:
            # player wins and gets rewards
            time.sleep(1)
            print("VICTORY")
            potRNG = random.randint(0,100)
            if potRNG > 80:
                level[player.y][player.x].inventory.append(items.potionH)
                time.sleep(.67)
                print("ENEMY DROPPED A POTION")
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

def getinv(inventory):
    # prints inventory
    for i in inventory:
        print(" *",i.name)

def save(player):
    # saves player game to external file
    with open('savefile.pickle', 'wb') as handle:
        pickle.dump(player,handle)
    time.sleep(1)
    print("GAME SAVED")

def printmenu():
    print("*******************")
    print("WELCOME TO TEXTGAME")
    print("*******************")
    print("SELECT YOUR CHOICE:")
    print("1. NEW GAME")
    print("2. LOAD GAME")
    print()
    print("9. EXIT GAME")

printmenu()
choices = ["1","2","9"]
choice = str(input())
while choice not in choices:
    print("INVALID CHOICE")
    choice = input()
if choice == "1":
    print("YOU WAKE UP IN A COLD ROOM")
    time.sleep(1)
    print("THE LAST THING YOU REMEMBER IS GOING TO EXPLORE A CAVE")
    time.sleep(1)
    print("YOUR CLOTHES ARE TATTERED")
    time.sleep(1)
    print("YOU PICK UP A NEARBY PLANK, AND LIGHT YOUR ONLY TORCH")
    player = Player(100,100,11,12,10,1,0,[items.potionH,items.torch],[items.sword,items.armour],True,1,0,[0])
elif choice == "2":
    try:
        with open('savefile.pickle', 'rb') as handle:
            player = pickle.load(handle)
        print("GAME LOADED")
    except:
        print("LOAD FAILED")
        player = Player(100,100,11,12,10,1,0,[items.potionH,items.torch],[items.sword,items.armour],True,1,0,[0])
elif choice == "9":
    quit()


while player.alive:
    player.nturn()
