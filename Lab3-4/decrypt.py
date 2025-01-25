import math

def decrypt(cipher, priv_key, mod):
    
    m = pow(cipher, priv_key, mod)
    message = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode('utf-8')
    return message

print(decrypt(9081546, 55309699, 73891453))