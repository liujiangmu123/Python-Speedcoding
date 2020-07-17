import pygame, random, math
from vector import *
pygame.init()

WIDTH, HEIGHT = 600, 400
cx, cy = WIDTH // 2, HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MarchingSquares')
