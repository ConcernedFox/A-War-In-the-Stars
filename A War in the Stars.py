import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
Screen = pygame.display.set_mode((WIDTH,HEIGHT))

E = pygame.image.load("A.png")
C = pygame.transform.rotate(E, -90)
F = pygame.image.load("B.png")
D = pygame.transform.rotate(F, 90)
S = pygame.image.load("s.jpg")
S = pygame.transform.scale(S, (WIDTH, HEIGHT))
pygame.font.init()
health_font = pygame.font.SysFont("Comic Sans MS", 36)

def draw_screen():
    Screen.blit(S, (0,0))
    Screen.blit(C, (100,500))
    Screen.blit(D, (650,500))
    rectangle = pygame.Rect(390, 0, 20, 600)
    pygame.draw.rect(Screen, "black", rectangle)
    A_health = health_font.render("Health: 10", 1, "black")
    Screen.blit(A_health, (60,60))
    B_health = health_font.render("Health: 10", 1, "black")
    Screen.blit(B_health, (550,60))

R = pygame.Rect(100, 500, 39, 39)
B = pygame.Rect(650, 500, 39, 39)
RH = 10
BH = 10
def R_move(key_pressed, Rect):
    if key_pressed[pygame.K_a] and Rect.x > 0:
        Rect.x -= 10
    elif key_pressed[pygame.K_d] and Rect.x < 400:
        Rect.x += 10
    elif key_pressed[pygame.K_w] and Rect.y > 0:
        Rect.y -= 10
    elif key_pressed[pygame.K_s] and Rect.y < 600:
        Rect.y += 10

while True:
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            pygame.quit()
    K = pygame.key.get_pressed()
    R_move(K, R)
    draw_screen()
    pygame.display.update()