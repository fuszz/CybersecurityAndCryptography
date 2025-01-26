import Crypto.Random as rnd
import Crypto.Util.Padding as pad
from Crypto.Cipher import AES
import Crypto.Util.Counter as cnt

def read_file(filepath):
    with open(filepath, "rb") as f:
        content = f.read()
    return content[:54], content[54:]

def save_file(filepath, header, body):
    with open(filepath, "wb") as f:
        f.write(header+body)

def gen_key(size):
    return rnd.get_random_bytes(size)

def gen_initial_vector(size):
    return rnd.get_random_bytes(size)

def gen_counter():
    return cnt.new(128)

def pad_data(data, padsize):
    return pad.pad(data, padsize)

def encrypt_AES_ECB(padded_body, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(padded_body)

def encrypt_AES_CBC(padded_body, key, initial_vector):
    cipher = AES.new(key, AES.MODE_CBC, initial_vector)
    return cipher.encrypt(padded_body)

def encrypt_AES_CFB(padded_body, key, initial_vector):
    cipher = AES.new(key, AES.MODE_CFB, initial_vector)
    return cipher.encrypt(padded_body)

def encrypt_AES_OFB(padded_body, key, initial_vector):
    cipher = AES.new(key, AES.MODE_OFB, initial_vector)
    return cipher.encrypt(padded_body)


def encrypt_AES_CTR(padded_body, key, ctr):
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(padded_body)

def decrypt_AES_CBC(encrypted_body, key, initial_vector):
    cipher = AES.new(key, AES.MODE_CBC, initial_vector)
    return cipher.decrypt(encrypted_body)


def save_key_and_initial_vector(filepath, key, initial_vector):
    with open(filepath, "w") as f:
        f.write(key.hex())
        f.write('\n')
        f.write(initial_vector.hex())

header, body = read_file("tux.bmp")
padded_body = pad_data(body, 16)

key = gen_key(16)
initial_vector = gen_initial_vector(16)

encrypted_body_ecb = encrypt_AES_ECB(padded_body, key)
save_file("z1_enc_ecb.bmp", header, encrypted_body_ecb)

encrypted_body_cbc = encrypt_AES_CBC(padded_body, key, initial_vector)
save_file("z1_enc_cbc.bmp", header, encrypted_body_cbc)

encrypted_body_cfb = encrypt_AES_CFB(padded_body, key, initial_vector)
save_file("z1_enc_cfb.bmp", header, encrypted_body_cfb)

encrypted_body_ofb = encrypt_AES_OFB(padded_body, key, initial_vector)
save_file("z1_enc_ofb.bmp", header, encrypted_body_ofb)

encrypted_body_ctr = encrypt_AES_CTR(padded_body, key, gen_counter())
save_file("z1_enc_ctr.bmp", header, encrypted_body_ctr)

save_key_and_initial_vector("z1_key_and_iv.txt", key, initial_vector)


header, encrypted_body_cbc = read_file("z1_enc_cbc.bmp")
decrypted_body = decrypt_AES_CBC(encrypted_body_cbc, key, initial_vector)
save_file("z1_decrypted.bmp", header, decrypted_body)