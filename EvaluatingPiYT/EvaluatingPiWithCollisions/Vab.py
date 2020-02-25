import pygame, random, vector, math
from hf import *
pygame.init()

WIDTH, HEIGHT = 800, 600
cx, cy = WIDTH // 2, HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('EvaluatingPiWithCollisions')

blockImg = pygame.image.load("block.png")

theHeight = 200