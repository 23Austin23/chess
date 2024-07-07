space = "   "

class Piece:
    def __init__(self, name, pos, posMoves = []):
        self.name = name
        self.pos = pos
        self.posMoves = posMoves
        
    def printAttributes(self):
        print(self.pos)
        print(self.name)
        print(posMoves)

    def returnPos(self):
        return self.pos
    
    def changePos(self, pos):
        self.pos = pos
        
    def returnName(self):
        return self.name
        
    def returnColor(self):
        return self.name[0]
    
    def returnPosMoves(self):
        return self.posMoves
        
    """ def isEnemy(self, loc):
        color = self.returnColor()"""