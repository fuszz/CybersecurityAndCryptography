def rozszerzony_euklides(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = rozszerzony_euklides(b, a % b)
        return g, y, x - (a // b) * y

def odwrotnosc_modularna(e, phi_n):
    g, x, y = rozszerzony_euklides(e, phi_n)
    if g != 1:
        raise ValueError("Brak odwrotności modularnej")
    else:
        return x % phi_n

e = 65537
phi_n = 8740
d = odwrotnosc_modularna(e, phi_n)
print(f"Klucz prywatny d: {d}")

# Zamiana szyfrogramu na liczbę dziesiętną
cipher = 0x63a584ee99130cd21c3e55366eed528a0b38d218b10a9dac5fee040d

# Odszyfrowanie wiadomości za pomocą pow
n = 9007199254740991  # Klucz publiczny
message = pow(cipher, d, n)

# Konwersja odszyfrowanej wiadomości na bajty i na tekst
message_bytes = message.to_bytes((message.bit_length() + 7) // 8, 'big')
message_text = message_bytes.decode('utf-8')

print(f"Odszyfrowana wiadomość: {message_text}")
