from EvaluatingPiWithCollisions.Vab import *

class Block:
    def __init__(self, x, width, mass, velocity):
        self.x = x
        self.y = theHeight - width
        self.w = width
        self.m = mass
        self.v = velocity

    def hitWall(self):
        return self.x <= 0

    def reverse(self):
        self.v *= -1

    def collide(self, other):
        return not (self.x + self.w < other.x or self.x > other.x + other.w)

    def bounce(self, other):
        sumM = self.m + other.m
        newV = (self.m - other.m) / sumM * self.v
        newV += (2 * other.m / sumM) * other.v

        return newV

    def update(self):
        self.x += self.v

    def show(self):
        screen.blit(pygame.transform.scale(blockImg, (self.w, self.w)), (self.x, self.y))