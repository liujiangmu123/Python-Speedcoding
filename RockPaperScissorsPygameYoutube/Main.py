import pygame, random, vector, math
pygame.init()

'''
Pygame Speedcoding Rock paper Scissors Visualization
Author: Ari24
Youtube: https://youtu.be/fQrgQzJPPYw
'''

def rps(user_input):
    '''
    Code aus meinem Speedcoding https://youtu.be/7KtWioCF2qI
    '''
    rps = ["stein", "schere", "papier"]
    current = random.choice(rps)

    if user_input in rps:
        if user_input == current:
            return [0, "Unentschieden!"]

        # Stein
        elif user_input == "stein" and current == "schere":
            return [1, "Ich habe Schere! Du hast gewonnen!"]

        elif user_input == "stein" and current == "papier":
            return [0, "Ich habe Papier! Ich habe gewonnen!"]

        # Schere
        elif user_input == "schere" and current == "stein":
            return [0, "Ich habe Stein! Ich habe gewonnen!"]

        elif user_input == "schere" and current == "papier":
            return [1, "Ich habe Papier! Du hast gewonnen!"]

        # Papier
        elif user_input == "papier" and current == "stein":
            return [1, "Ich habe Stein! Du hast gewonnen!"]

        elif user_input == "papier" and current == "schere":
            return [0, "Ich habe Schere! Ich habe gewonnen!"]

# Define the reset button
class Button:
    def __init__(self, x, y, width, height, text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (255, 255, 255)

    def show(self):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        screen.blit(
            pygame.font.SysFont("comicsansms", 32).render(
                self.text, True, (0, 0, 0)
            ),
            (self.rect.x + self.rect.width + 5, self.rect.y + self.rect.height // 4)
        )

    def check_mouse_button_down(self):
        x, y = pygame.mouse.get_pos()

        if x > self.rect.x and x < self.rect.x + self.rect.width:
            if y > self.rect.y and y < self.rect.y + self.rect.height:
                self.color = (0, 255, 0)
                return True

        return False

    def check_mouse_button_up(self):
        x, y = pygame.mouse.get_pos()

        if x > self.rect.x and x < self.rect.x + self.rect.width:
            if y > self.rect.y and y < self.rect.y + self.rect.height:
                self.color = (255, 255, 255)



WIDTH, HEIGHT = 400, 400
cx, cy = WIDTH // 2, HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RockPaperScissorsPygameYoutube')

paper_image = pygame.transform.scale(pygame.image.load("papier.png"), (60, 60))
paper_rect = pygame.Rect(105, 100, 60, 60)

scissor_image = pygame.transform.scale(pygame.image.load("schere.png"), (60, 60))
scissor_rect = pygame.Rect(105 + 70, 100, 60, 60)

rock_image = pygame.transform.scale(pygame.image.load("stein.png"), (60, 60))
rock_rect = pygame.Rect(105 + 70 * 2, 100, 60, 60)

def reset():
    global ergebnis, end_text, played_round
    ergebnis = None
    end_text = ""
    played_round = False

ergebnis = None
points = 0
end_text = ""

reset_button = Button(0, 250, 50, 50, text="Reset Game")

played_round = False

run = True
while run:
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.MOUSEBUTTONUP:
            reset_button.check_mouse_button_up()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.check_mouse_button_down():
                reset()

            if not played_round:
                # Get x and y position
                x, y = pygame.mouse.get_pos()

                # Check rock
                if x > rock_rect.x and x < rock_rect.x + rock_rect.width:
                    if y > rock_rect.y and y < rock_rect.y + rock_rect.height:
                        ergebnis = rps("stein")
                        points += ergebnis[0]
                        end_text = ergebnis[1]
                        played_round = True

                # Check paper
                if x > paper_rect.x and x < paper_rect.x + paper_rect.width:
                    if y > paper_rect.y and y < paper_rect.y + paper_rect.height:
                        ergebnis = rps("papier")
                        points += ergebnis[0]
                        end_text = ergebnis[1]
                        played_round = True

                # Check scissors
                if x > scissor_rect.x and x < scissor_rect.x + scissor_rect.width:
                    if y > scissor_rect.y and y < scissor_rect.y + scissor_rect.height:
                        ergebnis = rps("schere")
                        points += ergebnis[0]
                        end_text = ergebnis[1]
                        played_round = True


    screen.blit(
        pygame.font.SysFont("comicsansms", 32).render(
            "Wähle Weise", True, (0, 0, 0)
        ),
        (105, 40)
    )
    screen.blit(paper_image, (paper_rect.x, paper_rect.y))
    screen.blit(scissor_image, (scissor_rect.x, scissor_rect.y))
    screen.blit(rock_image, (rock_rect.x, rock_rect.y))

    screen.blit(
        pygame.font.SysFont("comicsansms", 20).render(
            f"Out: {end_text}", True, (0, 0, 0)
        ),
        (0, 170)
    )

    screen.blit(
        pygame.font.SysFont("comicsansms", 30).render(
            f"Punkte: {points}", True, (0, 0, 0)
        ),
        (0, 190)
    )

    reset_button.show()


    pygame.display.update()

pygame.quit()
