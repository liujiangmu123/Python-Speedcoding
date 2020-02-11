import pygame, random, vector, math
from hf import *
from vector import *
pygame.init()

WIDTH, HEIGHT = 800, 600
cx, cy = WIDTH // 2, HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Line Intersection')
