import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def quadratic_bezier_dnc(points, t):
    if len(points) == 1:
        return points[0]
    else:
        left_points = [point for point in points[:-1]]
        right_points = [point for point in points[1:]]
        return (1 - t) * quadratic_bezier_dnc(left_points, t) + t * quadratic_bezier_dnc(
            right_points, t
        )

def get_input():
    control_points = []
    for i in range(3):
        point = input(f"Masukkan titik kontrol {i+1} (format: x,y): ")
        x, y = map(float, point.split(","))
        control_points.append([x, y])
    num_iterations = int(input("Masukkan jumlah iterasi: "))
    return np.array(control_points), num_iterations


