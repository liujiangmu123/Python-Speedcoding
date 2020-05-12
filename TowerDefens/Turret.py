from Vab import *
pygame.init()

images = {
    "normal": ["normalTower.png", "normal2Tower.png", "normal3Tower.png"],
    "lv2": ["lv2Tower.png", "lv22Tower.png", "lv23Tower.png"]
}

negDists = {
    "normal": 80,
    "lv2": 70
}

shootCounts = {
    "normal": [20, 17, 15],
    "lv2": [40, 36, 33]
}

damagePerBullets = {
    "normal": [1, 1.5, 2],
    "lv2": [2, 2.5, 3]
}

distances = {
    "normal": [170, 200, 225],
    "lv2": [170, 210, 230]
}

attackUpgradeCosts = {
    "normal": [100, 190],
    "lv2": [120, 210]
}

class Turret:
    def __init__(self, col, row, turretType="normal"):
        self.col = col
        self.row = row

        self.pos = createVector(col, row)
        self.pos.mult(FIELDSIZE)

        self.type = turretType
        self.level = 0

        self.shootCount = 0
        self.maxShootCount = shootCounts[self.type][self.level]

        self.distance = distances[self.type][self.level]
        self.showDistance = False

        self.bullets = []
        self.dpb = damagePerBullets[self.type][self.level] # Damage per Bullets

        self.currentMob = -1

    def levelAttackUp(self):
        self.level += 1

        self.maxShootCount = shootCounts[self.type][self.level]
        self.distance = distances[self.type][self.level]
        self.dpb = damagePerBullets[self.type][self.level]

    def getAttackUpgradeCosts(self):
        return attackUpgradeCosts[self.type][self.level]

    def show(self):
        screen.blit(
            pygame.image.load("img/" + images[self.type][self.level]),
            (self.pos.x, self.pos.y)
        )

        if self.showDistance:
            pygame.draw.circle(screen, (255, 0, 0), (self.pos.x + FIELDSIZE // 2, self.pos.y + FIELDSIZE // 2), self.distance // 2, 1)

        for bullet in self.bullets:
            pygame.draw.ellipse(screen, (255, 0, 255), (bullet.x, bullet.y, 10, 10), 0)

    def update(self, mobs):
        print(self.currentMob)
        for mob in mobs:
            distance = math.hypot(mob.pos.x - self.pos.x, mob.pos.y - self.pos.y)

            if distance <= self.distance - negDists[self.type]:
                self.currentMob = mobs.index(mob)

            if self.currentMob > -1:
                try:
                    _dist = math.hypot(mobs[self.currentMob].pos.x - self.pos.x, mobs[self.currentMob].pos.y - self.pos.y)

                    if _dist >= self.distance - negDists[self.type]:
                        self.bullets = []
                        self.currentMob = -1
                except IndexError:
                    pass

        if self.currentMob > -1:
            self.shootCount += 1

            if self.shootCount == self.maxShootCount:
                self.shootCount = 0

                self.bullets.append(
                    createVector(self.pos.x + FIELDSIZE // 2, self.pos.y + FIELDSIZE // 2)
                )

            for bullet in self.bullets:
                if not mobs[self.currentMob].pos.x + FIELDSIZE // 4 == bullet.x:
                    if mobs[self.currentMob].pos.x + FIELDSIZE // 4 > bullet.x:
                        bullet.add(createVector(5, 0))
                    else:
                        bullet.add(createVector(-5, 0))

                if not mobs[self.currentMob].pos.y + FIELDSIZE // 2 == bullet.y:
                    if mobs[self.currentMob].pos.y + FIELDSIZE // 2 > bullet.y:
                        bullet.add(createVector(0, 5))
                    else:
                        bullet.add(createVector(0, -5))

                if math.hypot(mobs[self.currentMob].pos.x + FIELDSIZE // 4 - bullet.x, mobs[self.currentMob].pos.y + FIELDSIZE // 2 - bullet.y) <= 20:
                    self.bullets.remove(bullet)
                    mobs[self.currentMob].takeDamage(self.dpb)








