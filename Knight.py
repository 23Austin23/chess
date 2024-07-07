class Knight:
    def __init__(self, name, pos, can_attack):
        self.name = name
        self.pos = pos
        self.can_attack = can_attack

    def returnKnightCanAttack(self):
        return self.can_attack

    def returnPos(self):
        return self.pos
    
    def changePos(self, pos):
        self.pos = pos
     
    def returnName(self):
        return self.name
        
WKnight1 = Knight('WN1', 'B1', False)
WKnight2 = Knight('WN2', 'G1', False)
BKnight1 = Knight('BN1', 'B8', False)
BKnight2 = Knight('BN2', 'G8', False)
KnightList = []
KnightList.append(WKnight1)
KnightList.append(WKnight2)
KnightList.append(BKnight1)
KnightList.append(BKnight2)

def returnKnights():
    return KnightList