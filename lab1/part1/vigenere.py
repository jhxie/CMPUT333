#!/usr/bin/env python3

"""
Encrypt or decrypt the variant of Vigenère cipher shown in part 1 of lab 1.
"""

# ------------------------------- MODULE INFO ---------------------------------
__all__ = []
# ------------------------------- MODULE INFO ---------------------------------

# --------------------------------- MODULES -----------------------------------
import argparse

from itertools import repeat
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


def vigenere_encrypt(clear_text_byte: int, key: int) -> int:
    """
    Encrypts the given 'clear_text_byte' with the 'key' specified using
    one variant of the Vigenère cipher.
    """
    if not all(isinstance(arg, int) for arg in locals().values()):
        raise TypeError("All arguments must be of 'int' type")

    if clear_text_byte not in range(1 << 8):
        raise ValueError("'clear_text_byte' must be in range [0, 1 << 8)")

    high_mask = 0b11110000
    low_mask = high_mask >> 4
    plain_high = (clear_text_byte & high_mask) >> 4
    plain_low = clear_text_byte & low_mask
    key_high = (key & high_mask) >> 4
    key_low = key & low_mask

    return (mapping[plain_high][key_low] << 4) | mapping[plain_low][key_high]


def vigenere_decrypt(cipher_text_byte: int, key: int) -> int:
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
                        type=int,
                        required=True,
                        help="key to encrypt/decrypt the Vigenère variant")
    args = parser.parse_args()

    # if args.decrypt:
    #     print("Decrypted output is " + args.decrypt)
    # elif args.encrypt:
    #     print("Encrypted output is " + args.encrypt)

    for byte in map(vigenere_encrypt, bytes_get(args.file), repeat(args.key)):
        print(byte)
    # List all the non-private attributes
    # for attr in filter(lambda attr: not attr.startswith("_"), dir(args)):
    #     if getattr(args, attr):
    #         print(getattr(args, attr))

if __name__ == "__main__":
    main()
# -------------------------------- FUNCTIONS ----------------------------------
