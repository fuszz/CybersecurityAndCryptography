import random
import math
from sympy import mod_inverse

UPPER_BORDER = 9999

def is_primitive_number(a):
    if a < 2:
        return False
    for i in range(2, math.ceil(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

def euler_function(p, q):
    return (p - 1) * (q - 1)

def euklides(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def cipher(m, e, n):
    return (m ** e) % n

def decipher(c, d, n):
    return (c ** d) % n

def gen_d(euler_n, e):
    return mod_inverse(e, euler_n)

# Generowanie liczb pierwszych p i q
p, q = 4, 4
while not is_primitive_number(p):
    p = random.randint(3, UPPER_BORDER)

while not is_primitive_number(q):
    q = random.randint(3, UPPER_BORDER)

print(f"Generated primes: p = {p}, q = {q}")

n = p * q
euler_n = euler_function(p, q)

# Generowanie klucza publicznego e
e = random.randint(2, euler_n - 1)
while euklides(euler_n, e) != 1:
    e = random.randint(2, euler_n - 1)

# Generowanie klucza prywatnego d
d = gen_d(euler_n, e)

print(f"Public key: e = {e}, n = {n}")
print(f"Private key: d = {d}, n = {n}")

# Szyfrowanie i deszyfrowanie wiadomości
m = 8
c = cipher(m, e, n)
print(f"Encrypted message: {c}")

decrypted_message = decipher(c, d, n)
print(f"Decrypted message: {decrypted_message}")
