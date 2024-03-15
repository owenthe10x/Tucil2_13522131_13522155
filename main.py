import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from bruteforce import quadratic_bezier_bf, plot_curve
from divideandconquer import quadratic_bezier_dnc, get_input
import time
import datetime


def plot_bezier_curve(control_points, num_points=100, method="bruteforce"):
    fig, ax = plt.subplots()
    (line,) = ax.plot([], [], lw=2)
    (linec,) = ax.plot([], [], lw=2)

    points = ax.scatter([], [], color="red")
    pointc = ax.scatter([], [], color="green")

    def init():
        line.set_data([], [])
        linec.set_data([], [])
        return (line,)

    def animate(frame):
        t_values = np.linspace(0, 1, frame + 1)
        bezier_points = []
        start_time = time.perf_counter()
        for i in range(len(t_values)):
            if method == "divideandconquer":
                bezier_points.append(quadratic_bezier_dnc(control_points, t_values[i]))
            else:
                bezier_points.append(quadratic_bezier_bf(control_points, t_values[i]))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        elapsed_time_str = str(datetime.timedelta(seconds=elapsed_time))

        # Plot control points and lines connecting them
        x = [control_points[2, 0], control_points[1, 0]]
        y = [control_points[2, 1], control_points[1, 1]]
        for point in bezier_points:
            x.append(point[0])
            y.append(point[1])
        line.set_data(x, y)
        points.set_offsets(np.column_stack((x, y)))
        ax.set_xlim(
            min(min(x), min(control_points[:, 0])) - 0.1,
            max(max(x), max(control_points[:, 0])) + 0.1,
        )
        ax.set_ylim(
            min(min(y), min(control_points[:, 1])) - 0.1,
            max(max(y), max(control_points[:, 1])) + 0.1,
        )
        ax.text(
            0.02,
            0.95,
            f"Elapsed Time: {elapsed_time_str} seconds",
            transform=ax.transAxes,
            color="black",
            fontsize=12,
            ha="center",
        )

        return line, points

    ani = FuncAnimation(fig, animate, frames=num_points, init_func=init, blit=True)
    plt.show()


def get_input():
    control_points = []
    for i in range(3):
        point = input(f"Masukkan titik kontrol {i+1} (format: x,y): ")
        x, y = map(float, point.split(","))
        control_points.append([x, y])
    num_iterations = int(input("Masukkan jumlah iterasi: "))
    method = input("Masukkan metode (divideandconquer or bruteforce): ")
    return np.array(control_points), num_iterations, method


if __name__ == "__main__":
    control_points, num_iterations, method = get_input()
    plot_bezier_curve(control_points, num_iterations + 2, method)
