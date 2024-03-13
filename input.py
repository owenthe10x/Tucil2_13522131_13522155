import pygame, sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))
base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(875, 580, 140, 32)
color = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
nyala = color_passive

black = (20,20,20)

inputs = []
active = False

while True:
    screen.fill((255, 255, 255))

    for i in range (0,2):
        Quadratic = base_font.render("Masukkan input kedalam box dibawah ini:", True, black)
        textRect = Quadratic.get_rect()
        textRect.center = (960, 500)
        screen.blit(Quadratic, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        if len(user_text) > 0:  # Check if there's any text to delete
                            user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        inputs.append(user_text)
                        user_text = ''
                        print(inputs)
                    else:
                        user_text += event.unicode

    if active:
        nyala = color
    else:
        nyala = color_passive

    pygame.draw.rect(screen, nyala, input_rect, 2)

    text_surface = base_font.render(user_text, True, (20, 20, 20))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(175,text_surface.get_width() + 10)

    pygame.display.update()
    clock.tick(60)