import enemies
import items



class Room:
    def __init__(self,name,desc,actions, enemieslist,type,inventory):
        self.name = name
        self.desc = desc
        self.actions = actions
        self.enemieslist = enemieslist
        self.type = type
        self.inventory = inventory


def switchp(choice,flipped):
    switchorder = ["red", "orange", "yellow", "green", "blue", "purple"]  # this can be improved so it's not declared every time
    try:
        if choice[1] == switchorder[flipped]:
            flipped += 1
            print("YOU HEAR A CLICK")
            if flipped == len(switchorder):
                print("A DOOR TO THE EAST IS REVEALED")
                passage.actions = True
        else:
            flipped = 0
            print("ALL SWITCHES SNAP TO THEIR STARTING POSITION")
        return flipped
    except:
        print("A DOOR TO THE EAST IS REVEALED")
        passage.actions = True



wall = Room("WALL","",[],[],"temp",[])
sword = Room("A SMALL CLEARING",["YOU OBSERVE THAT YOU'VE ENTERED A SMALL CLEARING IN THE NARROW PATHWAY.","A SMALL PEDESTAL PROTRUDES IN THE CENTRE, ILLUMINATED BY FEINT CANDLELIGHT."],[],[],"perm",[items.sword2])
spawn = Room("A COLLAPSED TUNNEL",["YOU SURVEY YOUR SURROUNDINGS.", "THE TUNNEL TO THE CAVE YOU ENTERED HAS COLLAPSED.", "YOU ARE LEFT ON YOUR OWN."],[],[],"perm",[items.potionH,items.pendant])
enemyC = Room("A CRAMPED CORRIDOR",["YOU SQUEEZE THROUGH INTO WHAT SEEMS TO BE AN OLD TUNNEL LEFT BY MINERS","IT'S DARK, AND DAMP."],[],[enemies.orc,enemies.bat,enemies.slime],"temp",[])
switch = Room("A PUZZLING ROOM",["YOU ENTER A LARGE ROOM FILLED WITH LEVELS","THERE ARE SIX LEVERS:","BLUE. GREEN. ORANGE. PURPLE. RED. YELLOW"],[],[],"perm",[])
potion = Room("A CONCEALED STASH",["YOU NOTICE A SMALL HOLE IN THE WALL","IT CONTAINS A POTION"],[],[],"perm",[items.potionH])
passage = Room("A PASSAGE",["YOU WALK THROUGH THE DOOR INTO A PASSAGE","YOU SEE TRICKLES OF LIGHT FROM FURTHER IN","WALKING FURTHER, YOU SEE THE OUTDOORS","YOU HAVE FOUND THE EXIT."],False,[],"perm",[])
