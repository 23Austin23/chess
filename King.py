space == '   '

class King:
    def __init__(self, name, pos, in_danger, can_attack):
        self.name = name
        self.pos = pos
        self.in_danger = in_danger
        self.can_attack = can_attack

    def returnKingCanAttack(self):
        return self.can_attack

    def returnKingInDanger(self):
        return self.in_danger

    def returnPos(self):
        return self.pos
    
    def changePos(self, pos):
        self.pos = pos
    
    def returnName(self):
        return self.name
    
    def hasMoved(self, move, rows):
        self.changePos(move)
        self.posMoves = self.getNewMoves(rows)
        print(f'New pos Moves: {self.posMoves}')
     
    def getNewMoves(self, rows):
        newMoves = []
        pos = self.returnPos()
        if self.returnName()[0] == "B":
            if rows[int(pos[1]) - 2][ord(pos[0]) - 65] == space: #check front
                newMoves.append(pos[0] + str(int(pos[0] - 1)))
            if move[0] != 'A': #check Right
                if rows[int(pos[1]) - 2][ord(pos[0] - 66]) != space:
                    if rows[int(pos[1] - 2)][ord(pos[0]) - 64][0] == 'W':
                        newMoves.append(ascii(ord(pos[0]) - 1) + pos[1])
                
WKing = King('WK ', 'E1', False, False)
BKing = King('BK ', 'D8', False, False)

def returnKings():
    return [WKing, BKing]
