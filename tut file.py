import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('pygame')
install('tk')

import pygame
import time
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('Instructions','This is Conways Game of life. It is a zero player game.\nThe Rules are simple \n1. If a cell has less than 2 neighbours or more than 3 neighbors it will die. \n2. If a dead cell has exactly 3 neighbours alive, it will come back to life. \nTo play the game, select the initial cells to be kept alive, press enter and then.. watch the generations grow \n TIP: Plot your generations in the middle of the screen as the game of life is played on a infinite plane')

BLACK = (0, 0, 0)
WHITE = (0, 0, 0)
GREEN = (255, 255, 255)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
def board(n):
    bo = [[0]*n for i in range(n)]
    return bo
grid = board(50)
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)

alt_grid = board(len(grid))
# Initialize pygame
pygame.init()

screen_size = len(grid)*25
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [screen_size+200,screen_size]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def show_board(bo):
    for i in range(len(bo)):
        print(bo[i])
    return
def next_turn_blocks(bo):

    alive_cell = []

    for i in range(1,len(bo)-1):
        for j in range(1, len(bo)-1):
            count = 0

            if bo[i][j] == 0:

                for x in range(-1,2):
                    for y in range(-1,2):

                        if x == 0 and y ==0:
                            continue

                        if bo[i+x][j+y] == 1:
                            count += 1

                if count == 3:
                    alive_cell.append((i,j))

            if bo[i][j] == 1:

                for x in range(-1, 2):
                    for y in range(-1, 2):

                        if x == 0 and y ==0:
                            continue

                        if bo[i + x][j + y] == 1:
                            count += 1

                if count ==3 or count ==2:
                    alive_cell.append((i,j))

    return alive_cell


curr_grid = grid
# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            curr_grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:

                done2 = False

                while not done2:
                    for event in pygame.event.get():  # User did something
                        if event.type == pygame.QUIT:  # If user clicked close
                            done = True
                            done2 = True

                    screen.fill(BLACK)

                    alive_cell = next_turn_blocks(grid)
                    print(alive_cell)

                    alt_grid = board(len(grid))

                    grid = board(len(grid))

                    for i in alive_cell:
                        grid[i[0]][i[1]] = 1

                    show_board(grid)
                    print('')

                    # Draw the grid
                    for row in range(len(grid)):
                        for column in range(len(grid)):
                            color = WHITE
                            if grid[row][column] == 1:
                                color = GREEN
                            pygame.draw.rect(screen,
                                             color,
                                             [(MARGIN + WIDTH) * column + MARGIN,
                                              (MARGIN + HEIGHT) * row + MARGIN,
                                              WIDTH,
                                              HEIGHT])


                    # Limit to 60 frames per second
                    clock.tick(60)

                    # Go ahead and update the screen with what we've drawn.
                    pygame.display.flip()
                    time.sleep(0.5)




    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(len(grid)):
        for column in range(len(grid)):
            color = WHITE
            if curr_grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('Fun facts','I hope you enjoyed your generations grow into seemingly amazing patterns. This game of life is amazing not only because it produces amazing patterns, but it also shows a big flaw in our preception of theories. We always assume that given a initial state of the system and the rules which governs it, we will be able to predict the future state at any finite instance. But this game gives us both, an initial state and the rules which governs the system, yet it is impossible to say if a inital generation will be stable, die out, or will keep on oscilating.')
