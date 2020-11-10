#project based on https://www.youtube.com/watch?v=vnd3RfeG3NM&t=292s

import pygame
from checker.constants import WIDTH, HEIGHT
from checker.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')



def main():
    run = True
    clock = pygame.time.Clock() #put a clock who runs the game at a certain pace
    board = Board()
    
    #doing an event loop
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    
    board.draw_squares (WIN)   #passes my game window and draws 
    pygame.display.update() #updates the display of the game



    pygame.quit()

      



main ()

