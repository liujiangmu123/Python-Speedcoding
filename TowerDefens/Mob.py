from Vab import *
pygame.init()

class Mob:
    def __init__(self, startCol, startRow, map):
        self.startPos = createVector(startCol, startRow)
        self.pos = self.startPos.copy()
        self.pos.mult(FIELDSIZE)

        self.map = map
        self.live = 20

        self.movementSpeed = 1
        self.movementCounter = 0
        self.maxMovementCounter = 2
        self.moveDir = createVector(0, 0)
        self.currentCell = 0
        self.nextCell = 1

    def show(self):
        screen.blit(
            pygame.font.SysFont("arial", 16).render(
                f"{self.live} hp", True, (0, 0, 0)
            ),
            (self.pos.x + 10, self.pos.y + 6)
        )
        pygame.draw.circle(screen, (255, 0, 255), (self.pos.x + FIELDSIZE // 2, self.pos.y + FIELDSIZE // 2 + 10), FIELDSIZE // 4, 0)
        pygame.draw.circle(screen, (0, 0, 0), (self.pos.x + FIELDSIZE // 2, self.pos.y + FIELDSIZE // 2 + 10), FIELDSIZE // 4, 2)

    def update(self):
        self.movementCounter += 1

        nextCellCol, nextCellRow = self.map[self.nextCell][0], self.map[self.nextCell][1]
        currCellCol, currCellRow = self.map[self.currentCell][0], self.map[self.currentCell][1]

        if self.movementCounter == self.maxMovementCounter:
            self.movementCounter = 0

            distanceCol = nextCellCol - currCellCol
            distanceRow = nextCellRow - currCellRow

            self.moveDir.set(distanceCol * self.movementSpeed, distanceRow * self.movementSpeed)

            self.pos.add(self.moveDir)

        if self.pos.x > nextCellCol * FIELDSIZE or self.pos.y > nextCellRow * FIELDSIZE:
            self.currentCell = self.nextCell
            self.nextCell += 1

            #self.moveDir.set(0, 0)



