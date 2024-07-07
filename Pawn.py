space = "   "

class Pawn(Piece):
    def __init__(self, name, pos):
        super().__init__(name, pos)
        self.firstMove = True
        if self.returnColor() == "W":
            
        
    def hasMoved(self, move, rows):
        self.firstMove = False
        self.changePos(move)
        self.posMoves = self.getNewMoves(rows)
        print(f'New pos Moves: {self.posMoves}')
        
   """ def isEnemy(self, loc):
        color = self.returnColor()"""
        

    def getNewMoves(self, rows """Edit to be game Board"""):
        newMoves = []
        if self.returnName()[0] == "B":
            if rows.isSpace(self.returnPos()): #check front
                newMoves.append(move[0] + str(int(move[1]) - 1))
            if move[0] != "A":#check right diagonal
                if not rows.isSpace(self.returnPos())""" and rows.isEnemy(self.returnColor(), loc)""":
                    if rows[int(self.pos[1]) - 2][ord(self.pos[0]) - 64][0] == "W":
                        newMoves.append(ascii(ord(self.pos[0]) - 1) + self.pos[1])
            if self.pos[0] != "H": #check left diagonal
                if rows[int(self.pos[1]) - 2][ord(self.pos[0]) - 64] != space:
                    if rows[int(self.pos[1]) - 2][ord(self.pos[0]) - 64][0] == "W":
                        newMoves.append(ascii(ord(self.pos[0]) + 1) + self.pos[1])
            self.posMoves = newMoves
        else: #piece is white
            if rows[int(self.pos[1])][ord(self.pos[0]) - 65] == space:#check front
                newMoves.append(self.pos[0] + str(int(self.pos[1]) + 1))
            if self.pos[0] != "A":#check right diagonal
                if rows[int(self.pos[1])][ord(self.pos[0]) - 66] != space:
                    if rows[int(self.pos[1])][ord(self.pos[0]) - 64][0] == "B":
                        newMoves.append(ascii(ord(self.pos[0]) - 1) + str(int(self.pos[1]) + 1))
            if self.pos[0] != "H": #check left diagonal
                if rows[int(self.pos[1])][ord(self.pos[0]) - 64] != space:
                    if rows[int(self.pos[1])][ord(self.pos[0]) - 64][0] == "B":
                        newMoves.append(ascii(ord(self.pos[0]) + 1) + str(int(self.pos[1]) + 1))
            self.posMoves = newMoves
        
BPawn1 = Pawn('BP1', 'A7')
BPawn2 = Pawn('BP2', 'B7')
BPawn3 = Pawn('BP3', 'C7')
BPawn4 = Pawn('BP4', 'D7')
BPawn5 = Pawn('BP5', 'E7')
BPawn6 = Pawn('BP6', 'F7')
BPawn7 = Pawn('BP7', 'G7')
BPawn8 = Pawn('BP8', 'H7')
WPawn1 = Pawn('WP1', 'A2')
WPawn2 = Pawn('WP2', 'B2')
WPawn3 = Pawn('WP3', 'C2')
WPawn4 = Pawn('WP4', 'D2')
WPawn5 = Pawn('WP5', 'E2')
WPawn6 = Pawn('WP6', 'F2')
WPawn7 = Pawn('WP7', 'G2')
WPawn8 = Pawn('WP8', 'H2')
PawnList = []
PawnList.append(BPawn1)
PawnList.append(BPawn2)
PawnList.append(BPawn3)
PawnList.append(BPawn4)
PawnList.append(BPawn5)
PawnList.append(BPawn6)
PawnList.append(BPawn7)
PawnList.append(BPawn8)
PawnList.append(WPawn1)
PawnList.append(WPawn2)
PawnList.append(WPawn3)
PawnList.append(WPawn4)
PawnList.append(WPawn5)
PawnList.append(WPawn6)
PawnList.append(WPawn7)
PawnList.append(WPawn8)

def returnPawns():
    return PawnList

"""def getNewMoves(piece, move, rows):
    newMoves = []
    if piece.returnName()[0] == "B":
        if rows[int(move[1]) - 2][ord(move[0]) - 65] == space: #check front
            newMoves.append(move[0] + str(int(move[1]) - 1))
        if move[0] != "A":#check right diagonal
            if rows[int(move[1]) - 2][ord(move[0]) - 66] != space:
                if rows[int(move[1]) - 2][ord(move[0]) - 64][0] == "W":
                    newMoves.append(ascii(ord(move[0]) - 1) + move[1])
        if move[0] != "H": #check left diagonal
            if rows[int(move[1]) - 2][ord(move[0]) - 64] != space:
                if rows[int(move[1]) - 2][ord(move[0]) - 64][0] == "W":
                    newMoves.append(ascii(ord(move[0]) + 1) + move[1])
        return newMoves
    else: #piece is white
        if rows[int(move[1])][ord(move[0]) - 65] == space:#check front
            newMoves.append(move[0] + str(int(move[1]) + 1))
        if move[0] != "A":#check right diagonal
            if rows[int(move[1])][ord(move[0]) - 66] != space:
                if rows[int(move[1])][ord(move[0]) - 64][0] == "B":
                    newMoves.append(ascii(ord(move[0]) - 1) + str(int(move[1]) + 1))
        if move[0] != "H": #check left diagonal
            if rows[int(move[1])][ord(move[0]) - 64] != space:
                if rows[int(move[1])][ord(move[0]) - 64][0] == "B":
                    newMoves.append(ascii(ord(move[0]) + 1) + str(int(move[1]) + 1))
        return newMoves"""
