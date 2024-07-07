"""A PvP Chess Game"""
""" Game Flow """
"""
Game loads with instructions.
Upon press of enter key, game board is shown.
White will go first.
Then black.
Play will alternate between players until either there is
insufficient material to continue, a resignation is requested,
a stalemate occures or a checkmatehas occured.
When one of these conditions have been met, game will end
and the winner will be announced, if applicable.
"""
from GameBoard import *

Space = "   "
player = 0
gameCon = 1
allowed = ["A", "B", "C", "D", "E", "F", "G", "H", "1", "2", "3", "4", "5", "6", "7", "8"]
def instructions():
    print("""
Hello! Thank you for choosing to play my chess game!
Here I will give you a run down of the rules:
There are no specials moves coded into this game.
All you can do are the basic moves of the pieces.
Now you can either win by checkmate or stalemate.

Here is the game board:""")
    print_game_board()

def presentCurrentBoard(board):
    """line1 = []
    line2 = []
    line3 = []
    line4 = []
    line5 = []
    line6 = []
    line7 = []
    line8 = []"""
    board.gameBoardWithPieces()
    '''line1, line2, line3, line4, line5, line6, line7, line8 = removeAndInstall('wr1', 8, 2, line1, line2, line3, line4, line5, line6, line7, line8)
    gameBoardWithPieces(line1, line2, line3, line4, line5, line6, line7, line8)'''

def getInputFirst(player, rows):
   # match = False
    move = input("Which piece would you like to move(A1 - H8): ").upper()
    while len(move) != 2:
        move = input("You did not enter the two character coordinate for your piece. Please try again: ").upper()
    if rows[int(move[1]) - 1][ord(move[0]) - 65] != space:
        if (player == 1 and rows[int(move[1]) - 1][ord(move[0]) - 65].returnName()[0] == "W") or (player == 0 and rows[int(move[1]) - 1][ord(move[0]) - 65].returnName()[0] == "B"):
            if move[0] in allowed and move[1] in allowed:
                    return move
            else:
                while not match:
                    print("Your selection was not valid, please select a piece")
                    move = input("Which piece would you like to move(A1 - H8): ").upper() #Assume A2 for testing
                    if move[0] in allowed and move[1] in allowed:
                        return move
    else:
        print("You did not select one of your pieces. Please try again.")
        return getInputFirst(player, rows)

def getMoveInput(piece, rows):
   # match = False
    move = input(f'Where would you like to move {piece.returnName()}: ').upper()
    while len(move) != 2:
        move = input("You did not enter the two character coordinate for your piece. Please try again: ").upper()
    posMoves = piece.returnPosMoves()
    if move in posMoves:
        piece.hasMoved(move, rows)
        return move
    else:
        while move not in posMoves:
            print(f'You did not enter a valid move for {piece.returnName()}. Please try again.')
            return getMoveInput(piece, rows)

def findNewMoves(piecesList):
    for piece in piecesList:
        piece.getNewMoves(rows)

def interface():
    gameBoard = GameBoard()
    player = 1
    match = False
    while(gameCon != 0):
        if(player == 1):
            print("Currently it is White's turn to move.\n")
            pieceName = "W"
        else:
            print("Currently it is Black's turn to move.\n")
            
            pieceName = "B"
        presentCurrentBoard(gameBoard)
        moveFrom = getInputFirst(player, gameBoard.returnRows()) #Checks if piece moved is players and is valid coordinate. 
        piece = gameBoard.returnRows()[int(moveFrom[1]) - 1][ord(moveFrom[0]) - 65]
        moveTo = getMoveInput(piece, gameBoard.returnRows())
        #Check if piece can move 
        #Clear space piece occupied
        holder = gameBoard.returnRows()[int(moveFrom[1]) - 1][ord(moveFrom[0]) - 65]
        gameBoard.spacify(moveFrom)
        #Change pos of piece
        #Update gameBoard with pos
        install(holder, gameBoard.returnRows())
        """Check the move, ensure it is valid and that the piece can move"""        """Piece has moved. Iterate through game pieces to find new available moves"""
        pieces = gameBoard.returnPieces()
        findNewMoves(pieces, gameBoard.returnRows())
        
        """Change player"""
        player = abs(player - 1)

interface()
