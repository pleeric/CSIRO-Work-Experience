import numpy as np
import pygame
import time
Grid =  np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],dtype=bool)

displacesurface = pygame.display.set_mode([1280,720])

ColourOn = (255,255,0)
ColourOff = (127,127,127)



def GetNeighbours(x,y):
    NumberOfNeighbours = 0
    for a in range(x-1,x+2):
        for b in range(y-1,y+2):
            if a < 0 or b < 0 or a > 8 or b > 8:
                continue
            if Grid[a][b] == 1:
                NumberOfNeighbours += 1
            
    return NumberOfNeighbours



def UpdateGrid(Grid):
    NewBoard = np.zeros(Grid.shape)
    for x in range(len(Grid)):
        for y in range(len(Grid)):
            if Grid[x][y] == 1 and GetNeighbours(x,y) in [2,3]:
                NewBoard[x,y] = 1
            elif Grid[x][y] == 0 and GetNeighbours(x,y) == 3:
                NewBoard[x,y] = 1
            elif Grid[x][y] == 1 and GetNeighbours(x,y) > 3:
                NewBoard[x][y] = 0
            elif Grid[x][y] == 1 and GetNeighbours < 2:
                NewBoard[x][y] = 0
    Grid = NewBoard
    return NewBoard

def DisplayGrid():
    for x,y in np.ndindex(Grid.shape):
        x_position = x*50
        y_position = y*50
        if Grid[x][y] == 1:
            pygame.draw.rect(displacesurface, ColourOn, [x_position,y_position,x+50,y+50])
        else:
            pygame.draw.rect(displacesurface, ColourOff, [x_position,y_position,x_position+50,y_position+50])




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    DisplayGrid()
    print("hi")
    UpdateGrid(Grid)
    time.sleep(1)




