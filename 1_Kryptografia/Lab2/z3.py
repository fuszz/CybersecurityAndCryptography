import Crypto.Cipher.AES as AES


def read_file(filepath):
    with open(filepath, "rb") as f:
        content = f.read()
    return content[:54], content[54:]

def read_str(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    return content

def save_file(filepath, header, body):
    with open(filepath, "wb") as f:
        f.write(header+body)
        
def decrypt(encryption_mode, encrypted_body, key, initial_vector):
    cipher = AES.new(key, AES.MODE_CBC, initial_vector)
    return cipher.decrypt(encrypted_body)

key, initial_vector = read_str("z1_key_and_iv.txt").split()
print(key)
print(initial_vector)
header, encrypted_body = read_file("z2_modified.bmp")
decrypted_body = decrypt(AES.MODE_CBC, encrypted_body, bytes.fromhex(key), bytes.fromhex(initial_vector))
save_file("z3_decrypted.bmp", header, decrypted_body)