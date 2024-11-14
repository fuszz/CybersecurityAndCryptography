import random

def modify_bytes(input_filename, output_filename, byte_modifications):
    """
    Funkcja do modyfikacji wybranych bajtów w pliku.
    :param input_filename: Nazwa wejściowego pliku (zaszyfrowanego obrazu BMP)
    :param output_filename: Nazwa wyjściowego pliku z wprowadzonymi zmianami
    :param byte_modifications: Lista krotek zawierających pozycję bajtu i nową wartość bajtu
    [(position1, new_byte1), (position2, new_byte2), ...]
    """
    # Wczytanie zaszyfrowanego obrazu
    with open(input_filename, 'rb') as f:
        file_data = bytearray(f.read())
        
    print(len(file_data))
    header = file_data[:54]
    file_data = file_data[54:]
        
    for pair in byte_modifications:
        file_data[pair[0]] = pair[1]

    file_data = header + file_data
    with open(output_filename, 'wb') as f:
        f.write(file_data)

list = [(x, random.randint(0, 255)) for x in range(0, 100)]

modify_bytes("z1_enc_cbc.bmp", "z2_modified.bmp", list)