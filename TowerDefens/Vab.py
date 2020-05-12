import pygame, random, math, json, hf
from hf import *
from vector import *
from Array import *
pygame.init()

WIDTH, HEIGHT = 800, 600
cx, cy = WIDTH // 2, HEIGHT // 2

FIELDSIZE = 50
COLS, ROWS = WIDTH // FIELDSIZE, HEIGHT // FIELDSIZE

screen = pygame.display.set_mode((WIDTH + 50, HEIGHT + 50))
pygame.display.set_caption('TowerDefense')
