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

def plot_bezier_curve(control_points, num_points=100):
    t_values = np.linspace(0, 1, num_points)
    bezier_points = np.array([bezier_curve(control_points, t) for t in t_values])
    
    plt.figure()
    plt.plot(bezier_points[:, 0], bezier_points[:, 1], 'b-')
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-')
    plt.show()


