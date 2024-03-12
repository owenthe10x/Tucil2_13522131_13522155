import pygame
from positions import Position
from curves import *

width, height = 1920, 1080
size = (width, height)

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

font = pygame.font.Font("freesansbold.ttf", 32)

# colors
white = (235, 235, 235)
black = (20, 20, 20)
red = (242, 2, 2)
blue = (2, 146, 242)

# parameters
time = 0
speed = 0.002
Quadratic_positions_bruteforce = [
    Position(600, 650, "P0"),
    Position(800, 550, "P1"),
    Position(700, 450, "P2"),
]
Quadratic_positions_dnc = [
    Position(1100, 650, "P0"),
    Position(1300, 550, "P1"),
    Position(1200, 450, "P2"),
]

# results
quadratic_curve_bruteforce = []
quadratic_curve_dnc = []

run = True
while run:
    screen.fill(white)
    clock.tick(fps)
    pygame.display.set_caption("Bezier Curve Brute Force vs Divide and Conquer ")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    Quadratic = font.render("Brute Force", True, black)
    textRect = Quadratic.get_rect()
    textRect.center = (700, 300)
    screen.blit(Quadratic, textRect)
    Quadratic = font.render("Divide and Conquer", True, black)
    textRect = Quadratic.get_rect()
    textRect.center = (1200, 300)
    screen.blit(Quadratic, textRect)

    quadraticBezier(
        Quadratic_positions_bruteforce, time, screen, blue, quadratic_curve_bruteforce, red
    )
    quadraticBezier(Quadratic_positions_dnc, time, screen, blue, quadratic_curve_dnc, red)

    if len(quadratic_curve_bruteforce) > 2:
        pygame.draw.lines(screen, blue, False, quadratic_curve_bruteforce, 5)
    if len(quadratic_curve_dnc) > 2:
        pygame.draw.lines(screen, blue, False, quadratic_curve_dnc, 5)

    if time >= 1:
        time = 0
        quadratic_curve_bruteforce.clear()
        quadratic_curve_dnc.clear()

    # draw points
    for point in Quadratic_positions_bruteforce:
        point.display(screen, black)

    for point in Quadratic_positions_dnc:
        point.display(screen, black)

    time += speed
    pygame.display.update()

pygame.quit()
