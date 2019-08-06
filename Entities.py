class Tile:
    def __init__(self, x, y):
        self.posx = x
        self.posy = y
        self.entity = None
    
    def moves(self, grid, x, y, turn):
        if(self.entity == 'Q'):
            return getQueenMoves(grid, x, y)
        elif(self.entity == 'B'):
            return getBishopMoves(grid, x, y)
        elif(self.entity == 'R'):
            return getRookMoves(grid, x, y)
        elif(self.entity == 'K'):
            return getKingMoves(grid, x, y)
        elif(self.entity == 'P'):
            return getPawnMoves(grid, x, y, turn)

class Grid:
    def __init__(self, x, y, size):
        self.grid = []
        
        # print(range(x, size))
        
        for i in range(0, x, size):
            self.grid.append([])
            for j in range(0, y, size):
                self.grid[len(self.grid)-1].append(Tile(i, j))

def getPawnMoves(grid, x, y, turn):
    allmoves = []


    if(turn == "white"):
        if(y == 0):
            print('Should be a Q now')
            grid[x][y].entity = 'Q'
        else:
            allmoves.append(grid[x][y - 1])

        
        try:
            if(grid[x+1][y-1].entity != None):
                allmoves.append(grid[x + 1][y - 1])
            if(grid[x-1][y-1].entity != None):
                allmoves.append(grid[x - 1][y - 1])
        except:
            pass

    print(allmoves)
    return allmoves

def getKingMoves(grid, x, y):
    allmoves = []

    if(y > 0):
        allmoves.append(grid[x][y - 1])
    if(y < 7):
        allmoves.append(grid[x][y + 1])
    if(x > 0):
        allmoves.append(grid[x - 1][y])
    if(x < 7):
        allmoves.append(grid[x + 1][y])
    if(x < 7 and y < 7):
        allmoves.append(grid[x + 1][y + 1])
    if(x < 7 and y > 0):
        allmoves.append(grid[x + 1][y - 1])
    if(x > 0 and y > 0):
        allmoves.append(grid[x - 1][y - 1])
    if(x > 0 and x < 7):
        allmoves.append(grid[x - 1][y + 1])
    

    return allmoves

def getQueenMoves(grid, x, y):
    allmoves = []

    allmoves.extend(getRightHorizonatal(grid, x, y))
    allmoves.extend(getLeftHorizontal(grid, x, y))
    allmoves.extend(getUp(grid, x, y))
    allmoves.extend(getDown(grid, x, y))
    allmoves.extend(getRightDown(grid, x, y))
    allmoves.extend(getRightUp(grid, x, y))
    allmoves.extend(getLeftUp(grid, x, y))
    allmoves.extend(getLeftDown(grid, x, y))
    if(None in allmoves):
        allmoves.remove(None)

    return allmoves

def getBishopMoves(grid, x, y):
    allmoves = []

    allmoves.extend(getRightDown(grid, x, y))
    allmoves.extend(getRightUp(grid, x, y))
    allmoves.extend(getLeftUp(grid, x, y))
    allmoves.extend(getLeftDown(grid, x, y))
    if(None in allmoves):
        allmoves.remove(None)

    return allmoves

def getRookMoves(grid, x, y):
    allmoves = []

    allmoves.extend(getRightHorizonatal(grid, x, y))
    allmoves.extend(getLeftHorizontal(grid, x, y))
    allmoves.extend(getUp(grid, x, y))
    allmoves.extend(getDown(grid, x, y))

    if(None in allmoves):
        allmoves.remove(None)

    return allmoves



def getRightHorizonatal(grid, x, y):
    availableMoves = []
    x = x + 1
    while x < 8:
        availableMoves.append(grid[x][y])

        if grid[x][y].entity != None:
            break
        x+=1
    return availableMoves

def getLeftHorizontal(grid, x, y):
    availableMoves = []
    x = x - 1
    while x >= 0:
        availableMoves.append(grid[x][y])

        if grid[x][y].entity != None:
            break
        x-=1
    return availableMoves

def getUp(grid, x, y):
    availableMoves = []
    y = y - 1
    while y >= 0:
        availableMoves.append(grid[x][y])

        if grid[x][y].entity != None:
            break
        y-=1
    return availableMoves

def getDown(grid, x, y):
    availableMoves = []
    y = y + 1
    while y <= 7:
        availableMoves.append(grid[x][y])

        if grid[x][y].entity != None:
            break
        y+=1
    return availableMoves

def getRightDown(grid, x, y):
    availableMoves = []
    x = x + 1
    y = y + 1
    while x <= 7 and y <= 7:
        availableMoves.append(grid[x][y])

        if grid[x] [y].entity != None:
            break
        x+=1
        y+=1
    return availableMoves

def getRightUp(grid, x, y):
    availableMoves = []
    x = x + 1
    y = y - 1
    while x <= 7 and y >= 0:
        availableMoves.append(grid[x][y])

        if grid[x] [y].entity != None:
            break
        x+=1
        y-=1
    return availableMoves

def getLeftUp(grid, x, y):
    availableMoves = []
    x = x - 1
    y = y - 1
    while x >= 0 and y >= 0:
        availableMoves.append(grid[x][y])

        if grid[x] [y].entity != None:
            break
        x-=1
        y-=1
    return availableMoves

def getLeftDown(grid, x, y):
    availableMoves = []
    x = x - 1
    y = y + 1
    while x >= 0 and y <= 7:
        availableMoves.append(grid[x][y])

        if grid[x] [y].entity != None:
            break
        x-=1
        y+=1
    return availableMoves










                
                
