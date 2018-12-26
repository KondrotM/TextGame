class Item:
    def __init__(self,name,desc,type,armor,attack):
        self.name = name
        self.desc = desc
        self.type = type
        self.armor = armor
        self.attack = attack


sword2 = Item("A POLISHED SWORD","A SWORD WITH A RAZOR STEEL EDGE","weapon",0,5)
armour2 = Item("STUDDED ARMOUR","REINFORCED LEATHER ARMOUR","armour",3,0)
potionH = Item("POTION","A FLASK FILLED WITH A RED POTION","potion",0,0)
