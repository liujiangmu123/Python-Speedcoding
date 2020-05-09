import pygame, random, math, hf
from hf import *
from vector import *
pygame.init()

WIDTH, HEIGHT = 400, 600
FIELDHEIGHT = 400
cx, cy = WIDTH // 2, HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Worley Noise | Mode: drag | Points: 25')
