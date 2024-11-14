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

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a%b)

p = 180182183
q = 499999993
d = 68678011418660993
n = p*q
fi_n = (p-1)*(q-1)

poss_e_list = []

#for i in range(2, fi_n-1):
#    print(i)
#    if gcd(i, fi_n) == 1:
#        poss_e_list.append(i)

#print(poss_e_list)
poss_e_list = []
# Można też wykorzystać funkcję int(<str z liczbą>, <podstawa systemu>)

encrypted_1 = int("63a584ee99130", 16)

for e in poss_e_list:
    d = pow(e, -1, n)
    m = encrypted_1.to_bytes((encrypted_1.bit_length() + 7) // 8, 'big').decode('utf-8')
    print("Odnaleziono rozwiązanie: e = ", e, "Tekst = ", m)


