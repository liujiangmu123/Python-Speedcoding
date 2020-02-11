from Vab import *
pygame.init()

x1, y1 = WIDTH - 50, 10
x2, y2 = WIDTH - 50, HEIGHT - 10

x3, y3 = 100, HEIGHT // 2
x4, y4 = WIDTH - 10, HEIGHT // 2

def line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0:
        return createVector(0, 0)

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

    pt = createVector()
    pt.x = x1 + t * (x2 - x1)
    pt.y = y1 + t * (y2 - y1)

    return [pt, u]

intersection_vector = line_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
intersection_vector[0].to_integer()

run = True
while run:
    mouseX, mouseY = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    x4, y4 = mouseX, mouseY

    intersection_vector = line_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
    intersection_vector[0].to_integer()

    pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2))
    pygame.draw.line(screen, (255, 255, 255), (x3, y3), (x4, y4))

    pygame.draw.ellipse(screen, (255, 0, 0) if intersection_vector[1] > 1 else (0, 255, 0), (intersection_vector[0].x - 5, intersection_vector[0].y - 5, 10, 10))

    pygame.display.update()

pygame.quit()
