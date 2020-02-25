'''
Evaluating Pi with Collisions

Github:
YouTube:
Numberphile's Video: https://www.youtube.com/watch?v=abv4Fz7oNr0
TheCodingTrain's Video: https://www.youtube.com/watch?v=PoW8g67XNxA&t=0s
3Blue1Brown Videos:
- https://www.youtube.com/watch?v=HEfHFsfGXjs
- https://www.youtube.com/watch?v=jsYwFizhncE&t=0s

Creator: Ari24
'''
from EvaluatingPiWithCollisions.Vab import * # or from Vab import *
from EvaluatingPiWithCollisions.Block import * # or from Block import *
pygame.init()


count = 0
digits = 7
timeSteps = 100000

block1 = Block(100, 20, 1, 0)
m2 = pow(100, digits-1)
block2 = Block(300, 100, m2, -5 / timeSteps)

run = True
while run:
    pygame.time.Clock().tick(60)
    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, (255, 255, 255), (0, theHeight, WIDTH, HEIGHT - theHeight))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    for i in range(timeSteps):
        if block1.collide(block2):
            v1 = block1.bounce(block2)
            v2 = block2.bounce(block1)

            block1.v = v1
            block2.v = v2

            count += 1

        if block1.hitWall():
            block1.reverse()

            count += 1

        block1.update()
        block2.update()

    block1.show()
    block2.show()

    screen.blit(pygame.font.SysFont("comicsansms", 32).render(
        str(count)[0] + "." + str(count)[1::], True, (0, 0, 0)), (10, 210))


    pygame.display.update()

pygame.quit()
