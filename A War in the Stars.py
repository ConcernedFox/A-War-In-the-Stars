import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
Screen = pygame.display.set_mode((WIDTH,HEIGHT))

A = pygame.image.load("A.png")
A = pygame.transform.rotate(A, -90)
B = pygame.image.load("B.png")
B = pygame.transform.rotate(B, 90)

def draw_screen():
    Screen.blit(A, (100,500))
    Screen.blit(B, (650,500))

while True:
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            pygame.quit()
    draw_screen()
    pygame.display.update()