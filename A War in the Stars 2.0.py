import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))

Z = pygame.image.load("Z.png")
X = pygame.image.load("X.png")
Y = pygame.image.load("images.png")
Y = pygame.transform.scale(Y, (800,600))
pygame.font.init()
health_font = pygame.font.SysFont("Comic Sans MS", 36)

def draw_screen(R, L, A, B):
    Screen.blit(Y, (0,0))
    Screen.blit(Z, (L.x,L.y))
    Screen.blit(X, (R.x,R.y))
    for Re in A:
        pygame.draw.rect(Screen, "black", Re)
    for Le in B:
        pygame.draw.rect(Screen, "black", Le)
    rectangle = pygame.Rect(390, 0, 20, 600)
    pygame.draw.rect(Screen, "black", rectangle)
    A_health = health_font.render("Health: 10", 1, "black")
    Screen.blit(A_health, (60,60))
    B_health = health_font.render("Health: 10", 1, "black")
    Screen.blit(B_health, (550,60))

R = pygame.Rect(100, 500, 39, 39)
B = pygame.Rect(650, 500, 39, 39)
Rshoot = pygame.USEREVENT + 1
Bshoot = pygame.USEREVENT + 2
RH = 10
BH = 10

def R_Move(key_pressed, Rect):
    if key_pressed[pygame.K_w] and Rect.y > 0:
        Rect.y -= 10
    elif key_pressed[pygame.K_s] and Rect.y < 600:
        Rect.y += 10
    elif key_pressed[pygame.K_a] and Rect.x > 0:
        Rect.x -= 10
    elif key_pressed[pygame.K_d] and Rect.x < 300:
        Rect.x += 10

def L_Move(key_pressed, Rect):
    if key_pressed[pygame.K_UP] and Rect.y > 0:
        Rect.y -= 10
    elif key_pressed[pygame.K_DOWN] and Rect.y < 600:
        Rect.y += 10
    elif key_pressed[pygame.K_LEFT] and Rect.x > 500:
        Rect.x -= 10
    elif key_pressed[pygame.K_RIGHT] and Rect.x < 800:
        Rect.x += 10

R_BULLETS = []
L_BULLETS = []
Max_Bullets = 6 

def R_and_B(R, B, R_BULLETS, L_BULLETS):
    for r in R_BULLETS:
        r.x += 10
    for l in L_BULLETS:
        l.x -= 10

while True:
    for p in pygame.event.get():
        if p.type == pygame.QUIT:
            pygame.quit()
        if p.type == pygame.KEYDOWN:
            if p.key == pygame.K_z:
                if len(R_BULLETS) < Max_Bullets:
                    A = pygame.Rect(R.x + 39, R.y + 20, 10, 5)
                    R_BULLETS.append(A)
            if p.key == pygame.K_m:
                if len(L_BULLETS) < Max_Bullets:
                    D = pygame.Rect(B.x, B.y + 20, 10, 5)
                    L_BULLETS.append(D)
    K = pygame.key.get_pressed()
    R_Move(K, R)
    L_Move(K, B)
    draw_screen(R, B, R_BULLETS, L_BULLETS)
    R_and_B(R, B, R_BULLETS, L_BULLETS)
    pygame.display.update()