import math
import matplotlib.pyplot as plt
import numpy as np


def get_points(a, b, p):
    def is_quadratic_residue(n, p):
        """Sprawdza, czy liczba n jest resztą kwadratową modulo p."""
        return pow(n, (p - 1) // 2, p) == 1

    points = []
    for x in range(p):
        # Oblicz prawą stronę równania y^2 ≡ x^3 + ax + b (mod p)
        rhs = (x**3 + a * x + b) % p
        if is_quadratic_residue(rhs, p):  # Sprawdź, czy y^2 ma rozwiązanie
            for y in range(p):
                if (y * y) % p == rhs:
                    points.append((x, y))
    points.append((None, None))  # Punkt w nieskończoności
    return points


points = get_points(2, 3, 17)
X = [a[0] for a in points]
Y = [a[1] for a in points]

plt.plot(X, Y, '.')
plt.show()