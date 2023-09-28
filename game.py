import pygame
import input_device
import board
import draw

# tldr the game gives a copy of the board to 
# the player and runs input(), which will return 
# the updated board upon successful input (inludes select piece)

class Game_object:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = board.Board()
        self.player1 = input_device.Input_device()
        self.player2 = input_device.Input_device()
    
    def run(self):
        active_player = self.player1
        while self.running:
            input = active_player.input()
            if  input == -1:
                running = 0 # -1 is termination signal
            if input == 0:
                0 # does nothing
            else:
                self.board = input
                # change active input
            
            # draw.draw_board(self.board) 
            self.screen.fill("purple")
            pygame.display.flip()
            
            self.clock.tick(60)  # limits FPS to 60
        pygame.quit()

def start():
    game = Game_object()
    game.run()

