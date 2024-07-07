Divide = "|"
space = "   "
Line = "---"
Bottom = "___"

from Pawn import *
from Rook import *
from King import *
from Queen import *
from Knight import *
from Bishop import *

class GameBoard:
    def __init__(self, rows = [[], [], [], [], [], [], [], []]):
        self.rows = rows
        self.rows = self.setPieces()
    
    def returnPieces(self):
        pieces = []
        for item in self.rows:
            if item != space:
                pieces.append(item)
        return pieces
    
    def returnRows(self):
        return self.rows
        
    def setPieces(self):
        rows = self.rows
        for i in range(8):
            rows[0].append(space)
            rows[1].append(space)
            rows[2].append(space)
            rows[3].append(space)
            rows[4].append(space)
            rows[5].append(space)
            rows[6].append(space)
            rows[7].append(space)
            
        Pawns = returnPawns()
        kings = returnKings()
        Knights = returnKnights()
        queens = returnQueens()
        Rooks = returnRooks()
        Bishops = returnBishops()
        pieces = []
        for item in Pawns:
            pieces.append(item)
        for item in kings:
            pieces.append(item)
        for item in Knights:
            pieces.append(item)
        for item in queens:
            pieces.append(item)
        for item in Rooks:
            pieces.append(item)
        for item in Bishops:
            pieces.append(item)
        
        for item in pieces:
            #print(item.returnPos() + f' {item.returnPos()[1]} : {ord(item.returnPos()[0]) - 65}')
            rows[int(item.returnPos()[1]) - 1][ord(item.returnPos()[0]) - 65] = item
        return rows
        
        def isSpace(self, loc):
            rows = self.returnRows()
            return rows[int(loc[1])][ord(loc[0]) - 65] == space
        
    def gameBoardWithPieces(self):
        rows = self.rows
        i = 0
        print(Divide + Line, end = "")
        print(Divide + ' A ' + Divide + ' B ' + Divide + ' C ' + Divide + ' D ' + Divide + ' E ' + Divide + ' F ' + Divide + ' G ' + Divide + ' H ' + Divide + "\n" , end = '')
        n = 0
        print('|---|' + Line * 10 + '-|')
        row = 1
        for item in rows:
            print(f'| {row} |', end="")
            for item2 in item:
                if item2 == space:
                    print(item2 + Divide, end = "")
                else:
                    print(item2.returnName() + Divide, end = "")
            #print(Divide)
            print('\n' + '|---|' + Line * 10 + '-|')
            row += 1
        print(Divide + Line + Divide + ' A ' + Divide + ' B ' + Divide + ' C ' + Divide + ' D ' + Divide + ' E ' + Divide + ' F ' + Divide + ' G ' + Divide + ' H ' + Divide + "\n" , end = '')
        print('\n')

    def returnRows(self):
        return self.rows
        
    def spacify(self, move):
        self.rows[int(move[1]) - 1][ord(move[0]) - 65] = space

    def returnPieces(self):
        rows = self.returnRows()
        pieces = list()
        for row in rows:
            for piece in row:
                if piece != space:
                    pieces.append(piece)
        return pieces

def install(piece, rows):
    pos = piece.returnPos()
    rows[int(pos[1]) - 1][ord(pos[0]) - 65] = piece
    
    
    
def print_game_board():
    i = 0
    n = 0
    for n in range(11):
        print(Line, end = "")
    print(end = '\n')
    while i < 8:
        n = 0
        for n in range(8):
            print(Divide + space, end = "")
        print(Divide)
        n = 0
        for n in range(11):
            print(Line, end = "")
        print(end = '\n\n')
        i += 1


