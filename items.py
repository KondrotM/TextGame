class Item:
    def __init__(self,name,desc,type,defense,strength):
        self.name = name
        self.desc = desc
        self.type = type
        self.defense = defense
        self.strength = strength


sword = Item("A PLANK","A ROTTING PLANK OF WOOD","weapon",0,2)
armour = Item("RAGS", "RAGS TATTERED FROM YOUR FALL","armour",1,0)
sword2 = Item("A POLISHED SWORD","A SWORD WITH A RAZOR STEEL EDGE","weapon",0,5)
armour2 = Item("STUDDED ARMOUR","REINFORCED LEATHER ARMOUR","armour",3,0)
potionH = Item("POTION","A FLASK FILLED WITH A RED LIQUID","potion",0,0)
torch = Item("TORCH","A DIMLY BURNING TORCH WHICH ALLOWS YOU TO FIND YOUR WAY","misc",0,0)
