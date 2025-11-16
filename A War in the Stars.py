import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))

E = pygame.image.load("A.png")
C = pygame.transform.rotate(E, -90)
F = pygame.image.load("B.png")
D = pygame.transform.rotate(F, 90)
S = pygame.image.load("s.jpg")
S = pygame.transform.scale(S, (WIDTH, HEIGHT))
pygame.font.init()
health_font = pygame.font.SysFont("Comic Sans MS", 36)

def draw_screen(R, L, A, B, AA, AB):
    Screen.blit(S, (0,0))
    Screen.blit(C, (R.x, R.y))
    Screen.blit(D, (L.x, L.y))
    for Re in A:
        pygame.draw.rect(Screen, "red", Re)
    for Le in B:
        pygame.draw.rect(Screen, "blue", Le)
    rectangle = pygame.Rect(390, 0, 20, 600)
    pygame.draw.rect(Screen, "black", rectangle)
    A_health = health_font.render("Health: " + str(AA), 1, "black")
    Screen.blit(A_health, (60,60))
    B_health = health_font.render("Health: " + str(AB), 1, "black")
    Screen.blit(B_health, (550,60))

R = pygame.Rect(100, 500, 39, 39)
B = pygame.Rect(650, 500, 39, 39)
Rshoot = pygame.USEREVENT + 1
Bshoot = pygame.USEREVENT + 2
RH = 10
LH = 10
def R_move(key_pressed, Rect):
    if key_pressed[pygame.K_a] and Rect.x > 0:
        Rect.x -= 10
    elif key_pressed[pygame.K_d] and Rect.x < 350:
        Rect.x += 10
    elif key_pressed[pygame.K_w] and Rect.y > 0:
        Rect.y -= 10
    elif key_pressed[pygame.K_s] and Rect.y < 600:
        Rect.y += 10
        
def L_move(key_pressed, Rect):
    if key_pressed[pygame.K_LEFT] and Rect.x > 420:
        Rect.x -= 10
    elif key_pressed[pygame.K_RIGHT] and Rect.x < 800:
        Rect.x += 10
    elif key_pressed[pygame.K_UP] and Rect.y > 0:
        Rect.y -= 10
    elif key_pressed[pygame.K_DOWN] and Rect.y < 600:
        Rect.y += 10

R_BULLETS = []
L_BULLETS = []
Max_Bullets = 6

def R_and_B(R, B, R_BULLETS, L_BULLETS):
    for r in R_BULLETS:
        r.x += 10
        if r.colliderect(B):
            pygame.event.post(pygame.event.Event(Rshoot))
            R_BULLETS.remove(r)
    for l in L_BULLETS:
        l.x -= 10
        if l.colliderect(R):
            pygame.event.post(pygame.event.Event(Bshoot))
            L_BULLETS.remove(l)

AA = 10
AB = 10

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
                    G = pygame.Rect(B.x, B.y + 20, 10, 5)
                    L_BULLETS.append(G)
        if p.type == Rshoot:
            AB -= 2
            print(AB)
        elif p.type == Bshoot:
            AA -= 2
            print(AA)
    WINNER = ""
    if AA == 0:
        AC = health_font.render("WINNER = BLUE SPACESHIP!!!", 1, "black")
        Screen.blit(AC, (400,400))
        pygame.display.update()
        pygame.time.delay(5000)
        break
    elif AB == 0:
        AD = health_font.render("WINNER = RED SPACESHIP!!!", 1, "black")
        Screen.blit(AD, (400,400))
        pygame.display.update()
        pygame.time.delay(5000)
        break
    K = pygame.key.get_pressed()
    R_move(K, R)
    L_move(K, B)
    draw_screen(R, B, R_BULLETS, L_BULLETS, AA, AB)
    R_and_B(R, B, R_BULLETS, L_BULLETS)
    pygame.display.update()