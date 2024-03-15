import matplotlib.pyplot as plt
import numpy as np
#import pygame


'''def linearBezier(positions, t, screen, color, draw=True):
    x0 = (1 - t) * positions[0].x
    y0 = (1 - t) * positions[0].y

    x1 = t * positions[1].x
    y1 = t * positions[1].y

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
'''

def quadratic_bezier(positions, t):
    x0 = pow((1 - t), 2) * positions[0][0]
    y0 = pow((1 - t), 2) * positions[0][1]

    x1 = 2 * (1 - t) * t * positions[1][0]
    y1 = 2 * (1 - t) * t * positions[1][1]

    x2 = pow(t, 2) * positions[2][0]
    y2 = pow(t, 2) * positions[2][1]

    return [x0 + x1 + x2, y0 + y1 + y2]

def plot_curve(positions):
    t_values = np.linspace(0, 1, 100)
    curve_points = np.array([quadratic_bezier(positions, t) for t in t_values])

    plt.figure()
    plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-')
    plt.plot([p[0] for p in positions], [p[1] for p in positions], 'ro-')
    plt.show()

# Example usage:
if __name__ == "__main__":
    positions = [[0, 0], [1, 3], [2, -1]]
    plot_curve(positions)
