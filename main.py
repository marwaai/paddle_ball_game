import pygame  # import pygame library
import random  # import random library

pygame.init()  # initialize pygame

# 1️⃣ Setup the game window
screen = pygame.display.set_mode((600, 600))  # create a 600x600 window
pygame.display.set_caption("Ball Game")  # set the game title
clock = pygame.time.Clock()  # clock to control game speed

# 2️⃣ Game variables
running = True        # is the game running?
x = 0                 # paddle position (mouse x)
xc = 10               # ball x position
yc = 0                # ball y position
score = 0             # score counter
gameover = False      # game over flag
font = pygame.font.Font(None, 36)  # font for text

# 3️⃣ Game loop
while running:
    # 3.1 Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit if window closed
            running = False

    # 3.2 Fill background
    screen.fill((255, 0, 0))  # red background

    if not gameover:
        # 3.3 Move ball down
        yc = yc + 3

        # 3.4 Draw ball
        h = pygame.draw.circle(screen, (255, 255, 255), (xc, yc), 10)

        # 3.5 Draw paddle (follows mouse)
        x = pygame.mouse.get_pos()[0]
        d = pygame.draw.rect(screen, (255, 255, 255), (x, 500, 200, 50))

        # 3.6 Collision: ball hits paddle
        if h.colliderect(d):
            score += 1
            yc = 0
            xc = random.randint(0, 500)

        # 3.7 Draw score
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text, (10, 10))

        # 3.8 Ball missed (game over)
        if yc > 550:
            gameover = True
    else:
        # 3.9 Show Game Over screen
        text = font.render("Game Over", True, (255, 255, 255))
        screen.blit(text, (200, 300))

        # 3.10 Restart if mouse clicked
        if pygame.mouse.get_pressed()[0]:
            gameover = False
            score = 0
            yc = 0

    # 3.11 Update screen
    pygame.display.flip()
    clock.tick(60)  # run at 60 FPS

pygame.quit()  # quit pygame
