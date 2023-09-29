#TODO: implement public select_piece, move_piece and private __piece_update_moves

class Piece:
    def __init__(self, x: int, y: int, color, type):
        self.x = x
        self.y = y
        moves = []
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

    def __check_move(self, x: int, y: int, color): # checks if is of opposite color, 0 means empty, returns position
        if x < 0 or 7 < x or y < 0 or 7 < y:
            return 0
        if color == 0: 
            if self.board_arr[x][y] == 0:
                return [x,y]
            else:
                return 0
        if color != self.board_arr[x][y].color:
            return [x,y]
    
    def __add_move(self, moves: list, x: int, y: int, color):
        move = self.__check_move(x,y,color)
        if move != 0:
            moves.append(move)
        return moves

    def __piece_create_moves(self, piece: Piece):
        moves = []
        if piece.type == 'pawn':
            if piece.color == 'black':
                dir_y = 1
            else:
                dir_y = -1
            moves = self.__add_move(moves, piece.x, piece.y + dir_y, 0) # forward
            for dir_x in [-1, 1]:
                moves = self.__add_move(moves, piece.x + dir_x, piece.y + dir_y, piece.color) # captures
            if piece.y == 3.5 + 2.5 * dir_y and self.__check_move(piece.x, piece.y + dir_y, 0) != 0:
                moves = self.__add_move(moves, piece.x, piece.y + 2 * dir_y, piece.color) # double first move
            # no an pasant :(
        if piece.type == 'bishop':
            for dir_x, dir_y in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                for i in range(8):
                    move = self.__check_move(piece.x + dir_x * i, piece.y + dir_y * i, '')

    def __init__(self):
        self.board_arr = [[0 for y in range(8)] for x in range(8)]
        for y in range(8):
            self.__place_piece(Piece(1,y,'black','pawn'))
            self.__place_piece(Piece(6,y,'white','pawn'))
        self.selected = 0
        self.highlighted = []
        
    def select_piece(self, x: int, y: int):
        if self.board_arr[x][y] == 0:
            return
        self.selected = self.board_arr[x][y]

    