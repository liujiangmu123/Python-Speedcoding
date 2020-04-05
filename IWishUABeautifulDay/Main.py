import pygame
import requests
import io
import os
import random
pygame.init()
pygame.font.init()


screen = pygame.display.set_mode((300, 500))
pygame.display.set_caption("I wish u a great day!")

font = pygame.font.Font(os.path.join("beautiful_font.ttf"), 30)
texts = [ # Pipe for newline
    "Life is a journey | not a destination",
    "Life is like riding a bicycle | To keep your balance | you must keep moving",
    "Where there is love there is life |",
    "A life spent making mistakes | is not only more honorable | but more useful than a life spent | doing nothing",
    "Life can only be | understood backwards; | but it must be lived forwards",
    "If I can stop one | heart from breaking | I shall not live in vain",
    "In the end | it's not the years in your life | that count | It's the life in your years",
    "Believe that life is worth | living and your belief will help | create the fact"
]

width, height = 300, 500

def get_img():
    global width, height
    URL = "https://source.unsplash.com/random"
    req = requests.get(URL)
    img = io.BytesIO(req.content)
    pg_img = pygame.image.load(img)

    width, height = pg_img.get_rect().size

    width = width // 3
    height = height // 3

    pygame.display.set_mode((width, height))


    return pygame.transform.scale(pg_img, (width, height))

def get_text():
    return random.choice(texts).replace("|", "\n")

def render_multi_line(text, x, y, fsize, color):
    lines = text.splitlines()
    for i, l in enumerate(lines):
        screen.blit(font.render(l, 0, color), (x, y + fsize * i))


text = get_text()
img = get_img()

main_screen = True
run = True
while run:
    screen.fill((0, 0, 0))
    if not main_screen:
        screen.blit(img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if main_screen:
                main_screen = False

            img = get_img()
            text = get_text()

            print("The image says: " + text, "\n")



    if main_screen:
        screen.blit(
            pygame.font.SysFont("Calibri", 32).render(
                "Press me", True, (255, 255, 255)
            ), (90, 130)
        )
    else:
        render_multi_line(text, 0, 0, 30, (255, 255, 255))
    
    pygame.display.update()

pygame.quit()