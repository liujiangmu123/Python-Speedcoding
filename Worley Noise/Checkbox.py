from Vab import *

class CheckButton: # Check Box from my 2048 pygame version of dan's version
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.state = "on"
        self.w = w

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.w, self.w), 1)
        if self.state == "on":
            pygame.draw.line(screen, (255, 0, 255), (self.x, self.y), (self.x + self.w, self.y + self.w), 4)
            pygame.draw.line(screen, (255, 0, 255), (self.x + self.w, self.y), (self.x, self.y + self.w), 4)

    def is_clicked(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if x > self.x and x < self.x + self.w:
            if y > self.y and y < self.y + self.w:
                if self.state == "off":
                    self.state = "on"
                elif self.state == "on":
                    self.state = "off"