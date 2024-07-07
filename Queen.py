class Queen:
    def __init__(self, name, pos, can_attack):
        self.name = name
        self.pos = pos
        self.can_attack = can_attack

    def returnCanAttack(self):
        return self.can_attack

    def returnPos(self):
        return self.pos
    
    def changePos(self, pos):
        self.pos = pos
        
    def returnName(self):
        return self.name

WQueen = Queen('WQ ', 'D1', False)
BQueen = Queen('BQ ', 'E8', False)

def returnQueens():
    return [WQueen, BQueen]