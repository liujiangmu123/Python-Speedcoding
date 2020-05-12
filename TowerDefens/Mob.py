from Vab import *
pygame.init()

class Mob:
    def __init__(self, startCol, startRow, map):
        self.startPos = createVector(startCol, startRow)
        self.pos = self.startPos.copy()
        self.pos.mult(FIELDSIZE)

        self.map = map
        self.live = 20.0

        self.movementSpeed = 2
        self.movementCounter = 0
        self.maxMovementCounter = 2
        self.moveDir = createVector(0, 0)
        self.currentCell = 0
        self.nextCell = 1

        self.worth = 10

    def show(self):
        screen.blit(
            pygame.font.SysFont("arial", 16).render(
                f"{float(self.live)}", True, (0, 0, 0)
            ),
            (self.pos.x + 5, self.pos.y + 6)
        )

        screen.blit(
            pygame.transform.scale(pygame.image.load("img/heart.png"), (20, 20)),
            (self.pos.x + 5 + len(str(float(self.live))) * 7, self.pos.y + 6)
        )

        pygame.draw.circle(screen, (255, 0, 255), (self.pos.x + FIELDSIZE // 2, self.pos.y + FIELDSIZE // 2 + 10), FIELDSIZE // 4, 0)
        pygame.draw.circle(screen, (0, 0, 0), (self.pos.x + FIELDSIZE // 2, self.pos.y + FIELDSIZE // 2 + 10), FIELDSIZE // 4, 2)

    def update(self):
        self.movementCounter += 1

        if self.movementCounter == self.maxMovementCounter:
            self.movementCounter = 0

            currentCol, currentRow = self.map[self.currentCell][0], self.map[self.currentCell][1]
            nextCol, nextRow = self.map[self.nextCell][0], self.map[self.nextCell][1]
            nextPos = createVector(nextCol, nextRow)
            nextPos.mult(FIELDSIZE)

            if not nextPos.x == self.pos.x:
                if nextPos.x > self.pos.x:
                    self.pos.add(createVector(self.movementSpeed, 0))
                else:
                    self.pos.add(createVector(-self.movementSpeed, 0))

            if not nextPos.y == self.pos.y:
                if nextPos.y > self.pos.y:
                    self.pos.add(createVector(0, self.movementSpeed))
                else:
                    self.pos.add(createVector(0, -self.movementSpeed))

            if self.pos.x == nextPos.x and self.pos.y == nextPos.y:
                self.currentCell += 1
                self.nextCell += 1

    def checkLastSpot(self):
        return self.map[self.currentCell][2] == "end"

    def takeDamage(self, amount):
        self.live -= amount

    def isDeath(self):
        return self.live <= 0


