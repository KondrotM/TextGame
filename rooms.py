class Room:
    def __init__(self,name,desc,actions, enemies):
        self.name = name
        self.desc = desc
        self.actions = actions
        self.enemies = enemies

    def itemroom(self):


wall = Room("WALL","",[],[])
sword = Room("A SMALL CLEARING",["YOU OBSERVE THAT YOU'VE ENTERED A SMALL CLEARING IN THE NARROW PATHWAY.","A SMALL PEDESTAL PROTRUDES IN THE CENTRE, ILLUMINATED BY FEINT CANDLELIGHT."],[])
enemiesC = Room("")


##  List of Rooms:
##  Spawn, x, Sword, Enemy, Potion, Puzzle.
##
## In the future, seperate classes can be declared for each kind of room:
## A class for an enemy room, an item room, a puzzle room.