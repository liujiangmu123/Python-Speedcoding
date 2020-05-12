from Vab import *
from Mob import *
from Turret import *
pygame.init()

class StartButton:
    def __init__(self, x, y, img, size=50):
        self.x = x
        self.y = y
        self.img = img
        self.size = size

        self.curColor = (0, 0, 0)
        self.clickedColor = (255, 255, 255)
        self.normalColor = (0, 0, 0)

    def show(self):
        screen.blit(pygame.transform.scale(pygame.image.load(self.img), (self.size, self.size)), (self.x, self.y))
        pygame.draw.rect(screen, self.curColor, (self.x, self.y, self.size, self.size), 1)

    def mouseHover(self, clicked):
        x, y = pygame.mouse.get_pos()

        if self.x < x < self.x + self.size:
            if self.y < y < self.y + self.size:
                if clicked: self.curColor = self.clickedColor
                if not clicked: self.curColor = self.normalColor
                return True
        return False


class TurretBuyButton:
    def __init__(self, x, y, costs, image, turretType):
        self.x = x
        self.y = y
        self.costs = costs
        self.img = pygame.image.load(image)
        self.type = turretType

    def show(self):
        pygame.draw.rect(screen, (70, 70, 70), (self.x, self.y, 50, 50), 3)
        screen.blit(
            pygame.transform.scale(self.img, (40, 40)),
            (self.x + 5, self.y + 5)
        )

        screen.blit(
            pygame.font.SysFont("helvetica", 15).render(str(self.costs), True, (255, 255, 255)),
            (self.x + 27, self.y + 35)
        )

    def mouseHover(self):
        x, y = pygame.mouse.get_pos()
        return (self.x < x < self.x + 50) and (self.y < y < self.y + 50)

with open("map.json", "r") as fh:
    map = json.load(fh)

drawMap = False
debugMode = True
limitFPS = True
current = 3

clicked = False
turretClick = False
clicks = 0
clickedCol = -1
clickedRow = -1

mobCounter = 0
maxMobCounter = 150
currentWaveMobs = 0
maxWaveMobs = 15

avaibleWaveButton = False

wave = 0

money = 300
lives = 20

turretButtons = [
    TurretBuyButton(0, HEIGHT, 100, "img/normalTower.png", "normal"),
    TurretBuyButton(50, HEIGHT, 150, "img/lv2Tower.png", "lv2")
]

for entry in map:
    if entry[2] == "start":
        startCol, startRow = entry[0], entry[1]
        break


mobs = [] # Mob(startCol, startRow, map)]
turrets = []
boughtTurrets = {}
showedTurrets = []

def draw_grid():
    for col in range(COLS):
        for row in range(ROWS):
            pygame.draw.rect(screen, (0, 0, 0), (col * FIELDSIZE, row * FIELDSIZE, FIELDSIZE, FIELDSIZE), 1)
def draw_map_tiles():
    for entry in map:
        if entry[2] == "normal":
            pygame.draw.rect(screen, (0, 0, 255), (entry[0] * FIELDSIZE, entry[1] * FIELDSIZE, FIELDSIZE, FIELDSIZE))
        if entry[2] == "start":
            screen.blit(pygame.image.load("img/startfield.png"), (entry[0] * FIELDSIZE, entry[1] * FIELDSIZE))
        if entry[2] == "end":
            screen.blit(pygame.image.load("img/trashfield.png"), (entry[0] * FIELDSIZE, entry[1] * FIELDSIZE))
def save_map():
    with open("map.json", "w") as fh:
        json.dump(map, fh, indent=4)
        drawMap = False

startWaveBtn = StartButton(WIDTH, HEIGHT, "img/play.png")

run = True
while run:
    if limitFPS: pygame.time.Clock().tick(120)
    screen.fill((100, 100, 100))
    draw_map_tiles()
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if debugMode: mobs.append(Mob(startCol, startRow, map))
        if event.type == pygame.KEYDOWN:
            if drawMap:
                if event.key == pygame.K_1: current = 1
                if event.key == pygame.K_2: current = 2
                if event.key == pygame.K_3: current = 3
                if event.key == pygame.K_s: save_map()
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()

            if x >= WIDTH or y >= HEIGHT:
                if not clicked:
                    startWaveBtn.mouseHover(False)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if drawMap:
                x, y = pygame.mouse.get_pos()
                col, row = x // FIELDSIZE, y // FIELDSIZE

                if pygame.mouse.get_pressed()[0]:
                    if current == 1:
                        if not [col, row, "start"] in map: map.append([col, row, "start"])
                    if current == 2:
                        if not [col, row, "end"] in map: map.append([col, row, "end"])
                    if current == 3: map.append([col, row, "normal"])
                if pygame.mouse.get_pressed()[2]:
                    if current == 3:
                        if [col, row, "normal"] in map:
                            map.remove([col, row, "normal"])
                    if current == 2:
                        if [col, row, "end"] in map:
                            map.remove([col, row, "end"])
                    if current == 1:
                        if [col, row, "start"] in map:
                            map.remove([col, row, "start"])
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                col, row = x // FIELDSIZE, y // FIELDSIZE

                if x >= WIDTH or y >= HEIGHT:
                    if not clicked and avaibleWaveButton and len(mobs) == 0:
                        if startWaveBtn.mouseHover(True):
                            wave += 1

                            mobCounter = 0
                            maxMobCounter = 150
                            currentWaveMobs = 0
                            maxWaveMobs = 15

                            avaibleWaveButton = False
                            clicked = False
                            turretClick = False
                            clickedRow = -1
                            clickedCol = -1

                            if wave > 2:
                                maxWaveMobs = wave * (5 + wave)

                    for button in turretButtons:
                        if button.mouseHover():
                            price = button.costs
                            if money >= price:
                                money -= price
                                if not button.type in boughtTurrets:
                                    boughtTurrets[button.type] = 1
                                else:
                                    boughtTurrets[button.type] += 1

                    if len(showedTurrets) - 1 >= row:
                        turretType = showedTurrets[row]
                        turrets.append(Turret(clickedCol, clickedRow, turretType=showedTurrets[row]))

                        showedTurrets.pop(row)
                        boughtTurrets[turretType] -= 1
                        if boughtTurrets[turretType] <= 0:
                            del boughtTurrets[turretType]

                    for turret in turrets:
                        if turretClick:
                            if turret.col == clickedCol and turret.row == clickedRow:
                                # pygame.draw.rect(screen, (70, 70, 70), (WIDTH, 47, 50, 50), 1)

                                if turret.level < 2:
                                    if WIDTH < x < WIDTH + 50 and 47 < y < 97:
                                        costs = turret.getAttackUpgradeCosts()
                                        if money >= costs:
                                            money -= costs
                                            turret.levelAttackUp()

                else:
                    if not clicked:
                        for turret in turrets:
                            if turret.col == col and turret.row == row:
                                # Upgrade
                                turretClick = True
                                clicks = 1
                                print("UPGRADE")
                            else:
                                print("PLACE")

                    isPath = False
                    for c, r, type_ in map:
                        if col == c and row == r:
                            isPath = True

                    if isPath: break

                    clicked = not clicked
                    clickedCol = col
                    clickedRow = row

                    if clicks == 0:
                        turretClick = False

                        for turret in turrets:
                            turret.showDistance = False

                    clicks = 0

    if wave == 0:
        avaibleWaveButton = True

    for turret in turrets:
        turret.show()
        turret.update(mobs)

    for mob in mobs:
        mob.show()
        mob.update()

        if mob.checkLastSpot():
            mobLives = mob.live
            mobs.remove(mob)
            lives -= math.ceil(mobLives / 2)

        if mob.isDeath():
            money += mob.worth
            mobs.remove(mob)

            for turret in turrets:
                turret.currentMob = -1
                turret.bullets = []

    if drawMap:
        screen.blit(pygame.font.SysFont("helvetica", 20).render(
            "1: Start Point, 2: End Point, 3 Follow Point, Right Mouse: Remove, Left Mouse: Place, S: Save, Current: " + str(
                current), True, (255, 255, 255)), (0, 0))

    pygame.draw.rect(screen, (0, 0, 0), (0, HEIGHT, WIDTH + 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (WIDTH, 0, 50, HEIGHT + 50))

    if clicked and not turretClick:
        pygame.draw.rect(screen, (255, 0, 0), (clickedCol * FIELDSIZE, clickedRow * FIELDSIZE, FIELDSIZE, FIELDSIZE), 2)
        showedTurrets = []

        for n, turretType in enumerate(boughtTurrets):
            if not turretType in showedTurrets:
                showedTurrets.append(turretType)
                image = pygame.transform.scale(pygame.image.load("img/" + turretType + "Tower.png"), (40, 40))

                pygame.draw.rect(screen, (70, 70, 70), (WIDTH, n * FIELDSIZE, FIELDSIZE, FIELDSIZE), 3)
                screen.blit(image, (WIDTH + 5, n * FIELDSIZE + 5))
                screen.blit(
                    pygame.font.SysFont("helvetica", 15).render(str(boughtTurrets[turretType]), True, (255, 255, 255)),
                    (WIDTH, n * FIELDSIZE)
                )


    for button in turretButtons:
        button.show()

    if not clicked and avaibleWaveButton and len(mobs) == 0:
        startWaveBtn.show()

    screen.blit(
        pygame.font.SysFont("comicsansms", 20).render(str(money), True, (255, 255, 255)),
        (10, 10)
    )

    screen.blit(
        pygame.transform.scale(pygame.image.load("img/coin.png"), (30, 30)),
        (10 + (len(str(money)) * 13), 10)
    )

    screen.blit(
        pygame.font.SysFont("comicsansms", 20).render(str(lives), True, (255, 255, 255)),
        (60 + (len(str(money)) * 13), 10)
    )

    screen.blit(
        pygame.transform.scale(pygame.image.load("img/heart.png"), (30, 30)),
        (60 + (len(str(money)) * 13) + (len(str(lives)) * 13), 10)
    )

    screen.blit(
        pygame.font.SysFont("helvetica", 30).render(f"Wave {wave}", True, (255, 255, 255)),
        (WIDTH // 2 - 40, 10)
    )

    if wave > 0:
        if not currentWaveMobs == maxWaveMobs:
            mobCounter += 1

            if mobCounter == maxMobCounter:
                mobCounter = 0
                mobs.append(Mob(startCol, startRow, map))

                currentWaveMobs += 1
        elif len(mobs) == 0:
            avaibleWaveButton = True

    for turret in turrets:
        if turretClick:
            if turret.col == clickedCol and turret.row == clickedRow:
                turret.showDistance = True
                pygame.draw.rect(screen, (255, 0, 0), (turret.col * FIELDSIZE, turret.row * FIELDSIZE, FIELDSIZE, FIELDSIZE), 2)

                screen.blit(pygame.font.SysFont("courier", 20).render("LV" + str(turret.level + 1), True, (255, 255, 255)), (WIDTH + 8, 8))

                if turret.level < 2:
                    costs = turret.getAttackUpgradeCosts()
                    pygame.draw.rect(screen, (70, 70, 70), (WIDTH, 47, 50, 50), 1)
                    screen.blit(pygame.font.SysFont("courier", 30).render("+1", True, (255, 255, 255)), (WIDTH + 4, 52))
                    screen.blit(pygame.font.SysFont("new york", 20).render(str(costs), True, (255, 255, 255)), (WIDTH, 47))


    pygame.display.update()

pygame.quit()
