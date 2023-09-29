
class Piece:
    def __init__(self, x: int, y: int, color, type):
        self.x = x
        self.y = y
        if not (color == 'black' or color == 'white'):
            raise ValueError('Invalid color')
        self.color = color

        if not (type == 'pawn' or type == 'rook' or type == 'knight' or type == 'bishop' or type == 'king' or type == 'queen'):
            raise ValueError('Invalid piece')
        self.type = type


class Board:

    #board_arr =[[]]

    def __place_piece(self, piece: Piece):
        self.board_arr[piece.x][piece.y] = piece

    def __remove_piece(self, piece: Piece):
        self.board_arr[piece.x][piece.y] = 0

    def __move_piece(self, x: int, y: int, piece: Piece):
        self.__remove_piece(piece)
        piece.x = x
        piece.y = y
        self.__place_piece(piece)

    def __init__(self):
        self.board_arr = [[0 for y in range(8)] for x in range(8)]
        for x in range(8):
            self.__place_piece(Piece(x,1,'black','pawn'))
            self.__place_piece(Piece(x,6,'white','pawn'))
        self.__place_piece(Piece(0,0,'black','rook'))
        self.__place_piece(Piece(7,0,'black','rook'))
        self.__place_piece(Piece(0,7,'white','rook'))
        self.__place_piece(Piece(7,7,'white','rook'))
        self.__place_piece(Piece(1,0,'black','knight'))
        self.__place_piece(Piece(6,0,'black','knight'))
        self.__place_piece(Piece(1,7,'white','knight'))
        self.__place_piece(Piece(6,7,'white','knight'))
        self.__place_piece(Piece(2,0,'white','bishop'))
        self.__place_piece(Piece(5,0,'white','bishop'))
        self.__place_piece(Piece(2,7,'black','bishop'))
        self.__place_piece(Piece(5,7,'black','bishop'))
        self.__place_piece(Piece(3,0,'black','queen'))
        self.__place_piece(Piece(3,7,'white','queen'))
        self.__place_piece(Piece(4,0,'black','king'))
        self.__place_piece(Piece(4,7,'white','king'))
        self.selected = 0
        self.highlighted = []
    def __moves(self): # returns list of moves
        0
    
    def __highlight(self, remove_highlight = False): # (de-)highlights possible moves on select
        0
    
    def select_piece(self, x: int, y: int):
        if self.board_arr[x][y] == 0:
            return
        self.selected = self.board_arr[x][y]

    def move_piece(self, x: int, y: int):
        0

    def get_board(self):
        return self.board_arr
    def get_selected(self):
        return self.selected
    def get_highlighted(self):
        return self.highlighted