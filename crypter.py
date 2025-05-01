import base64
import marshal
import os
import re
import zlib

from colorama import Fore, init
from cryptography.fernet import Fernet

init(autoreset=True)


def xor_encrypt(data, key):
    return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key) + 1)))


def fernet_encrypt(key, data):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(data.encode())


def encode_b64(data):
    return base64.b64encode(data).decode()


def extract_imports(code):
    imports = [
        "import sys",
        "import base64",
        "import zlib",
        "import marshal",
        "import ctypes",
        "from cryptography.fernet import Fernet",
    ]
    for line in code.split("\n"):
        if re.match(r"^(import|from) ", line.strip()):
            if line.strip() not in imports:
                imports.append(line.strip())
    return "\n".join(imports)


def obfuscate_code(code):
    extracted_imports = extract_imports(code)
    encryption_key = Fernet.generate_key()
    mask_key = os.urandom(len(encryption_key))
    masked_key = xor_encrypt(encryption_key, mask_key)
    encrypted_data = fernet_encrypt(encryption_key, code)
    encoded_data = encode_b64(encrypted_data)
    compressed_data = zlib.compress(encoded_data.encode())
    marshalled_data = marshal.dumps(compressed_data)
    final_data = encode_b64(marshalled_data)

    stub_code = f"""'''
  ██████╗ ██████╗ ███████╗███████╗███████╗
 ██╔═████╗██╔══██╗██╔════╝██╔════╝██╔════╝
 ██║██╔██║██████╔╝█████╗  █████╗  █████╗
 ████╔╝██║██╔══██╗██╔══╝  ██╔══╝  ██╔══╝
 ╚██████╔╝██████╔╝███████╗███████╗██║
  ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝      🥩
'''
{extracted_imports}

def xor_decrypt(data, key):
    return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key) + 1)))

mask_key = {list(mask_key)}
masked_key = {list(masked_key)}
decryption_key = xor_decrypt(bytes(masked_key), bytes(mask_key))
encrypted_data = base64.b64decode({repr(final_data)})
encrypted_data = marshal.loads(encrypted_data)
encrypted_data = zlib.decompress(encrypted_data)
encrypted_data = base64.b64decode(encrypted_data).decode()
cipher = Fernet(decryption_key)
decrypted_data = bytearray(cipher.decrypt(encrypted_data))
mem_code = memoryview(decrypted_data)
getattr(__import__("builtins"), "".join(map(chr, [101, 120, 101, 99])))(mem_code.tobytes())
ctypes.memset(ctypes.addressof(ctypes.c_char.from_buffer(decrypted_data)), 0, len(decrypted_data))
ctypes.memset(ctypes.addressof(ctypes.c_char.from_buffer(mem_code)), 0, len(mem_code))
del decrypted_data, mem_code
"""
    return stub_code
