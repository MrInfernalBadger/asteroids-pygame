import math


def generate_rotations(points):
    """Generates a dictionary of polygons for each degree of rotation

    Args:
        points (list of tupes): A list of tuples of x, y coordinates of a polygon
    """
    result = []
    angle = 180
    for point in points:
        x = (point[0] * math.cos(angle)) - (point[1] * math.sin(angle))
        y = (point[1] * math.cos(angle)) + (point[0] * math.sin(angle))
    
    # for degree in range(360):
    #     print(degree)


# generate_rotations([(0, 20), (-10, -20), (10, -20)])
generate_rotations([(1, 1)])