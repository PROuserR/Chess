import pygame


class ChessUnit:
    pos = [0, 0]
    dead = False
    isWhite = False
    image = ''
    type = ''


    def __init__(self, imagePath):
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, (50, 50))
        if 'w_' in imagePath:
            self.isWhite = True

        if 'Bishop' in imagePath:
            self.type = 'Bishop'
        elif 'King' in imagePath:
            self.type = 'King'
        elif 'Knight' in imagePath:
            self.type = 'Knight'
        elif 'Pawn' in imagePath:
            self.type = 'Pawn'
        elif 'Queen' in imagePath:
            self.type = 'Queen'
        elif 'Rook' in imagePath:
            self.type = 'Rook'


    def checkMovement(self, pos):
        if self.type == 'Pawn':
            if self.isWhite:
                if pos[1] - self.pos[1] <= 100 and pos[0] == self.pos[0]:
                    return True
                elif pos[1] - self.pos[1] <= 50 and (pos[0] - self.pos[0] == 50 or pos[0] - self.pos[0] == -50):
                    return True
            else:
                if pos[1] - self.pos[1] >= -100 and pos[0] == self.pos[0]:
                    return True
                elif pos[1] - self.pos[1] >= -50 and (pos[0] - self.pos[0] == 50 or pos[0] - self.pos[0] == -50):
                    return True
        elif self.type == 'Rook':
            if pos[0] == self.pos[0] or pos[1] == self.pos[1]:
                return True
        elif self.type == 'Bishop':
            if abs(self.pos[0] - pos[0]) == abs(self.pos[1] - pos[1]):
                return True
        elif self.type == 'Queen':
            if abs(self.pos[0] - pos[0]) == abs(self.pos[1] - pos[1]):
                return True
            elif pos[0] == self.pos[0] or pos[1] == self.pos[1]:
                return True
        elif self.type == 'King':
            if abs(pos[0] - self.pos[0]) <= 50 and abs(pos[1] - self.pos[1]) <= 50:
                return True
        elif self.type == 'Knight':
            if abs(pos[0] - self.pos[0]) == 50 and abs(self.pos[1] - pos[1]) == 100:
                return True
            elif abs(pos[0] - self.pos[0]) == 100 and abs(self.pos[1] - pos[1]) == 50:
                return True

            
        return False


    def moveTo(self, posToMove):
        self.pos[0] = posToMove[0]
        self.pos[1] = posToMove[1]

