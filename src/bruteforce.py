import math


def bezier_bf(positions, t):
    x = 0
    y = 0
    n = len(positions) - 1
    for i in range(len(positions)):
        coeff = math.comb(n, i) * ((1 - t) ** (n - i)) * (t**i)
        x += coeff * positions[i][0]
        y += coeff * positions[i][1]
    return [x, y]
