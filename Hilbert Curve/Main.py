from Vab import *
pygame.init()

def hilbert_curve():
    order = 7
    N = int(pow(2, order))
    total = N * N

    path = []

    def hilbert(i):
        points = [
            createVector(0, 0),
            createVector(0, 1),
            createVector(1, 1),
            createVector(1, 0)
        ]

        index = i & 3
        v = points[index]

        for j in range(1, order):
            i = i >> 2
            index = i & 3

            length = pow(2, j)

            if index == 0:
                temp = v.x
                v.x = v.y
                v.y = temp
            elif index == 1:
                v.y += length
            elif index == 2:
                v.x += length
                v.y += length
            elif index == 3:
                temp = length - 1 - v.x
                v.x = length - 1 - v.y
                v.y = temp

                v.x += length

        return v


    for i in range(total):
        path.append(hilbert(i))
        length = WIDTH / N
        path[i].mult(length)
        path[i].add(createVector(length // 2, length // 2))

        path[i].to_integer()

    FPS = order * 6
    counter = 0
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False

        for i in range(counter):
            screen.set_at((path[i].x, path[i].y), (255, 255, 255))

            r = map(i, 0, len(path), 0, 255)
            g = map(i, 0, len(path), 255, 0)
            b = map(i, 0, len(path), 100, 255)

            if not i == len(path) - 1:
                pygame.draw.line(screen, (r, g, b), (path[i].x, path[i].y), (path[i + 1].x, path[i + 1].y))


        counter += 10
        if counter >= len(path):
            counter = 0


        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    hilbert_curve()