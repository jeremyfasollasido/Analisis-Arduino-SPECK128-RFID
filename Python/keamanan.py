from speck import SpeckCipher  # Pastikan Anda menginstal library speck

# Ciphertext dan plaintext
data_ciphertext = bytes.fromhex("8951BC942AA270D53FC7D28859E8A983")
data_plaintext = bytes.fromhex("23EEAE0D000000000000000000000000")

# Brute force range (contoh: 24-bit key space untuk pengujian)
max_key = 2**24  # Anda dapat mengubah ukuran ini
found = False

for key in range(max_key):
    # Konversi key menjadi 16 byte (Speck membutuhkan 128-bit key)
    test_key = key.to_bytes(16, 'big')
    cipher = SpeckCipher(test_key, key_size=128, block_size=128)

    # Dekripsi ciphertext
    decrypted = cipher.decrypt(data_ciphertext)

    if decrypted == data_plaintext:
        print(f"Key ditemukan: {test_key.hex()}")
        found = True
        break

if not found:
    print("Key tidak ditemukan dalam range yang diuji.")
