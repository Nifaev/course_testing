from math import sqrt


def solve_quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError

    d = b * b - 4 * a * c

    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return min(x1, x2), max(x1, x2)
