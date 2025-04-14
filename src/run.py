import pygame
import sys
import os
from pygame.locals import *
from helper_functions import *


os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
fpsClock = pygame.time.Clock()


# CONFIG
WIDTH = 400
HEIGHT = 400
windowSurfaceObj = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')


def moveUnitOnBoard(pos):
    global selectedUnit
    global wTurn

    clearSquare(selectedUnit, windowSurfaceObj)
    removeUnitOnGRID(selectedUnit)
    posToMove = (pos[0] // 50) * 50, (pos[1] // 50) * 50
    selectedUnit.moveTo(posToMove)
    windowSurfaceObj.blit(selectedUnit.image, selectedUnit.pos)
    addToGrid(selectedUnit)
    selectedUnit = None
    wTurn = not wTurn


def boardClick():
    global selectedUnit
    global wTurn

    if event.type == MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pos = (pos[0] // 50) * 50, (pos[1] // 50) * 50
        color = (0, 127, 127)
        rect = pygame.Rect(pos[0], pos[1], 50, 50)
        pygame.draw.rect(windowSurfaceObj, color, rect)

        if getUnitByPos(pos):
            if getUnitByPos(pos).isWhite != wTurn:
                if selectedUnit:
                    if selectedUnit.checkMovement(pos):
                        moveUnitOnBoard(pos)
                return
            selectedUnit = getUnitByPos(pos)
        else:
            if selectedUnit:
                if selectedUnit.checkMovement(pos):
                    moveUnitOnBoard(pos)

    if event.type == MOUSEBUTTONUP:
        redrawSquare(windowSurfaceObj)


initBoard(windowSurfaceObj)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            boardClick()
            pygame.display.update()
            fpsClock.tick(30)
