from Vab import *

class Button: # Button class from my 2048 pygame version of dan's version
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    def draw(self):
        pygame.draw.rect(screen, (60, 60, 60), (self.x, self.y, self.w, self.w))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.w), 2)


    def is_clicked(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if x > self.x and x < self.x + self.w:
            if y > self.y and y < self.y + self.w:
                return True

        return False