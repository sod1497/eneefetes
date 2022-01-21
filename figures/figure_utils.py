import math


def rotate(x: int, y: int, angle: int):
    """
    Calculates a new pair of (x,y) as a result of rotating the coordinates using (0,0) as center
    :param x:
    :param y:
    :param angle:
    :return:
    """

    actual_angle = angle_from_origin(x, y)
    new_angle = actual_angle + angle
    radious = distance_to_origin(x, y)
    new_x = radious * math.cos(math.radians(new_angle))
    new_y = radious * math.sin(math.radians(new_angle))
    return new_x, new_y


def angle_from_origin(x: int, y: int):
    """
    Returns the angle of the line that crosses the origin and (x,y) with the X+ axis
    :param x:
    :param y:
    :return:
    """
    return angle_line_x(0, 0, x, y)


def angle_line_x(x1: int, y1: int, x2: int, y2: int):
    """
    Return the angle of the line formed by two points with the X+ axis
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    if (x2 - x1) != 0:
        angle = math.atan((y2 - y1) / (x2 - x1))
    else:
        angle = math.radians(-90)

    angle_d = math.degrees(angle)
    if x2 < x1 or (x1 == x2 and x1 < 0):
        angle_d = angle_d + 180
    while angle_d < 0:
        angle_d = 360 + angle_d

    return angle_d


def distance_to_origin(x: int, y: int):
    return distance_between_points(0, 0, x, y)


def distance_between_points(x1: int, y1: int, x2: int, y2: int):
    return math.sqrt((abs(y2 - y1) ** 2) + (abs(x2 - x1) ** 2))
