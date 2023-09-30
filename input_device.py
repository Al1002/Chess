import pygame

def input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return -1
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button != 1: # not left click
                pass        
            print('click at x: ' + str(event.pos[0]) + ', y: ' + str(event.pos[1]))
            return # TODO: return coordinates of clicked cell
    return 0

