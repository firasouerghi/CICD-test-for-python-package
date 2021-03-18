import numpy as np
from scipy.optimize import fsolve


def circle_area(r):
    """Given the radius, calculates the area of a circle

    Args:
        r (float): radius of the circle

    Raises:
        ValueError: if the argument is not a float

    Returns:
        float: the area of the circle
    """

    if not isinstance(r, float):
        raise ValueError('Wrong argmument type')

    rsqr = r**2
    area = np.pi * rsqr
    return np.round(area)


def square_area(l):
    """Given the length of the side, calculates the area of a square

    Args:
        l (float): length of the side

    Raises:
        ValueError: if the argument is not a float

    Returns:
        float: the area of the square
    """
    if not isinstance(l, float):
        raise ValueError('Wrong argmument type')

    area = l**2
    return np.round(area)


if __name__ == '__main__':
    l = 10.0
    r = 5.644

    print(f'The area of a square with l={l} cm is {square_area(l)} cm²')
    print(f'The area of a circle with r={r} cm is {circle_area(r)} cm²')
