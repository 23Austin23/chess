class Bishop:
    def __init__(self, name, pos, can_attack):
        self.name = name
        self.pos = pos
        self.can_attack = can_attack

    def returnBishopCanAttack(self):
        return self.can_attack

    def returnPos(self):
        return self.pos
    
    def changePos(self, pos):
        self.pos = pos
        
    def returnName(self):
        return self.name

WBishop1 = Bishop('WB1', 'C1', False)
WBishop2 = Bishop('WB2', 'F1', False)
BBishop1 = Bishop('BB1', 'C8', False)
BBishop2 = Bishop('BB2', 'F8', False)
BishopList = []
BishopList.append(BBishop1)
BishopList.append(BBishop2)
BishopList.append(WBishop1)
BishopList.append(WBishop2)

def returnBishops():
    return BishopList