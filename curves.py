import pygame


def linearBezier(positions, time, screen, color, draw=True):
    x0 = (1 - time) * positions[0].x
    y0 = (1 - time) * positions[0].y

    x1 = time * positions[1].x
    y1 = time * positions[1].y

    curve = (x0 + x1, y0 + y1)

    if draw == True:
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (positions[0].x, positions[0].y),
            (positions[1].x, positions[1].y),
            1,
        )
        pygame.draw.line(
            screen,
            color,
            (positions[0].x, positions[0].y),
            (int(curve[0]), int(curve[1])),
            5,
        )
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    elif draw == False:
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
        return (int(curve[0]), int(curve[1]))


def quadraticBezier(positions, time, screen, color, curve_list, green, draw=True):

    x0 = pow((1 - time), 2) * positions[0].x
    y0 = pow((1 - time), 2) * positions[0].y

    x1 = 2 * (1 - time) * time * positions[1].x
    y1 = 2 * (1 - time) * time * positions[1].y

    x2 = time**2 * positions[2].x
    y2 = time**2 * positions[2].y

    curve = (x0 + x1 + x2, y0 + y1 + y2)
    if draw == True:
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (positions[0].x, positions[0].y),
            (positions[1].x, positions[1].y),
            1,
        )
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (positions[1].x, positions[1].y),
            (positions[2].x, positions[2].y),
            1,
        )
        first_line = [positions[0], positions[1]]
        second_line = [positions[1], positions[2]]

        a = linearBezier(first_line, time, screen, green, False)
        b = linearBezier(second_line, time, screen, green, False)

        pygame.draw.line(screen, green, a, b, 2)
        pygame.draw.circle(screen, color, (int(curve[0]), int(curve[1])), 8)
    curve_list.append((int(curve[0]), int(curve[1])))
