from copy import deepcopy

class Piece:
    def __init__(self, x: int, y: int, color, type):
        self.x = x
        self.y = y
        self.moves = []
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
        # an passant
        if piece.type == 'pawn' and abs(piece.x - x) == 1 and self.board_arr[x][y] == 0:
            self.__remove_piece(self.board_arr[x][piece.y])
        
        self.move_history.append((piece.color, piece.type, (piece.x, piece.y), (x, y)))
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
        else:
            if self.board_arr[x][y] == 0:
                return 0
            if color != self.board_arr[x][y].color:
                return [x,y]
            return 0
    
    def __add_move(self, moves: list, x: int, y: int, color):
        move = self.__check_move(x,y,color)
        if move != 0:
            moves.append(move)
        return moves
    
    # returns a list of moves for a given piece
    def __piece_create_moves(self, piece: Piece): # this function is a sin, but boy do i not care
        moves = []
        if piece.type == 'pawn':
            if piece.color == 'black':
                dir_y = 1
            else:
                dir_y = -1
            moves = self.__add_move(moves, piece.x, piece.y + dir_y, 0) # forward
            for dir_x in [-1, 1]:
                moves = self.__add_move(moves, piece.x + dir_x, piece.y + dir_y, piece.color) # captures
            if piece.y == 3.5 - 2.5 * dir_y and self.__check_move(piece.x, piece.y + dir_y, 0) != 0:
                moves = self.__add_move(moves, piece.x, piece.y + 2 * dir_y, 0) # double first move
            # no an pasant :( 
            # adding an passant
            if len(self.move_history) > 0:
                last_move = self.move_history[-1]
                if last_move[1] == 'pawn' and abs(last_move[3][1] - last_move[2][1]) == 2 and last_move[3][1] == piece.y and abs(last_move[3][0] - piece.x) == 1:
                    moves = self.__add_move(moves, last_move[3][0], last_move[3][1] + dir_y, 0) 
        if piece.type == 'bishop':
            for dir_x, dir_y in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                for i in range(1,8):
                    move = self.__check_move(piece.x + dir_x * i, piece.y + dir_y * i, 0)
                    if move == 0:
                        moves = self.__add_move(moves, piece.x + dir_x * i, piece.y + dir_y * i, piece.color)
                        break
                    moves.append(move)
        if piece.type == 'rook':
            for dir_x, dir_y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                for i in range(1,8):
                    move = self.__check_move(piece.x + dir_x * i, piece.y + dir_y * i, 0)
                    if move == 0:
                        moves = self.__add_move(moves, piece.x + dir_x * i, piece.y + dir_y * i, piece.color)
                        break
                    moves.append(move)
        if piece.type == 'queen':
            for dir_x, dir_y in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                for i in range(1,8):
                    move = self.__check_move(piece.x + dir_x * i, piece.y + dir_y * i, 0)
                    if move == 0:
                        moves = self.__add_move(moves, piece.x + dir_x * i, piece.y + dir_y * i, piece.color)
                        break
                    moves.append(move)
        if piece.type == 'king':
            for dir_x, dir_y in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                for i in [1]:
                    move = self.__check_move(piece.x + dir_x * i, piece.y + dir_y * i, 0)
                    if move == 0:
                        moves = self.__add_move(moves, piece.x + dir_x * i, piece.y + dir_y * i, piece.color)
                        break
                    moves.append(move)
        if piece.type == 'knight':
            for dir_x, dir_y in [[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]: 
                moves = self.__add_move(moves, piece.x + dir_x, piece.y + dir_y, 0)
                moves = self.__add_move(moves, piece.x + dir_x, piece.y + dir_y, piece.color)
        
        moves = self.__check4check(moves, piece.color, piece)
        return moves
    
    def __check4check(self, moves: list, colour, piece):
        #check if move puts the king in check
        #if so, remove it from the list

        if self.check_check == False: #to avoid recursion
            return moves

        to_remove = []

        for move in moves:
            sim_board = Board(False)
            sim_board.board_arr = deepcopy(self.board_arr)
            sim_board.__move_piece(move[0], move[1], sim_board.board_arr[piece.x][piece.y])
            sim_board.update_moves()
            if sim_board.__check4check_helper(colour):
                to_remove.append(move)  
        
        for move in to_remove:
            moves.remove(move)

        return moves
    
    def __check4check_helper(self, colour):
        #check if king is in check
        #if so, return True
        #else, return False
        
        for x in range(8):
            for y in range(8):
                piece = self.board_arr[x][y]
                if piece != 0:
                    if piece.color != colour:
                        for move in piece.moves:
                            if self.board_arr[move[0]][move[1]] != 0:
                                if self.board_arr[move[0]][move[1]].type == 'king':
                                    return True
                                
        return False
        
    def __init__(self, check_check = True):
        self.check_check = check_check
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
        self.__place_piece(Piece(2,0,'black','bishop'))
        self.__place_piece(Piece(5,0,'black','bishop'))
        self.__place_piece(Piece(2,7,'white','bishop'))
        self.__place_piece(Piece(5,7,'white','bishop'))
        self.__place_piece(Piece(3,0,'black','queen'))
        self.__place_piece(Piece(3,7,'white','queen'))
        self.__place_piece(Piece(4,0,'black','king'))
        self.__place_piece(Piece(4,7,'white','king'))
        self.selected = 0
        self.highlighted = []
        self.move_history = []
        #(colour, piece, (fx, fy), (tx, ty))
        
    def update_moves(self, colour = 0):
        any_moves = False
        for x in range(8):
            for y in range(8):
                piece = self.board_arr[x][y]
                if piece != 0:
                    piece.moves = self.__piece_create_moves(piece)
                    if len(piece.moves) > 0 and piece.color == colour:
                        any_moves = True
        return any_moves

    def select_piece(self, x: int, y: int, color):
        piece = self.board_arr[x][y]
        if piece == 0:
            return 0
        if piece.color != color:
            return 0
        if self.selected == [x, y]: # selecting already selected => disselect
            self.selected = 0
            self.highlighted = []
            return 1 
        self.selected = [x, y]
        self.highlighted = piece.moves
        return 1

    def move_piece(self, x: int, y: int, color):
        if [x,y] in self.board_arr[self.selected[0]][self.selected[1]].moves:
            rval = 1
            
            if self.board_arr[x][y] and self.board_arr[x][y].type == 'king':
                rval = 2
            self.__move_piece(x, y, self.board_arr[self.selected[0]][self.selected[1]])
            self.selected = 0
            self.highlighted = []
            return rval
        return 0

    def get_board_arr(self):
        return self.board_arr
    def get_selected(self):
        return self.selected
    def get_highlighted(self):
        return self.highlighted

if __name__ == "__main__":
    board_obj = Board()
    board_obj.select_piece(4,7, 'black')