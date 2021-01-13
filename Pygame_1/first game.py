import pygame
import ball
import player

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

player = player.player(250, 480)
ball = ball.ball(350, 250, 30, 20)


def redrawGameWindow():
    win.fill((0, 0, 0))
    player.draw(win)
    ball.draw(win)
    pygame.display.update()


# mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.vel:
        player.x += player.vel

    ball.move()

    redrawGameWindow()

pygame.quit()
