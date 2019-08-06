import pygame
from Entities import *
import math

# TO DO LIST:
# CREATE A COPY OF SELECTED ITEMS
# 
# 
# 
# 


def main():
    pygame.init()
    window = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Chess")
    window.fill((255, 255, 255))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()

    size = int(math.sqrt((400 * 400) / 64))
    grid = Grid(400, 400, size).grid

    background_image = pygame.image.load("./images/board2.png").convert()

    selected = Tile(0, 0)
    #Rename this variable
    # old = None

    grid[0][0].entity = "Q"
    grid[0][6].entity = "B"
    grid[5][6].entity = "R"
    grid[0][1].entity = "K"
    grid[6][6].entity = "P"
    availableMoves = []
    x = 0
    y = 0

    turn = "white"

    running = True
    while running:

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False
            elif(event.type == pygame.MOUSEBUTTONUP):
                mousepos = pygame.mouse.get_pos()
                # print(mousepos[0])
                # print(mousepos[1])
                x = int(mousepos[0]/50)
                y = int(mousepos[1]/50)
                # print(x)
                # print(y)
                # print(selected)

                #THE CODE BELOW WAS THE ORIGINAL VERSION. IT WORKS BUT SO COMPLICATED
                # if(selected.entity == None):
                #     selected.posx = grid[x][y].posx
                #     selected.posy = grid[x][y].posy
                #     selected.entity = grid[x][y].entity
                #     old = grid[x][y]

                #     availableMoves = getQueenMoves(grid, x, y)
                    
                # elif(grid[x][y] in availableMoves):
                #     # grid[x][y].posx = selected.posx
                #     # grid[x][y].posy = selected.posy
                #     grid[x][y].entity = selected.entity
                #     selected.entity = None
                #     selected.posx = None
                #     selected.posy = None
                #     old.entity = None
                #     availableMoves.clear()


                if(selected.entity == None):
                    selected = grid[x][y]
                    print(x)
                    availableMoves = selected.moves(grid, x, y, turn)
                    print(availableMoves)
                    
                else:
                    if(grid[x][y] in availableMoves):
                        grid[x][y].entity = selected.entity
                        selected.entity = None
                    else:
                        availableMoves.clear()


        # if selected.entity == 'Q':
        #     availableMoves = getQueenMoves(grid, x, y)
        #     print(len(availableMoves))
        # else:
        #     availableMoves.clear()


        # Draw everything:
        window.blit(background_image, [0, 0])

        if(selected.entity != None):
            pygame.draw.rect(window, (0, 191, 255), (selected.posx, selected.posy, size, size))

        for i in grid:
            for j in i:
                if(j in availableMoves and selected.entity != None):
                    pygame.draw.rect(window, (0, 0, 255), (j.posx + 5 , j.posy + 5 , size - 10 , size - 10))
                    # pygame.display.update()

                if(j.entity != None):
                    textsurface = myfont.render(j.entity, False, (0, 0, 0))
                    window.blit(textsurface,(j.posx + 25, j.posy + 25))

        pygame.display.update()
        window.fill((255, 255, 255))
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
