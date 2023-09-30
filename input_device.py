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
            print(x)
            print(y)
            if x in range (8) and y in range (8):
                return [x,y]
    return 0

