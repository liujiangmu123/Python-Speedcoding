from Vab import *

class Point: # dragable points
    def __init__(self, x, y, w=10):
        self.v = createVector(x, y)
        self.w = w

        self.color = (0, 255, 0)
        self.dragged = False

        self.state = "drag"

    def show(self):
        pygame.draw.circle(screen, self.color, (self.v.x, self.v.y), self.w)

    def update(self):
        if self.dragged:
            x, y = pygame.mouse.get_pos()

            if y <= FIELDHEIGHT and self.v.y <= FIELDHEIGHT:
                self.v.set(x, y)

    def isMouseInCircle(self, pos):
        x, y = pos
        rectX, rectY = self.v.x - self.w // 2, self.v.y - self.w // 2

        if rectX < x < rectX + self.w:
            if rectY < y < rectY + self.w:
                if self.state == "drag":
                    self.color = (255, 255, 0)
                if self.state == "delete":
                    self.color = (255, 0, 0)
                if self.state == "create":
                    self.color = (0, 255, 0)

                return True

        self.color = (0, 255, 0)
        return False
