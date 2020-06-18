from Vab import *
pygame.init()


class Button:
    def __init__(self, color: tuple, clicked_color: tuple, bot_clicked_color: tuple, x: int, y: int, width: int, height: int, color_type: str):
        self.pos = createVector(x, y)
        self.color = color
        self.width = width
        self.height = height
        self.clicked = False
        self.bot_clicked = False
        self.clicked_color = clicked_color
        self.bot_clicked_color = bot_clicked_color
        self.can_be_clicked = True
        self.color_type = color_type

    def show(self):
        pygame.draw.rect(screen, (self.color if not self.clicked else self.clicked_color if self.can_be_clicked else self.color) if not self.bot_clicked else self.bot_clicked_color, (self.pos.x, self.pos.y, self.width, self.height))

    def is_mouse_init(self, pos):
        x, y = pos
        return (
            self.pos.x < x < self.pos.x + self.width and
            self.pos.y < y < self.pos.y + self.height
        )

def draw_layout():
    pygame.draw.line(screen, (100, 100, 100), (cx - 5, 0), (cx - 5, cy - 5), 3)
    pygame.draw.line(screen, (100, 100, 100), (cx + 5, 0), (cx + 5, cy - 5), 3)
    pygame.draw.line(screen, (100, 100, 100), (WIDTH, cy - 5), (cx + 5, cy - 5), 3)
    pygame.draw.line(screen, (100, 100, 100), (WIDTH, cy + 5), (cx + 5, cy + 5), 3)
    pygame.draw.line(screen, (100, 100, 100), (cx - 5, HEIGHT), (cx - 5, cy + 5), 3)
    pygame.draw.line(screen, (100, 100, 100), (cx + 5, HEIGHT), (cx + 5, cy + 5), 3)
    pygame.draw.line(screen, (100, 100, 100), (0, cy + 5), (cx - 5, cy + 5), 3)
    pygame.draw.line(screen, (100, 100, 100), (0, cy-5), (cx - 5, cy - 5), 3)

    pygame.draw.circle(screen, (255, 255, 255), (cx, cy), 99, 0)
    pygame.draw.circle(screen, (0, 0, 0), (cx, cy), 100, 3)


buttons = [
    Button((255, 0, 0), (225, 0, 0), (170, 0, 0), 0, 0, cx-6, cy-6, "r"),
    Button((0, 0, 255), (0, 0, 225), (0, 0, 170), cx + 6, 0, WIDTH, cy - 6, "b"),
    Button((0, 255, 0), (0, 225, 0), (0, 170, 0), 0, cy + 5, cx - 5, HEIGHT, "g"),
    Button((255, 255, 0), (225, 225, 0), (170, 170, 0), cx + 5, cy + 5, WIDTH, HEIGHT, "y")
]

colors = ["r", "g", "b", "y"]
moves = []
points = 0

def getButtonWithColor(c):
    for btn in buttons:
        if btn.color_type == c:
            return btn

    return None


add_move_delay = 0
current_moves_index = 0
current_show_index = 0
button_to_press = None
userCanMove = False
getNewMove = True
show_new_moves = True
addNewMove = True
run = True
while run:
    pygame.time.Clock().tick(30)
    screen.fill((20, 20, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

            for button in buttons:
                if button.is_mouse_init(position):
                    button.clicked = True

                    if not getNewMove and userCanMove:
                        if button.color_type == moves[current_moves_index]:
                            print(f"User: {button.color_type}")
                            current_moves_index += 1
                        else:
                            raise Exception("Game Over!")

                        if current_moves_index > len(moves) - 1:
                            getNewMove = True
                            addNewMove = True
                            userCanMove = False
                            points += 1

        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()

            for button in buttons:
                if button.is_mouse_init(position):
                    button.clicked = False

    pygame.draw.rect(screen, (130, 0, 0), (0, 0, cx - 5, cy - 5), 0)
    pygame.draw.rect(screen, (0, 130, 0), (0, cy + 5, cx - 5, HEIGHT), 0)
    pygame.draw.rect(screen, (0, 0, 130), (cx + 5, 0, WIDTH, cy - 5), 0)
    pygame.draw.rect(screen, (130, 130, 0), (cx + 5, cy + 5, WIDTH, HEIGHT), 0)

    for button in buttons:
        button.show()

    draw_layout()

    screen.blit(
        pygame.font.SysFont("arial", 70, bold=True, italic=False).render(
            str(nf(points, 3)), True, (0, 0, 0)
        ), (cx - 57, cy - 65)
    )

    pygame.display.update()

    if show_new_moves:
        add_move_delay += 1

    if add_move_delay >= 30:
        add_move_delay = 0

        if button_to_press is not None:
            if button_to_press.bot_clicked:
                button_to_press.bot_clicked = False

        if not current_show_index > len(moves) - 1:
            color = moves[current_show_index]
            button_to_press = getButtonWithColor(color)
            button_to_press.bot_clicked = True

        if not current_show_index > len(moves) - 1:
            current_show_index += 1

        if current_show_index > len(moves) - 1 and not button_to_press.bot_clicked:
            getNewMove = False
            show_new_moves = False
            current_show_index = 0
            current_moves_index = 0
            userCanMove = True

    if getNewMove and addNewMove:
        current_moves_index = 0
        moves.append(random.choice(colors))

        addNewMove = False
        show_new_moves = True
        print(moves)

pygame.quit()
