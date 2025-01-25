import rsa_key_pair

def encrypt_message(message):
    n, e, d = rsa_key_pair.gen_keys()
    
    m = int.from_bytes(message.encode('utf-8'), 'big')
    return pow(m, e, n), d, n
    
    
print(encrypt_message("Hel"))

# Uwaga - przyjęta długość klucza pozwala zaszyfrować tekst o długości max 3 znaków.
# Tekst można podzielić na bloki. A lepiej wydłużyć klucz.