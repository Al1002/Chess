#must take the board from board_manipulator and draw it in the game window
import pygame
import board
import sys

class Draw:
    def __init__(self, board, selected_piece, highlighted_squares):
        self.board_data = board
        self.selected_piece = selected_piece
        self.highlighted_squares = highlighted_squares
        # take assets from assets folder
        texture = pygame.image.load('assets/ChessAssets.png')
        # create a dictionary of all the pieces
        self.pieces = {}
        self.pieces['white_pawn'] = texture.subsurface((48, 40, 13, 16))
        self.pieces['black_pawn'] = texture.subsurface((62, 40, 13, 16))
        self.pieces['white_rook'] = texture.subsurface((77, 39, 13, 17))
        self.pieces['black_rook'] = texture.subsurface((91, 39, 13, 17))
        self.pieces['white_knight'] = texture.subsurface((45, 63, 17, 17))
        self.pieces['black_knight'] = texture.subsurface((63, 63, 17, 17))
        self.pieces['white_bishop'] = texture.subsurface((81, 61, 13, 19))
        self.pieces['black_bishop'] = texture.subsurface((95, 61, 13, 19))
        self.pieces['white_queen'] = texture.subsurface((48, 83, 13, 21))
        self.pieces['black_queen'] = texture.subsurface((62, 83, 13, 21))
        self.pieces['white_king'] = texture.subsurface((78, 81, 13, 23))
        self.pieces['black_king'] = texture.subsurface((92, 81, 13, 23))
        self.tiles = texture.subsurface((72, 0, 32, 32))
        self.board = pygame.Surface((128, 128))
        for i in range(0, 4):
            for j in range(0, 4):
                self.board.blit(self.tiles, (32 * i, 32 * j))

    def draw_board(self):
        canvas = pygame.Surface((192, 192))
        canvas.blit(self.board, (32, 32))
        for x in range(0, 8):
            for y in range(0, 8):
                if self.board_data[x][y] != 0:
                    piece = self.pieces[self.board_data[x][y].color + '_' + self.board_data[x][y].type]
                    w, h = piece.get_size()
                    canvas.blit(piece, (40 + 16 * x - w/2, 44 + 16 * y - h))

        
        canvas = pygame.transform.scale(canvas, (768, 768))
        screen.blit(canvas, (0, 0))

if __name__ == '__main__':
    #test textures
    board_data = board.Board().get_board()
    d = Draw(board_data, '', '')
    pygame.init()
    screen = pygame.display.set_mode((768, 768))
    screen.fill((0, 0, 0))
    d.draw_board()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()