import pygame
pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("khung long chay bo")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

VELOCITY_X = 5
VELOCITY_Y = 6


SCORE_FONT = pygame.font.SysFont('time', 20)
GAME_FONT = pygame.font.SysFont('time', 50)

background_x = 0
background_y = 0
dinosaur_x = 20
dinosaur_y = 230
obstacle_x = 550
obstacle_y = 230
score = 0

BACKGROUND = pygame.image.load(r'D:\LaptrinhPython\Dinosaur_run\background.jpg')
DINOSAUR = pygame.image.load(r'D:\LaptrinhPython\Dinosaur_run\dinosaur.png')
OBSTACLE = pygame.image.load(r'D:\LaptrinhPython\Dinosaur_run\obstacles.png')

clock = pygame.time.Clock()
FPS = 60
run = True
jump = False
while run:
    screen.fill(WHITE)
    background_rect = screen.blit(BACKGROUND, (background_x, background_y))
    background_rect_next = screen.blit(BACKGROUND, (background_x + 600, background_y))
    if background_x + 600 <= 0:
        background_x = 0
    background_x -= VELOCITY_X
    
    dinosaur_rect = screen.blit(DINOSAUR, (dinosaur_x, dinosaur_y))
    obstacle_rect = screen.blit(OBSTACLE, (obstacle_x, obstacle_y))
    
    score_text = SCORE_FONT.render("Score: " + str(score), 1, RED)
    screen.blit(score_text, (10, 10))
        
    if obstacle_x <= -20:
        obstacle_x = 550
        score += 1
    obstacle_x -= VELOCITY_X
    
    if 120 <= dinosaur_y <= 230:
        if jump == True:
            dinosaur_y -= VELOCITY_Y
    else:
        jump = False
        
    if dinosaur_y < 230:
        if jump == False:
            dinosaur_y += VELOCITY_Y
    
    if dinosaur_rect.colliderect(obstacle_rect):
        game_over_text = GAME_FONT.render("GAME OVER", 1, RED)
        screen.blit(game_over_text, (200, 150))
        VELOCITY_X = 0
            
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
            
    pygame.display.flip()
pygame.quit()