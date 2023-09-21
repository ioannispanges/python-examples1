import random


def generate_secure_key(key_length):
    key = bytes([random.randint(0, 255) for _ in range(key_length)])
    return key


key_length = 16
secure_key = generate_secure_key(key_length)

print("Generate Secure Key:", secure_key.hex())
