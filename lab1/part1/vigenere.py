#!/usr/bin/env python3

"""
Encrypt or decrypt the variant of Vigenère cipher shown in part 1 of lab 1.
"""

# ------------------------------- MODULE INFO ---------------------------------
__all__ = []
# ------------------------------- MODULE INFO ---------------------------------

# --------------------------------- MODULES -----------------------------------
import argparse

from itertools import cycle
# --------------------------------- MODULES -----------------------------------

# ---------------------------- GLOBAL CONSTANTS -------------------------------
# Match mapping indexes to fit the range for platintext and key characters
mapping = (
    (0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe),
    (0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0),
    (0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7),
    (0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa),
    (0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4),
    (0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3),
    (0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1),
    (0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf),
    (0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2),
    (0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5),
    (0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb),
    (0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6),
    (0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8),
    (0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9),
    (0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd),
    (0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc)
)
# ---------------------------- GLOBAL CONSTANTS -------------------------------

# -------------------------------- FUNCTIONS ----------------------------------


def vigenere_encrypt(output_file_name: str, input_file_name: str, key: str):
    """
    Encrypts the file with 'input_file_name' with the given full 'key' and
    writes the output to file with 'output_file_name'.
    """
    with open(output_file_name, "wb") as output_file:
        for byte in map(_byte_encrypt, bytes_get(input_file_name), cycle(key)):
            output_file.write(byte)


def vigenere_decrypt(output_file_name: str, input_file_name: str, key: str):
    pass


def _byte_encrypt(clear_text_byte: int, subkey: str) -> bytes:
    """
    Encrypts the given 'clear_text_byte' with the 'subkey' specified using
    one variant of the Vigenère cipher.

    NOTE: The 'subkey' is a single character of the whole Vigenère key;
    for example, 'h' is the first subkey of the key 'hello'.
    It is the caller's responsibility to pass the correct 'subkey' for a given
    'clear_text_byte' and ensures the "wrap-around" behavior of 'subkey'.
    """
    # if not all(isinstance(arg, int) for arg in locals().values()):
    #     raise TypeError("'clear_text_byte' must be of 'int' type")
    if not isinstance(clear_text_byte, int):
        raise TypeError("'clear_text_byte' must be of 'int' type")

    if clear_text_byte not in range(1 << 8):
        raise ValueError("'clear_text_byte' must be in range [0, 1 << 8)")

    if not isinstance(subkey, str):
        raise TypeError("'subkey' must be of 'str' type")

    if 1 != len(subkey):
        raise ValueError("'subkey' must be a single character 'str' type")

    subkey_value = ord(subkey)
    high_mask = 0b11110000
    low_mask = high_mask >> 4
    plain_high = (clear_text_byte & high_mask) >> 4
    plain_low = clear_text_byte & low_mask
    subkey_high = (subkey_value & high_mask) >> 4
    subkey_low = subkey_value & low_mask
    cipher_high = mapping[plain_high][subkey_low] << 4
    cipher_low = mapping[plain_low][subkey_high]
    # To convert an 'int' to a 'bytes' object properly in python 3,
    # use the call pattern of bytes([0x9a])
    cipher_byte = bytes([cipher_high | cipher_low])

    return cipher_byte


def _byte_decrypt(cipher_text_byte: int, subkey: str) -> bytes:
    pass


def bytes_get(file_name: str) -> int:
    """
    Returns a generator that gets one byte of the given 'file_name'
    at a time.
    """
    if not isinstance(file_name, str):
        raise TypeError("'file_name' argument must be of 'str' type")

    with open(file_name, "rb") as input_file:
        while True:
            # Read a single byte at a time
            byte = input_file.read(1)
            if not byte:
                break
            yield int(byte.hex(), base=16)
            # print("{0:#x}".format(byte[0]))


def main():
    """
    """
    cli_description = "Encrypt/decrypt a file with the Vigenère cipher"
    parser = argparse.ArgumentParser(description=cli_description)
    group = parser.add_mutually_exclusive_group()

    parser.add_argument("file",
                        type=str,
                        nargs="?",
                        help="file to be encrypted/decrypted")
    group.add_argument("-d",
                       "--decrypt",
                       type=str,
                       required=False,
                       help="file name of the decrypted output")
    group.add_argument("-e",
                       "--encrypt",
                       type=str,
                       required=False,
                       help="file name of the encrypted output")
    parser.add_argument("-k",
                        "--key",
                        type=str,
                        required=True,
                        help="key to encrypt/decrypt the Vigenère variant")
    args = parser.parse_args()

    if args.decrypt:
        print("Decrypted output is " + args.decrypt)
    elif args.encrypt:
        print("Encrypted output is " + args.encrypt)
        vigenere_encrypt(args.encrypt, args.file, args.key)

    # List all the non-private attributes
    # for attr in filter(lambda attr: not attr.startswith("_"), dir(args)):
    #     if getattr(args, attr):
    #         print(getattr(args, attr))

if __name__ == "__main__":
    main()
# -------------------------------- FUNCTIONS ----------------------------------
