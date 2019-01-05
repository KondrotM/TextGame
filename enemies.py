class Enemy:
    def __init__(self,name,desc,weakness,health,strength,exp):
        self.name = name
        self.desc = desc
        self.weakness = weakness
        self.health = health
        self.strength = strength
        self.exp = exp


skeleton = Enemy("SKELETON","A WARRIOR OF THE UNDEAD.","CHOP",80,7,55)
bat = Enemy("BAT","A LARGE, RAVENOUS BAT.","SLASH",15,15,30)
orc = Enemy("ORC","A FIERECE ORC, TOWERING OVER YOU.","LUNGE",50,12,40)
slime = Enemy("SLIME","AN OMINOUS GLOB OF ROTTING GOO","CHOP",40,9,25)
spirit = Enemy("SPIRIT","A DEMONIC SPIRIT HAUNTS THE DUNGEON","SLASH",7,15,60)
succubus = Enemy("SUCCUBUS","AN EVIL SUCCUBUS DASHES AROUND YOU","LUNGE",14,8,50)
