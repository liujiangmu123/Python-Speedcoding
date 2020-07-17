from Vab import *
pygame.init()

rez = 20
cols = WIDTH // rez + 1
rows = HEIGHT // rez + 1

def color(rgb):
    return int(rgb), int(rgb), int(rgb)

def getState(a, b, c, d):
    return a * 8 + b * 4 + c * 2 + d * 1

def line(a, b):
    color_ = (
        255 - a.x if 255 - a.x > 0 else 0, b.x if b.x < 255 else 255, a.x + b.x if a.x + b.x < 255 else 255
    )
    pygame.draw.line(screen, color_, (a.x, a.y), (b.x, b.y), 1)


field = []
for i in range(cols):
    field.append([])
    for j in range(rows):
        field[i].append(
            math.floor(random.randint(0, 1))
        )

run = True
while run:
    screen.fill(color(0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            field = []
            for i in range(cols):
                field.append([])
                for j in range(rows):
                    field[i].append(
                        math.floor(random.randint(0, 1))
                    )

    for i in range(cols):
        for j in range(rows):
            strokeWeight = round(rez * 0.2)

            pygame.draw.circle(screen, color(10), (i*rez, j*rez), strokeWeight, strokeWeight)

    for i in range(cols-1):
        for j in range(rows-1):
            x = i * rez
            y = j * rez

            a = createVector(x + rez // 2, y)
            b = createVector(x + rez, y + rez // 2)
            c = createVector(x + rez // 2, y + rez)
            d = createVector(x, y + rez // 2)
            
            state = getState(field[i][j], field[i+1][j], field[i+1][j+1], field[i][j+1])

            if state == 1: line(c, d)
            elif state == 2: line(b, c)
            elif state == 3: line(b, d)
            elif state == 4: line(a, b)
            elif state == 5: line(a, d); line(b, c)
            elif state == 6: line(a, c)
            elif state == 7: line(a, d)
            elif state == 8: line(a, d)
            elif state == 9: line(a, c)
            elif state == 10: line(a, b); line(c, d)
            elif state == 11: line(a, b)
            elif state == 12: line(b, d)
            elif state == 13: line(b, c)
            elif state == 14: line(c, d)

    pygame.display.update()

pygame.quit()
