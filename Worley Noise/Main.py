from Vab import *
from Button import *
from Checkbox import *
from Point import *
pygame.init()
screen.fill((0, 0, 0))

modes = ["drag", "create", "delete"]
curMode = 0
points = []

visible = True

for i in range(25):
    x = random.randint(0, WIDTH)
    y = random.randint(0, FIELDHEIGHT)
    points.append(Point(x, y))

def generatePoints():
    for x in range(WIDTH):
        for y in range(FIELDHEIGHT):
            distances = []
            for i in range(len(points)):
                v = points[i].v
                d = math.hypot(x - v.x, y - v.y) # U need to use math.hypot here or it wont work
                distances.append(d)

            distances.sort()
            c = map(distances[0], 0, WIDTH, 0, 255)

            screen.set_at((x, y), (c, c, c))

    pygame.image.save(screen, "background.png")

generatePoints()

bg = pygame.image.load("background.png")
regenerateButton = Button(10, FIELDHEIGHT + 10, 50)
toggleVisibility = Button(10, FIELDHEIGHT + 70, 50)
switchMode = Button(10, FIELDHEIGHT + 130, 50)

toDel = []

run = True
while run:
    pygame.draw.rect(screen, (70, 70, 70), (FIELDHEIGHT, 0, WIDTH, HEIGHT))
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, (70, 70, 70), (FIELDHEIGHT, 0, WIDTH, HEIGHT))
    regenerateButton.draw()
    switchMode.draw()
    toggleVisibility.draw()

    screen.blit(
        pygame.font.SysFont("arial", 20).render("Regenerate", True, (255, 255, 255)),
        (70, FIELDHEIGHT + 10 + (50 // 5) * 2)
    )

    screen.blit(
        pygame.font.SysFont("arial", 20).render("Toggle Visibility", True, (255, 255, 255)),
        (70, FIELDHEIGHT + 70 + (50 // 5) * 2)
    )

    screen.blit(
        pygame.font.SysFont("arial", 20).render("ModeSwitch (title)", True, (255, 255, 255)),
        (70, FIELDHEIGHT + 130 + (50 // 5) * 2)
    )

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos = pygame.mouse.get_pos()
            if regenerateButton.is_clicked(m_pos):
                generatePoints()
                bg = pygame.image.load("background.png")

            if toggleVisibility.is_clicked(m_pos):
                visible = not visible

            if switchMode.is_clicked(m_pos):
                curMode += 1
                if curMode == len(modes):
                    curMode = 0

                pygame.display.set_caption(f"Worley Noise | Mode: {modes[curMode]} | Points: {len(points)}")

                for p in points:
                    p.state = modes[curMode]

                break

            for p in points:
                if p.isMouseInCircle(m_pos):
                    if curMode == 0:
                        if visible:
                            p.dragged = True

                    if curMode == 2:
                        if visible:
                            if len(points) > 1:
                                toDel.append(p)

            if curMode == 1:
                if visible:
                    x, y = m_pos

                    if y <= FIELDHEIGHT:
                        p = Point(m_pos[0], m_pos[1])
                        p.state = modes[curMode]
                        points.append(p)
                        pygame.display.set_caption(f"Worley Noise | Mode: {modes[curMode]} | Points: {len(points)}")
                        break

            for i, p in enumerate(toDel):
                points.remove(p)
                toDel.pop(i)

                pygame.display.set_caption(f"Worley Noise | Mode: {modes[curMode]} | Points: {len(points)}")

        if event.type == pygame.MOUSEBUTTONUP:
            for p in points:
                p.dragged = False

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            for p in points:
                p.isMouseInCircle(pos)


    for p in points:
        if visible:
            p.show()
            p.update()

    pygame.display.update()

pygame.quit()
