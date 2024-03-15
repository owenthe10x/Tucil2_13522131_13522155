import matplotlib.pyplot as plt
import numpy as np

def bezier_curve(points, t):
    if len(points) == 1:
        return points[0]
    else:
        new_points = []
        for i in range(len(points) - 1):
            new_points.append((1 - t) * points[i] + t * points[i + 1])
        return bezier_curve(new_points, t)

def plot_bezier_curve(control_points, num_points=100):
    t_values = np.linspace(0, 1, num_points)
    bezier_points = np.array([bezier_curve(control_points, t) for t in t_values])
    
    plt.figure()
    plt.plot(bezier_points[:, 0], bezier_points[:, 1], 'b-')
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-')
    plt.show()

def get_input():
    control_points = []
    for i in range(3):
        point = input(f"Masukkan titik kontrol {i+1} (format: x,y): ")
        x, y = map(float, point.split(","))
        control_points.append([x, y])
    num_iterations = int(input("Masukkan jumlah iterasi: "))
    return np.array(control_points), num_iterations

if __name__ == "__main__":
    control_points, num_iterations = get_input()
    plot_bezier_curve(control_points, num_iterations + 2)