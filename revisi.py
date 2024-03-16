import matplotlib.pyplot as plt
import numpy as np

def divide_n_conquer(points, t):
    if len(points) == 1:
        return points[0]
    else:
        left_points = [point for point in points[:-1]]
        right_points = [point for point in points[1:]]
        return (1 - t) * divide_n_conquer(left_points, t) + t * divide_n_conquer(right_points, t)

def bezier_curve(control_points, t):
    return divide_n_conquer(control_points, t)

def plot_bezier_curve(control_points, num_points):
    t_values = np.linspace(0, 1, num_points)
    bezier_points = np.array([bezier_curve(control_points, t) for t in t_values])
    
    plt.figure()
    plt.plot(bezier_points[:, 0], bezier_points[:, 1], 'b-')
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-')
    plt.show()

def iterasi(n):
    if n == 1:
        return 1
    else:
        return 2 * iterasi(n - 1) + 1

def get_input():
    control_points = []
    titik = int(input("Masukkan jumlah titik kontrol: "))
    for i in range(titik):
        point = input(f"Masukkan titik kontrol {i+1} (format: x,y): ")
        x, y = map(float, point.split(","))
        control_points.append([x, y])
    num_iterations = int(input("Masukkan jumlah iterasi: "))
    num_iteration = iterasi(num_iterations)
    return np.array(control_points), num_iteration

if __name__ == "__main__":
    control_points, num_iterations = get_input()
    plot_bezier_curve(control_points, num_iterations + 2)