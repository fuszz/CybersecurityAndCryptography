import math

def factor(n):
    factorial = []
    for i in range (2, math.ceil(math.sqrt(n))):
        if n%i == 0:
            factorial.append(i)
            factorial.append(int(n/i))
            
    return factorial

def decrypt(c, d, n):
    return pow(c, d, n)

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

n = 0x140115e871b5a6f
e = 0x10001



# Można też wykorzystać funkcję int(<str z liczbą>, <podstawa systemu>)

encrypted_1 = int("63a584ee99130", 16)
encrypted_2 = int("cd21c3e55366ee", 16)
encrypted_3 = int("d528a0b38d218b", 16)
encrypted_4 = int("10a9dac5fee040d", 16)

# p, q uzyskujemy w wyniku faktoryzacji liczby n
# potem obliczamy fi(n)
# mamy już podane e
# obliczamy liczbę d = pow(e, -1, fi(n))

p, q = factor(n)

if not (is_prime(p) or is_prime(q)):
    print("Liczby nie są pierwsze!")
    exit(0)

fi_n = (p-1)*(q-1)
d = pow(e, -1, fi_n)

m1 = decrypt(encrypted_1, d, n)
m2 = decrypt(encrypted_2, d, n)
m3 = decrypt(encrypted_3, d, n)
m4 = decrypt(encrypted_4, d, n)

print(m1.to_bytes((m1.bit_length() + 7) // 8, 'big').decode('utf-8'))
print(m2.to_bytes((m2.bit_length() + 7) // 8, 'big').decode('utf-8'))
print(m3.to_bytes((m3.bit_length() + 7) // 8, 'big').decode('utf-8'))
print(m4.to_bytes((m4.bit_length() + 7) // 8, 'big').decode('utf-8'))
