import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from bruteforce import bezier_bf
from divideandconquer import bezier_dnc
import time


def plot_bezier_curve(control_points, num_points=100, method="bruteforce"):

    fig, ax = plt.subplots()
    (line,) = ax.plot([], [], lw=2)
    (linehelper,) = ax.plot([], [], lw=2)

    points = ax.scatter([], [], color="red")
    pointhelper1 = ax.scatter([], [], color="green")
    pointhelper2 = ax.scatter([], [], color="green")

    def init():
        line.set_data([], [])
        linehelper.set_data([], [])
        return (line,)

    def animate(frame):
        t_values = np.linspace(0, 1, frame + 1)
        bezier_points = []
        total_time = 0

        start_time = time.perf_counter()
        for i in range(len(t_values)):
            if method == "divideandconquer":
                bezier_points.append(bezier_dnc(control_points, t_values[i]))
            else:
                bezier_points.append(bezier_bf(control_points, t_values[i]))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        total_time += elapsed_time
        # Plot control points and lines connecting them
        x = []
        y = []
        for point in bezier_points:
            x.append(point[0])
            y.append(point[1])
        xhelper1 = []
        yhelper1 = []
        line.set_data(x, y)
        for point in control_points:
            ax.plot(point[0], point[1], "bo")
            xhelper1.append(point[0])
            yhelper1.append(point[1])

        linehelper.set_data(xhelper1, yhelper1)
        points.set_offsets(np.column_stack((x, y)))
        # pointhelper1.set_offsets(np.column_stack((xhelper1, yhelper1)))
        # pointhelper2.set_offsets(np.column_stack((xhelper2, yhelper2)))
        ax.set_xlim(
            min(min(x), min(control_points[:, 0])) - 0.1,
            max(max(x), max(control_points[:, 0])) + 0.1,
        )
        ax.set_ylim(
            min(min(y), min(control_points[:, 1])) - 0.1,
            max(max(y), max(control_points[:, 1])) + 0.1,
        )
        # Check if the animation has reached its last frame
        if frame == 0:
            # pause for 2 seconds
            ax.set_title(f"Total time for {method} algorithm: {total_time} seconds")
            time.sleep(2)
        return line, points, linehelper, pointhelper1, pointhelper2

    ani = FuncAnimation(
        fig, animate, frames=num_points, init_func=init, blit=True, repeat=False
    )
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
    print("Metode yang tersedia:")
    print("1. Divide and Conquer")
    print("2. Brute Force")
    method = input("Masukkan metode (1/2): ")
    if method == "1":
        method = "divideandconquer"
    else:
        method = "bruteforce"
    num_iteration = iterasi(num_iterations)
    return np.array(control_points), num_iteration, method


if __name__ == "__main__":
    # control_points, num_iterations, method = get_input()
    control_points = np.array(
        [
            [-2, -3],
            [-3, -2],
            [0, -2],
            [0.5, -2.5],
            [1, -3],
            [2, 1],
        ]
    )
    method = "bruteforce"
    num_iterations = 16
    # +2 karena pada plotting ada 2 frame yang digunakan untuk render titik dan garis kontrol
    plot_bezier_curve(control_points, num_iterations + 2, method)
