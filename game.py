import pygame
import input_device
import board
from draw import Draw
from pygame.display import gl_get_attribute
from pygame.mixer_music import play

class Game_object:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((768, 768))
        self.draw = Draw()
        self.clock = pygame.time.Clock()
        # self.running = True
        self.board = board.Board()
    
    def __switch_player(self, player):
        if player == 'white':
            return 'black'
        if player == 'black':
            return 'white'

    def run(self):
        player = 'white'
        self.board.update_moves()
        self.draw.draw_board(self.screen, self.board)
        game_change = 0
        view_change = 0
        pause = 0
        while True:
            input = input_device.input()
            if input == -1:
                break # -1 is termination signal
            if input == 0 or input == None:
                continue # if nothing happens, we do nothing
            if pause:
                continue

            if self.board.selected == 0 or self.board.get_selected() == [input[0], input[1]]:
                view_change = self.board.select_piece(input[0], input[1], player)
            else:
                if self.board.board_arr[input[0]][input[1]] !=0 and self.board.board_arr[input[0]][input[1]].color == player:
                    view_change = self.board.select_piece(input[0], input[1], player)
                else:
                    game_change = self.board.move_piece(input[0], input[1], player)

            if game_change:
                if not self.board.update_moves(self.__switch_player(player)):
                    print(player + ' won!')
                    pause = 1
                # do checkmate checks, alter moves accordingly
                # if an passant-able, add an passant move
                player = self.__switch_player(player)
                game_change = 0
                view_change = 1
            
            if view_change:
                self.screen.fill("purple")
                self.draw.draw_board(self.screen, self.board) 
                # pygame.display.flip() # redundant
                view_change = 0
            
            self.clock.tick(60)  # limits FPS to 60
        pygame.quit()

def start():
    game = Game_object()
    game.run()

