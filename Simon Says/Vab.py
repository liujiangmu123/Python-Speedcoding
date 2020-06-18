import pygame, random
from hf import *
from vector import *
pygame.init()

WIDTH, HEIGHT = 400, 600
cx, cy = WIDTH // 2, HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simon Says')
