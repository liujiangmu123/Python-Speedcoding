from Vab import *
from Mob import *
pygame.init()

with open("map.json", "r") as fh:
    map = json.load(fh)


drawMap = False
current = 3

for entry in map:
    if entry[2] == "start":
        startCol, startRow = entry[0], entry[1]
        break


print(map)

mob = Mob(startCol, startRow, map)

def draw_grid():
    for col in range(COLS):
        for row in range(ROWS):
            pygame.draw.rect(screen, (0, 0, 0), (col * FIELDSIZE, row * FIELDSIZE, FIELDSIZE, FIELDSIZE), 1)
def draw_map_tiles():
    for entry in map:
        if entry[2] == "normal":
            pygame.draw.rect(screen, (0, 0, 255), (entry[0] * FIELDSIZE, entry[1] * FIELDSIZE, FIELDSIZE, FIELDSIZE))
        if entry[2] == "start":
            pygame.draw.rect(screen, (0, 255, 0), (entry[0] * FIELDSIZE, entry[1] * FIELDSIZE, FIELDSIZE, FIELDSIZE))
        if entry[2] == "end":
            pygame.draw.rect(screen, (255, 0, 0), (entry[0] * FIELDSIZE, entry[1] * FIELDSIZE, FIELDSIZE, FIELDSIZE))
def save_map():
    with open("map.json", "w") as fh:
        json.dump(map, fh, indent=4)
        drawMap = False

run = True
while run:
    pygame.time.Clock().tick(60)
    screen.fill((100, 100, 100))
    draw_map_tiles()
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN:
            if drawMap:
                if event.key == pygame.K_1: current = 1
                if event.key == pygame.K_2: current = 2
                if event.key == pygame.K_3: current = 3
                if event.key == pygame.K_s: save_map()
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

    mob.show()
    mob.update()


    if drawMap:
        screen.blit(pygame.font.SysFont("helvetica", 20).render(
            "1: Start Point, 2: End Point, 3 Follow Point, Right Mouse: Remove, Left Mouse: Place, S: Save, Current: " + str(
                current), True, (255, 255, 255)), (0, 0))
    pygame.display.update()

pygame.quit()
