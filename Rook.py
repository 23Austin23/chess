class Rook:
    def __init__(self, name, pos, can_attack):
        self.name = name
        self.pos = pos
        self.can_attack = can_attack

    def returnRookCanAttack(self):
        return self.can_attack

    def returnPos(self):
        return self.pos
    
    def changePos(self, pos):
        self.pos = pos
        
    def returnName(self):
        return self.name

WRook1 = Rook('WR1', 'A1', False)
WRook2 = Rook('WR2', 'H1', False)
BRook1 = Rook('BR1', 'A8', False)
BRook2 = Rook('BR2', 'H8', False)
RookList = []
RookList.append(WRook1)
RookList.append(WRook2)
RookList.append(BRook1)
RookList.append(BRook2)

def returnRooks():
    return RookList