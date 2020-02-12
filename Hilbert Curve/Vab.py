import pygame
from vector import *
from hf import *

pygame.init()

WIDTH, HEIGHT = 512, 512
cx, cy = WIDTH // 2, HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hilbert Curve')
