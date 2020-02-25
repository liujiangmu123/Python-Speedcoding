'''
Evaluating Pi with Darts
Pi = 4 * (DartsInCircle / TotalDarts)

Github:
Youtube:
Wikipedia: https://en.wikipedia.org/wiki/Approximations_of_%CF%80

Creator: Ari24
'''

from EvaluatingPiWithDarts.Vab import * # or from Vab import *
import time
pygame.init()

radius = 200

total = 0
circle = 0

pi = 0

# Check if dart is in circle
def isDartInCircle(x, y, centerX, centerY, radius):
    dx = abs(x - centerX)
    dy = abs(y - centerY)

    if dx + dy <= radius:
        return True

    if dx > radius or dy > radius:
        return False

    if dx ** 2 + dy ** 2 <= radius ** 2:
        return True
    else:
        return False

screen.fill((0, 0, 0))
pygame.draw.ellipse(screen, (255, 255, 255), (0, 0, radius*2, radius*2), 4)
pygame.draw.rect(screen, (255, 255, 255), (0, 0, radius*2, radius*2), 4)
run = True
before = time.time()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    if not str(pi).startswith("3.1415"):
        for i in range(100):

            x = random.randint(WIDTH // 2 + -radius, WIDTH // 2 + radius)
            y = random.randint(HEIGHT // 2 + -radius, HEIGHT // 2 + radius)

            total += 1

            # Coloring the darts
            color = (255, 0, 0)

            if isDartInCircle(x, y, WIDTH // 2, HEIGHT // 2, radius):
                color = (100, 255, 0)
                circle += 1

            pi = 4 * (circle / total)

            screen.set_at((x, y), color)
            pygame.display.update()
    else:
        run = False

    print(pi)

after = time.time()

print(f"Pi is ca.: {pi}\nThis takes {after - before} seconds")
pygame.quit()

# Die Operation dauert ein wenig lange. Am besten lässt man es im Hintergrund laufen
