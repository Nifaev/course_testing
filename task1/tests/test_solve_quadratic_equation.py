import pytest

from quadratic_equation.solve_quadratic_equation import solve_quadratic_equation


def test_zero_a():
    with pytest.raises(ValueError):
        solve_quadratic_equation(0, 1, -3)


def test_no_roots():
    result = solve_quadratic_equation(9, 2, 1)
    assert result is None


def test_one_root():
    result = solve_quadratic_equation(1, 2, 1)
    assert result == -1.0


def test_two_roots():
    result = solve_quadratic_equation(1, -5, 4)
    assert result == (1.0, 4.0)

