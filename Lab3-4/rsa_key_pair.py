import math
import random

def euler(p, q):
    return (p-1)*(q-1)

def gen_keys():
    p = 7433
    q = 9941

    n = p*q
    euler_n = euler(p, q)

    e = random.randint(2, euler_n-1)
    while math.gcd(e, euler_n) != 1:
        e = random.randint(2, euler_n-1)
    d = pow(e, -1, euler_n)

    return n, e, d