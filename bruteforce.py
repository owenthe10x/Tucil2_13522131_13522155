import math


def linear_bezier_bf(positions, t):
    x0 = (1 - t) * positions[0][0]
    y0 = (1 - t) * positions[0][1]

    x1 = t * positions[1][0]
    y1 = t * positions[1][1]

    return [x0 + x1, y0 + y1]


def quadratic_bezier_bf(positions, t):
    x0 = pow((1 - t), 2) * positions[0][0]
    y0 = pow((1 - t), 2) * positions[0][1]

    x1 = 2 * (1 - t) * t * positions[1][0]
    y1 = 2 * (1 - t) * t * positions[1][1]

    x2 = pow(t, 2) * positions[2][0]
    y2 = pow(t, 2) * positions[2][1]

    return [x0 + x1 + x2, y0 + y1 + y2]


def bezier_bf(positions, t):
    x = 0
    y = 0
    n = len(positions) - 1
    for i in range(len(positions)):
        coeff = math.comb(n, i) * ((1 - t) ** (n - i)) * (t**i)
        x += coeff * positions[i][0]
        y += coeff * positions[i][1]
    return [x, y]
