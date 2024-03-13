import numpy as np
import matplotlib.pyplot as plt

def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

def bezier_curve(points, t):
    n = len(points) - 1
    curve_point = np.zeros(2)
    for i in range(n + 1):
        curve_point += binomial_coefficient(n, i) * ((1 - t) ** (n - i)) * (t ** i) * points[i]
    return curve_point

def divide_and_conquer_bezier(points, t, iterations):
    if iterations == 0:
        return points[0]
    else:
        divided_points = []
        for i in range(len(points) - 1):
            divided_point = (1 - t) * points[i] + t * points[i + 1]
            divided_points.append(divided_point)
        return divide_and_conquer_bezier(divided_points, t, iterations - 1)

def plot_bezier_curve(points, iterations, num_points=100):
    curve_points = []
    for t in np.linspace(0, 1, num_points):
        curve_point = divide_and_conquer_bezier(points, t, iterations)
        curve_points.append(curve_point)
    curve_points = np.array(curve_points)
    plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='Bézier Curve')
    plt.plot(points[:, 0], points[:, 1], 'ro-', label='Control Points')
    plt.title('Bézier Curve with Control Points after {} iterations'.format(iterations))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Input
def get_input():
    points = []
    for i in range(3):
        x, y = map(float, input(f"Masukkan koordinat titik {i+1} (format: x y): ").split())
        points.append([x, y])
    iterations = int(input("Masukkan jumlah iterasi: "))
    return np.array(points), iterations

# Example usage:
if __name__ == "__main__":
    control_points, iterations = get_input()
    plot_bezier_curve(control_points, iterations)
