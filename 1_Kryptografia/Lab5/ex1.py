import matplotlib.pyplot as plt
from math import sqrt, isqrt

def get_points(a, b, p):
    X = range(0, 300, 2)
    Y = []
    for x in X:
        rhs = (x**3 + a * x + b) % p  # Prawa strona równania y^2 = x^3 + ax + b
        y = sqrt(rhs) if rhs >= 0 else float('nan')
        Y.append(y)
    return tuple(zip(X, Y))

# Parametry secp256k1
points1 = get_points(0, 7, 2**256 - 2**32 - 977)
plt.plot([x[0] for x in points1], [x[1] for x in points1], '.r', label='secp256k1')

# Parametry secp256r1
points2 = get_points(-3, 4105836372515214212932612978004726840911444101599372555481690190577, 2**256 - 2**224 + 2**192 + 2**96 - 1)
plt.plot([x[0] for x in points2], [x[1] for x in points2], 'ob', label='secp256r1')

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Elliptic Curve Points")
plt.show()
