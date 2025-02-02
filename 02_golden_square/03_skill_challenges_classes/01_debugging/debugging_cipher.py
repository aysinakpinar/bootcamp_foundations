def encode(text, key):
    cipher = make_cipher(key)
    print(f"This is cipher {cipher}")
    ciphertext_chars = []
    print("Iterating over text")
    for i in text:
        print(f"Letter {i}")
        print(f"index of letter {i} {cipher.index(i)}")
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)
    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    print (f"This is cipher = {cipher}")
    plaintext_chars = []
    print("Iterating over encrypted")
    for i in encrypted:
        print(f"letter in encrypted = {i}")
        print(f" ord(i) = {ord(i)}")
        plain_char = cipher[ord(i) - 65] "it was [65 - ord(i)} should be [ord(i) - 65]"
        print(f"Plain char = {plain_char}")
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(0, 26)] "it was [chr(i + 98) for i in range(1, 26)] should be [chr(i + 97) for i in range(0, 26)]  " 
    cipher_with_duplicates = list(key) + alphabet
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
