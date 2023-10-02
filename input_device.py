import pygame

def input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1
        if event.type == pygame.MOUSEBUTTONUP: 
            if event.button != 1: # not left click
                pass
            print('click at x: ' + str(event.pos[0]) + ', y: ' + str(event.pos[1]))
            x = int((event.pos[0] - 128) / 64)
            y = int((event.pos[1] - 128) / 64)
            if x in range (8) and y in range (8):
                return [x,y]
    return 0

def promotion_input(color):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1
        if event.type == pygame.MOUSEBUTTONUP: 
            if event.button != 1:
                pass
            print('click at x: ' + str(event.pos[0]) + ', y: ' + str(event.pos[1]))
            selection = int((event.pos[0] - 128 - (2 * 64))/64)
            height = int((event.pos[1] + 32 - (768 - 128) * (color == 'white'))/64)
            pieces = ['knight','bishop','rook','queen']
            if height == 1 and selection in range(0,4):
                return pieces[selection]