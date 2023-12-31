import sys
import pygame
import board 

class Draw:
    def __init__(self):
        # take assets from assets folder
        self.texture = pygame.image.load('assets/ChessAssets.png')
        # create a dictionary of all the pieces
        self.pieces = {}
        self.pieces['white_pawn'] = self.texture.subsurface((48, 40, 13, 16))
        self.pieces['black_pawn'] = self.texture.subsurface((62, 40, 13, 16))
        self.pieces['white_rook'] = self.texture.subsurface((77, 39, 13, 17))
        self.pieces['black_rook'] = self.texture.subsurface((91, 39, 13, 17))
        self.pieces['white_knight'] = self.texture.subsurface((45, 63, 17, 17))
        self.pieces['black_knight'] = self.texture.subsurface((63, 63, 17, 17))
        self.pieces['white_bishop'] = self.texture.subsurface((95, 61, 13, 19))
        self.pieces['black_bishop'] = self.texture.subsurface((81, 61, 13, 19))
        self.pieces['white_queen'] = self.texture.subsurface((48, 83, 13, 21))
        self.pieces['black_queen'] = self.texture.subsurface((62, 83, 13, 21))
        self.pieces['white_king'] = self.texture.subsurface((78, 81, 13, 23))
        self.pieces['black_king'] = self.texture.subsurface((92, 81, 13, 23))
        self.tiles = self.texture.subsurface((72, 0, 32, 32))
        self.board = pygame.Surface((128, 128))
        for i in range(0, 4):
            for j in range(0, 4):
                self.board.blit(self.tiles, (32 * i, 32 * j))

    # @param
    # screen: SE
    # board_arr: 2d array with pieces
    # selected_piece: [x,y] of the selected piece 
    # highlighted_squares: arr of [x,y] of highlited squares
    # taken = []: arr of Piece objects that have been taken
    def __draw_board(self, screen: pygame.Surface, board_arr: list, selected_piece: list, highlighted_squares: list, taken = []):
        canvas = pygame.Surface((192, 192))
        canvas.blit(self.board, (32, 32))
        highlight = [self.texture.subsurface(2, 0, 1, 1), self.texture.subsurface(3, 0, 1, 1)]
        highlight = [pygame.transform.scale(highlight[0], (16, 16)), pygame.transform.scale(highlight[1], (16, 16))]
        for square in highlighted_squares:
            canvas.blit(highlight[(square[0] + square[1]) % 2], (32 + 16 * square[0], 32 + 16 * square[1]))
        for x in range(0, 8):
            for y in range(0, 8):
                if board_arr[x][y] != 0:
                    piece = self.pieces[board_arr[x][y].color + '_' + board_arr[x][y].type]
                    w, h = piece.get_size()
                    canvas.blit(piece, (40 + 16 * x - w/2, 44 + 16 * y - h - (selected_piece == [x, y]) * 6))
        wt, bt = 32, 32
        for type in ['queen', 'rook', 'knight', 'bishop', 'pawn']:
            w = self.pieces['white_' + type].get_size()[0] / 2
            wl = 20 - w
            wr = 172 - w
            for piece in taken:
                if piece.type == type:
                    if piece.color == 'white':
                        canvas.blit(self.pieces['white_' + type], (wl, wt))
                        wt += 8
                    else:
                        canvas.blit(self.pieces['black_' + type], (wr, bt))
                        bt += 8
        canvas = pygame.transform.scale(canvas, (768, 768))
        screen.blit(canvas, (0, 0))
    
    # a simpler interface for draw_board()
    # @param
    # screen: SE
    # board: SE
    def draw_board(self, screen: pygame.Surface, board: board.Board):
        self.__draw_board(screen, board.get_board_arr(), board.get_selected(), board.get_highlighted(), board.get_taken())
        pygame.display.update()

    def promotion(self, screen: pygame.Surface, player):
        canvas = pygame.Surface((16 * 4, 24))
        canvas.blit(self.pieces[player + '_knight'], (8 - self.pieces[player + '_knight'].get_size()[0] / 2, 24 - self.pieces[player + '_knight'].get_size()[1]))
        canvas.blit(self.pieces[player + '_bishop'], (24 - self.pieces[player + '_bishop'].get_size()[0] / 2, 24 - self.pieces[player + '_bishop'].get_size()[1]))
        canvas.blit(self.pieces[player + '_rook'], (40 - self.pieces[player + '_rook'].get_size()[0] / 2, 24 - self.pieces[player + '_rook'].get_size()[1]))
        canvas.blit(self.pieces[player + '_queen'], (56 - self.pieces[player + '_queen'].get_size()[0] / 2, 24 - self.pieces[player + '_queen'].get_size()[1]))
        canvas = pygame.transform.scale(canvas, (64 * 4, 96))
        screen.blit(canvas, (256, (768 - 128) * (player == 'black')))
        pygame.display.update()

if __name__ == '__main__':
    #test textures
    board_obj = board.Board()
    draw_obj = Draw()
    pygame.init()
    screen = pygame.display.set_mode((768, 768))
    screen.fill((0, 0, 0))
    draw_obj.draw_board(screen, board_obj)
    pygame.display.update()
    board_obj.update_moves()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # on click, lowers king and calls draw_board()
                print('click')
                board_obj.select_piece(4,4, 'black')
                draw_obj.draw_board(screen, board_obj)
