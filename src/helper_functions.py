from ChessUnit import *


GRID = [[[0 + i * 50, 0 + j * 50, None] for i in range(8)] for j in range(8)]
selectedUnit = None
wTurn = True


def redrawSquare(windowSurfaceObj):
    pos = pygame.mouse.get_pos()
    color = (0, 0, 0)
    if (pos[0] // 50) % 2 == 0 and (pos[1] // 50) % 2 == 0:
        color = (255, 255, 255)
    if (pos[0] // 50) % 2 == 1 and (pos[1] // 50) % 2 == 1:
        color = (255, 255, 255)

    rect = pygame.Rect((pos[0] // 50) * 50, (pos[1] // 50) * 50, 50, 50)
    pygame.draw.rect(windowSurfaceObj, color, rect)

    selectedUnit = getUnitByPos(pos)
    if selectedUnit:
        windowSurfaceObj.blit(selectedUnit.image, selectedUnit.pos)


def clearSquare(selectedUnit, windowSurfaceObj):
    color = (0, 0, 0)
    if (selectedUnit.pos[0] // 50) % 2 == 0 and (selectedUnit.pos[1] // 50) % 2 == 0:
        color = (255, 255, 255)
    if (selectedUnit.pos[0] // 50) % 2 == 1 and (selectedUnit.pos[1] // 50) % 2 == 1:
        color = (255, 255, 255)
        
    rect = pygame.Rect((selectedUnit.pos[0] // 50) * 50,
                       (selectedUnit.pos[1] // 50) * 50, 50, 50)
    pygame.draw.rect(windowSurfaceObj, color, rect)


def removeUnitOnGRID(unit):
    x = (unit.pos[0] // 50)
    y = (unit.pos[1] // 50)
    GRID[y][x][2] = None


def getUnitByPos(pos):
    x = (pos[0] // 50)
    y = (pos[1] // 50)
    return GRID[y][x][2]


def addToGrid(unit):
    x = unit.pos[0] // 50
    y = unit.pos[1] // 50
    GRID[y][x] = [GRID[y][x][0], GRID[y][x][1], unit]


def drawWPawns(windowSurfaceObj):
    for i in range(8):
        wPawn = ChessUnit('./ChessAssets/w_Pawn.png')
        wPawn.pos = [0 + i * 50, 50]
        addToGrid(wPawn)
        windowSurfaceObj.blit(wPawn.image, (0 + i * 50, 50))


def drawWChessUnits(windowSurfaceObj):
    wBishop = ChessUnit('./ChessAssets/w_Bishop.png')
    wBishop.pos = [100, 0]
    addToGrid(wBishop)
    windowSurfaceObj.blit(wBishop.image, (100, 0))

    wBishop2 = ChessUnit('./ChessAssets/w_Bishop.png')
    wBishop2.pos = [250, 0]
    addToGrid(wBishop2)
    windowSurfaceObj.blit(wBishop2.image, (250, 0))

    wKing = ChessUnit('./ChessAssets/w_King.png')
    wKing.pos = [150, 0]
    addToGrid(wKing)
    windowSurfaceObj.blit(wKing.image, (150, 0))

    wKnight = ChessUnit('./ChessAssets/w_Knight.png')
    wKnight.pos = [50, 0]
    addToGrid(wKnight)
    windowSurfaceObj.blit(wKnight.image, (50, 0))

    wKnight2 = ChessUnit('./ChessAssets/w_Knight.png')
    wKnight2.pos = [300, 0]
    addToGrid(wKnight2)
    windowSurfaceObj.blit(wKnight2.image, (300, 0))

    drawWPawns(windowSurfaceObj)

    wQueen = ChessUnit('./ChessAssets/w_Queen.png')
    wQueen.pos = [200, 0]
    addToGrid(wQueen)
    windowSurfaceObj.blit(wQueen.image, (200, 0))

    wRook = ChessUnit('./ChessAssets/w_Rook.png')
    wRook.pos = [0, 0]
    addToGrid(wRook)
    windowSurfaceObj.blit(wRook.image, (0, 0))

    wRook2 = ChessUnit('./ChessAssets/w_Rook.png')
    wRook2.pos = [350, 0]
    addToGrid(wRook2)
    windowSurfaceObj.blit(wRook2.image, (350, 0))


def drawBPawns(windowSurfaceObj):
    for i in range(8):
        bPawn = ChessUnit('./ChessAssets/b_Pawn.png')
        bPawn.pos = [0 + i * 50, 300]
        addToGrid(bPawn)
        windowSurfaceObj.blit(bPawn.image, (0 + i * 50, 300))


def drawBChessUnits(windowSurfaceObj):
    bBishop = ChessUnit('./ChessAssets/b_Bishop.png')
    bBishop.pos = [100, 350]
    addToGrid(bBishop)
    windowSurfaceObj.blit(bBishop.image, (100, 350))

    bBishop2 = ChessUnit('./ChessAssets/b_Bishop.png')
    bBishop2.pos = [250, 350]
    addToGrid(bBishop2)
    windowSurfaceObj.blit(bBishop2.image, (250, 350))

    bKing = ChessUnit('./ChessAssets/b_King.png')
    bKing.pos = [150, 350]
    addToGrid(bKing)
    windowSurfaceObj.blit(bKing.image, (150, 350))

    bKnight = ChessUnit('./ChessAssets/b_Knight.png')
    bKnight.pos = [50, 350]
    addToGrid(bKnight)
    windowSurfaceObj.blit(bKnight.image, (50, 350))

    bKnight2 = ChessUnit('./ChessAssets/b_Knight.png')
    bKnight2.pos = [300, 350]
    addToGrid(bKnight2)
    windowSurfaceObj.blit(bKnight2.image, (300, 350))

    drawBPawns(windowSurfaceObj)

    bQueen = ChessUnit('./ChessAssets/b_Queen.png')
    bQueen.pos = [200, 350]
    addToGrid(bQueen)
    windowSurfaceObj.blit(bQueen.image, (200, 350))

    bRook = ChessUnit('./ChessAssets/b_Rook.png')
    bRook.pos = [0, 350]
    addToGrid(bRook)
    windowSurfaceObj.blit(bRook.image, (0, 350))

    bRook2 = ChessUnit('./ChessAssets/b_Rook.png')
    bRook2.pos = [350, 350]
    addToGrid(bRook2)
    windowSurfaceObj.blit(bRook2.image, (350, 350))


def drawChessBoard(windowSurfaceObj):
    for i in range(9):
        for j in range(9):
            rect = pygame.Rect(0 + j * 50, 0 + i * 50, 50, 50)
            if i % 2 == 0:
                if j % 2 == 0:
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
                pygame.draw.rect(windowSurfaceObj, color, rect)
            else:
                if j % 2 != 0:
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
            pygame.draw.rect(windowSurfaceObj, color, rect)


def initBoard(windowSurfaceObj):
    drawChessBoard(windowSurfaceObj)
    drawWChessUnits(windowSurfaceObj)
    drawBChessUnits(windowSurfaceObj)