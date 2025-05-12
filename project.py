import pygame, sys
import numpy as np

## Global Variables: Act as an easy way to change code later on...
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
SPACE = 55
CIRCLEW = 15
CROSSW = 25
CIRCLER = 60
BG_COLOR = (245, 245, 220)
LINE_COLOR = (122, 118, 104)
CIRCLE_COLOR = (131, 163, 122)
WIN_LINE_WIDTH = 15
CROSS_COLOR = (66, 66, 66)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLER, CIRCLEW)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSSW)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSSW)
            else: pass
        #
    #
#
## Lines that create visual 'game board'...
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (600, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (600, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, 600), LINE_WIDTH)

def main():
    game_over = False
    player = 1
    win_counter = 0
    loss_counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                print("Thank you for playing! We'll See you next time on:\nTIC TAC TOE!!!")
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clCol = int(mouseX // SQUARE_SIZE)
                clRow = int(mouseY // SQUARE_SIZE)
                if av_square(clRow, clCol):
                    mark_square(clRow, clCol, player)
                    if check_win(player):
                        game_over = True
                    player = player % 2 + 1
                    draw_figures()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restart()
                        player = 1
                        game_over = False
                        #
                if event.type == pygame.WINDOWRESIZED or event.type == pygame.VIDEORESIZE:
                    screen.fill(BG_COLOR)
                    draw_lines()
                    draw_figures()
                    pygame.display.update()
            pygame.display.update()
            #
        #
    #
#

if __name__ == "__main__":
    introduction()
    pygame.init()
    ## Screen! Gotta be visible to play...
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption('XTREEME Tic-Tac-Toe!!!')
    screen.fill(BG_COLOR)
    ## Called a console board, this was kind of weird to learn
    ## Really not as intuitive as other 'pieces' of code...
    board = np.zeros((BOARD_ROWS, BOARD_COLS))
    ## MAIN! This is the big ol' chunk of code that plays the game...
    main()