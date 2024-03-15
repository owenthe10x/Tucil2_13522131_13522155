import pygame
from positions import Position
from bruteforce import *
from divideandconquer import *

width, height = 1920, 1080
size = (width, height)

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

font = pygame.font.Font("freesansbold.ttf", 32)
smallFont = pygame.font.Font("freesansbold.ttf", 20)
# colors
white = (235, 235, 235)
black = (20, 20, 20)
red = (242, 2, 2)
blue = (2, 146, 242)
color_active = pygame.Color("chartreuse4")
color_passive = pygame.Color("lightskyblue3")

# parameters
t = 0
iteration = 10
active_input = "None"


# results
quadratic_curve_bruteforce = []
quadratic_curve_dnc = []

# components
label_p0x = smallFont.render("x: ", True, black)
label_p0y = smallFont.render("y: ", True, black)
label_p1x = smallFont.render("x: ", True, black)
label_p1y = smallFont.render("y: ", True, black)
label_p2x = smallFont.render("x: ", True, black)
label_p2y = smallFont.render("y: ", True, black)
rect_p0x = label_p0x.get_rect()
rect_p0y = label_p0y.get_rect()
rect_p1x = label_p1x.get_rect()
rect_p1y = label_p1y.get_rect()
rect_p2x = label_p2x.get_rect()
rect_p2y = label_p2y.get_rect()
input_p0x = pygame.Rect(width // 2.3, (height // 4), 50, 25)
input_p0y = pygame.Rect((width // 2.3) + 150, (height // 4), 50, 25)
input_p1x = pygame.Rect(width // 2.3, (height // 4) + 50, 50, 25)
input_p1y = pygame.Rect((width // 2.3) + 150, (height // 4) + 50, 50, 25)
input_p2x = pygame.Rect(width // 2.3, (height // 4) + 100, 50, 25)
input_p2y = pygame.Rect((width // 2.3) + 150, (height // 4) + 100, 50, 25)
text_p0x = ""
text_p0y = ""
text_p1x = ""
text_p1y = ""
text_p2x = ""
text_p2y = ""

run = True
while run:
    screen.fill(white)
    screen.blit(label_p0x, ((width // 2.3) - 20, (height // 4)))
    screen.blit(label_p0y, (((width // 2.3) - 20) + 150, (height // 4)))
    screen.blit(label_p1x, ((width // 2.3) - 20, (height // 4) + 50))
    screen.blit(label_p1y, (((width // 2.3) - 20) + 150, (height // 4) + 50))
    screen.blit(label_p2x, ((width // 2.3) - 20, (height // 4) + 100, 50, 25))
    screen.blit(label_p2y, (((width // 2.3) - 20) + 150, (height // 4) + 100))

    clock.tick(fps)
    pygame.display.set_caption("Bezier Curve Brute Force vs Divide and Conquer ")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_p0x.collidepoint(event.pos):
                active_input = "p0x"
            elif input_p0y.collidepoint(event.pos):
                active_input = "p0y"
            elif input_p1x.collidepoint(event.pos):
                active_input = "p1x"
            elif input_p1y.collidepoint(event.pos):
                active_input = "p1y"
            elif input_p2x.collidepoint(event.pos):
                active_input = "p2x"
            elif input_p2y.collidepoint(event.pos):
                active_input = "p2y"
            else:
                active_input = "None"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            else:
                if active_input == "p0x":
                    if event.key == pygame.K_BACKSPACE:
                        text_p0x = text_p0x[:-1]
                    else:
                        text_p0x += event.unicode
                elif active_input == "p0y":
                    if event.key == pygame.K_BACKSPACE:
                        text_p0y = text_p0y[:-1]
                    else:
                        text_p0y += event.unicode
                elif active_input == "p1x":
                    if event.key == pygame.K_BACKSPACE:
                        text_p1x = text_p1x[:-1]
                    else:
                        text_p1x += event.unicode
                elif active_input == "p1y":
                    if event.key == pygame.K_BACKSPACE:
                        text_p1y = text_p1y[:-1]
                    else:
                        text_p1y += event.unicode
                elif active_input == "p2x":
                    if event.key == pygame.K_BACKSPACE:
                        text_p2x = text_p2x[:-1]
                    else:
                        text_p2x += event.unicode
                elif active_input == "p2y":
                    if event.key == pygame.K_BACKSPACE:
                        text_p2y = text_p2y[:-1]
                    else:
                        text_p2y += event.unicode

    Quadratic = font.render("Brute Force", True, black)
    textRect = Quadratic.get_rect()
    textRect.center = (700, 300)
    screen.blit(Quadratic, textRect)
    Quadratic = font.render("Divide and Conquer", True, black)
    textRect = Quadratic.get_rect()
    textRect.center = (1200, 300)
    screen.blit(Quadratic, textRect)

    color_p0x = color_passive
    color_p0y = color_passive
    color_p1x = color_passive
    color_p1y = color_passive
    color_p2x = color_passive
    color_p2y = color_passive
    if active_input == "p0x":
        color_p0x = color_active
    elif active_input == "p0y":
        color_p0y = color_active
    elif active_input == "p1x":
        color_p1x = color_active
    elif active_input == "p1y":
        color_p1y = color_active
    elif active_input == "p2x":
        color_p2x = color_active
    elif active_input == "p2y":
        color_p2y = color_active

    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(screen, color_p0x, input_p0x)
    pygame.draw.rect(screen, color_p0y, input_p0y)
    pygame.draw.rect(screen, color_p1x, input_p1x)
    pygame.draw.rect(screen, color_p1y, input_p1y)
    pygame.draw.rect(screen, color_p2x, input_p2x)
    pygame.draw.rect(screen, color_p2y, input_p2y)

    text_surface_p0x = font.render(text_p0x, True, (255, 255, 255))
    text_surface_p0y = font.render(text_p0y, True, (255, 255, 255))
    text_surface_p1x = font.render(text_p1x, True, (255, 255, 255))
    text_surface_p1y = font.render(text_p1y, True, (255, 255, 255))
    text_surface_p2x = font.render(text_p2x, True, (255, 255, 255))
    text_surface_p2y = font.render(text_p2y, True, (255, 255, 255))

    # render at position stated in arguments
    screen.blit(text_surface_p0x, (input_p0x.x + 5, input_p0x.y + 5))
    screen.blit(text_surface_p0y, (input_p0y.x + 5, input_p0y.y + 5))
    screen.blit(text_surface_p1x, (input_p1x.x + 5, input_p1x.y + 5))
    screen.blit(text_surface_p1y, (input_p1y.x + 5, input_p1y.y + 5))
    screen.blit(text_surface_p2x, (input_p2x.x + 5, input_p2x.y + 5))
    screen.blit(text_surface_p2y, (input_p2y.x + 5, input_p2y.y + 5))

    # set width of textfield so that text cannot get
    # outside of user's text input
    input_p0x.w = max(100, text_surface_p0x.get_width() + 10)
    input_p0y.w = max(100, text_surface_p0y.get_width() + 10)
    input_p1x.w = max(100, text_surface_p1x.get_width() + 10)
    input_p1y.w = max(100, text_surface_p1y.get_width() + 10)
    input_p2x.w = max(100, text_surface_p2x.get_width() + 10)
    input_p2y.w = max(100, text_surface_p2y.get_width() + 10)

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
    print("t adalah", t)
    quadraticBezier(
        Quadratic_positions_bruteforce,
        t,
        screen,
        blue,
        quadratic_curve_bruteforce,
        red,
    )
    quadraticBezier(Quadratic_positions_dnc, t, screen, blue, quadratic_curve_dnc, red)

    if len(quadratic_curve_bruteforce) > 2:
        pygame.draw.lines(screen, blue, False, quadratic_curve_bruteforce, 5)
    if len(quadratic_curve_dnc) > 2:
        pygame.draw.lines(screen, blue, False, quadratic_curve_dnc, 5)

    if t >= 1:
        t = 0
        quadratic_curve_bruteforce.clear()
        quadratic_curve_dnc.clear()

    # draw points
    for point in Quadratic_positions_bruteforce:
        point.display(screen, black)

    for point in Quadratic_positions_dnc:
        point.display(screen, black)

    t += 1 / iteration
    pygame.display.update()

    pygame.time.wait(500)

pygame.quit()
