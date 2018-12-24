import enemies

class Room:
    def __init__(self,name,desc,actions, enemies):
        self.name = name
        self.desc = desc
        self.actions = actions
        self.enemies = enemies


def switch():
    print("YOU COME INTO A ROOM WITH FIVE COLOURED SWITCHES: \n BLUE, GREEN, PURPLE, RED, ORANGE AND YELLOW")
    while True:
        choice = input("CHOOSE WHAT TO DO").lower()
        if choice in ["flip red switch","r"]:
            print("YOU HEAR A CLICK")
            choice = input("CHOOSE WHAT TO DO").lower()
            if choice in ["flip orange switch", "o"]:
                print("YOU HEAR A CLICK")
                choice = input("CHOOSE WHAT TO DO").lower()
                if choice in ["flip yellow switch", "y"]:
                    print("YOU HEAR A CLICK")
                    choice = input("CHOOSE WHAT TO DO").lower()
                    if choice in ["flip green switch", "g"]:
                        print("YOU HEAR A CLICK")
                        choice = input("CHOOSE WHAT TO DO").lower()
                        if choice in ["flip blue switch", "b"]:
                            print("YOU HEAR A CLICK")
                            choice = input("CHOOSE WHAT TO DO").lower()
                            if choice in ["flip purple switch", "p"]:
                                break
            print("ALL SWITCHES SNAP INTO THEIR ORIGINAL POSITIONS WITH A LOUD CRASH")
    print("THE DOOR OPENS")
    choice  = input("CHOOSE WHAT TO DO")
    if choice == "ENTER DOOR":
        print("You Win")


#switch()
#print("THE DOOR OPENS")


wall = Room("WALL","",[],[])
enemyC = Room("A SMALL CLEARING",["YOU OBSERVE THAT YOU'VE ENTERED A SMALL CLEARING IN THE NARROW PATHWAY.","A SMALL PEDESTAL PROTRUDES IN THE CENTRE, ILLUMINATED BY FEINT CANDLELIGHT."],[],[enemies.orc,enemies.bat,enemies.slime])
spawn = Room("A COLLAPSED TUNNEL",["A COLLAPSED TUNNEL"],[],[])


#enemiesC = Room("")

#class Item:
#    def __init__(self,name,):


##  List of Rooms:
##  Spawn, x, Sword, Enemy, Potion, Puzzle.
##
## In the future, seperate classes can be declared for each kind of room:
## A class for an enemy room, an item room, a puzzle room.