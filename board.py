
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

    board_arr =[[]]

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
        for y in range(8):
            self.__place_piece(Piece(1,y,'black','pawn'))
            self.__place_piece(Piece(6,y,'white','pawn'))
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