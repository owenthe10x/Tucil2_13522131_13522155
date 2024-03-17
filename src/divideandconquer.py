def bezier_dnc(points, t):
    if len(points) == 1:
        return points[0]
    else:
        left_points = [point for point in points[:-1]]
        right_points = [point for point in points[1:]]
        return (1 - t) * bezier_dnc(left_points, t) + t * bezier_dnc(right_points, t)
