import pygame
import math
import random


class Markers():
    def __init__():
        
    def createMarker():


def startup():
    """
    Sets the gameboard.
    """
    print("ADVANCED TIC-TAC-TOE (And TIC-TAC)\n------------------------\n\n\nPlease see rules:")
    print("TIC-TAC-TOE (Type 1 OR TicTacToe): ")
    choice = input(f"WELCOME!!! Welcome~!!!\nThis is your host—SentientSock—back with—say it with me now (Game?):")
    if choice == "TicTacToe" or choice == 1 or choice == "1" or choice == "tictactoe":
        print("Tic-Tac-Toe!!! HAHAHA~!!! There you have it folks!\nNow, lets give it up for our contestent (X/O?):")
        # Tic Tac Toe BOARD and RULES
        return 1
    elif choice == "TicTac" or choice == 2 or choice == "2" or choice == "tictac":
        print("Tic-Tac? HAHA! You are an enigma, well then... Im just\nthe host, what say do I have? Alright then,\nMiss Pena, please bring up the board, would you be so kind~")
        holdernumberonehun = input("PRESS ENTER TO START (-e- to exit)")
        if######make sure to recheck its not done
    else:


"""

NOTE: These lines are taken from the prior digital rain lab and I am using
it as a basis from which I am to base things off of. Additionally, I am 
researching the many ways that I can go about doing tic tac toe through Python
and from what I have gathered, my originally intended method of cycling through
an array (0-8) is inefficient. Additionally, it seems that pygame allows for
Events on clicks, which makes some things much easier!

"""
def main():
    pygame.init()
    pygame.display.set_caption("ADVANCED Tic-Tac-Toe (and Tic-Tac)")
    clock = pygame.time.Clock()
    dt = 0
    pygame.display.set_mode(size=(800,600))
    resolution = pygame.display.get_window_size()
    screen = pygame.display.set_mode((resolution), pygame.RESIZABLE)
    rain = Rain(resolution)
    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                # Update the screen size
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        # Game logic
        rain.update(dt)
        # Render & Display
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        rain.draw(screen)
        pygame.display.flip()
        # print(particle.age)
        dt = clock.tick(12)
    pygame.quit()



if __name__ == "__main__":
    main()

