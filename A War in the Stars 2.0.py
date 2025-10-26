import pygame
pygame.init

WIDTH = 800
HEIGHT = 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))

Z = pygame.image.load("Z.png")
X = pygame.image.load("X.png")
Y = pygame.image.load("images.png")
Y = pygame.transform.scale(Y, (800,600))
pygame.font.init()
health_font = pygame.font.SysFont("Comic Sans MS", 36)

def draw_screen():
    Screen.blit(Y, (0,0))
    Screen.blit(X, (100,500))
    Screen.blit(Z, (650,500))
    rectangle = pygame.Rect(390, 0, 20, 600)
    pygame.draw.rect(Screen, "black", rectangle)
    A_health = health_font.render("Health: 10", 1, "black")
    Screen.blit(A_health, (60,60))
    B_health = health_font.render("Health: 10", 1, "black")
    Screen.blit(B_health, (550,60))

R = pygame.Rect(100, 500, 39, 39)
B = pygame.Rect(650, 500, 39, 39)
RH = 10
BH =10
def R_Move(key_pressed, Rect):
    if key_pressed[pygame.K_w] and Rect.y > 0:
        Rect.y -= 10
    elif key_pressed[pygame.K_s] and Rect.y < 600:
        Rect.y += 10
    elif key_pressed[pygame.K_a] and Rect.x > 0:
        Rect.x -= 10
    elif key_pressed[pygame.K_d] and Rect.x < 400:
        Rect.x += 10

while True:
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            pygame.quit()
    K = pygame.key.get_pressed()
    R_Move(K, R)
    draw_screen()
    pygame.display.update()