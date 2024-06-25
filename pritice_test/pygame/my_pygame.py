import pygame
import sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("植物大战僵尸")

image = pygame.image.load('./images/peashooter.png').convert_alpha()
image = pygame.transform.scale(image, (50, 50))
print(image.get_rect(), image.get_rect().move(20, 10))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     keys = pygame.key.get_pressed()
#     print(keys)
#     if keys[pygame.KEYUP]:
#         image.get_rect().top -= 2
#     if keys[pygame.KEYDOWN]:
#         image.get_rect().top += 2
#     print(keys)
#     screen.fill((255, 255, 255))
#
#     # for _ in range(10):
#     image_move = image.get_rect().move(100, 0)
#     # print(image_move)
#     screen.blit(image, image_move)
#
#     pygame.display.flip()


