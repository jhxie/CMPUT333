#!/usr/bin/env python3

import sys

# mapping used for Lab 1
# NOTE 'map' identifier is a builtin function of python3
mapping = [
    [0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe],
    [0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0],
    [0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7],
    [0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa],
    [0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4],
    [0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3],
    [0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1],
    [0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf],
    [0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2],
    [0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5],
    [0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb],
    [0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6],
    [0x9, 0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8],
    [0xd, 0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9],
    [0xc, 0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd],
    [0xe, 0xf, 0x7, 0x6, 0x4, 0x5, 0x1, 0x0, 0x2, 0x3, 0xb, 0xa, 0x8, 0x9, 0xd, 0xc]
]

# Dictionary with keys of file type extension and values of tuples
# in the format of:
# (number of bytes to read from the offset 0 of files, matching bytes pattern)
SIGNATURE_TABLE = {
    # Compound File Binary Format - doc, xls, ppt
    "doc": (8, bytes([0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1])),
    # Zip File Format - zip, docx, xlsx, pptx
    "docx": (2, bytes([0x50, 0x4B])),
    # PDF Document - pdf
    "pdf": (4, bytes([0x25, 0x50, 0x44, 0x46])),
    # PostScript Document - ps
    "ps": (4, bytes([0x25, 0x21, 0x50, 0x53])),
    # Bytes 4 and 5 are wildcards and could be anything
    "jpg": (11, bytes([0xFF, 0xD8, 0xFF, 0xE1, 0x00, 0x00, 0x45, 0x78, 0x69, 0x66, 0x00]))
}

# Largest amount of bytes to read based on the given signatures
MAX_BYTES_TO_READ = 11

# Used for storing possible keys for various file signatures in SIGNATURE_TABLE
KEY_TABLE = {}

# Key for ciphertext2
KEY_BYTES = bytes([0x35, 0x33, 0x2E, 0x35, 0x30, 0x33, 0x35, 0x36, 0x33, 0x4E, 0x2C, 0x2D, 0x31, 0x31, 0x33, 0x2E, 0x35, 0x32, 0x38, 0x38, 0x39, 0x34, 0x57])
KEY_LENGTH = 23

# Key is any combination of printable characters 0x20 to 0x7F
#
# Key higher bit value must be 2,3,4,5,6 or 7
#
# Plaintext characters from ASCII hex values range from 0x00 to 0x7F
#
# Plaintext higher bit value must be 0,1,2,3,4,5,6 or 7
#
# ph <- higher 4 bits of plaintext
# pl <- lower 4 bits of plaintext
#
# kh <- higher 4 bits of key
# kl <- lower 4 bits of key
#
# ch <- mapping[ph][kl]
# cl <- mapping[pl][kh]
# c <- 0x(ch)(cl)
#
#
# Match mapping indexes to fit the range for platintext and key characters

def plaintextByte(mapping, ch, cl, kh, kl):
    """
    This method converts a given ch and cl, into a ph and pl with using a kh and kl.
    Returns the plaintext byte.
    """
    for i, x in enumerate(mapping):
        for j, y in enumerate(x):
            if (j == kh) and (j == kl) and (mapping[i][kh] == cl) and (mapping[i][kl] == ch):
                pl = i
                ph = i
            elif (j == kh) and (mapping[i][kh] == cl):
                pl = i
            elif (j == kl) and (mapping[i][kl] == ch):
                ph = i

    return ((ph << 4) + pl)

def getKeyFromPlainAndCipher(mapping, ph, pl, ch, cl):
    """
    Given a known plaintext byte and known ciphertext byte, find the key byte.
    """
    for i, x in enumerate(mapping):
        for j, y in enumerate(x):
            if (i == ph) and (mapping[ph][j] == ch):
                kl = j
            if (i == pl) and (mapping[pl][j] == cl):
                kh = j

    return ((kh << 4) + kl)

def checkFileHeader():
    """
    This method will check all of the given file headers in SIGNATURE_TABLE and
    add to KEY_TABLE what the start of the key would have to be to decrypt to a
    certain header.
    """
    # Get the header of the file
    cFile = open(sys.argv[1], "rb")
    encHeader = cFile.read(MAX_BYTES_TO_READ)
    cFile.close()

    print("Checking against hard coded signatures...")

    for fileType, infoTuple in SIGNATURE_TABLE.items():
        keylst = []
        bytesToExam, matchBytes = infoTuple
        for i in range (bytesToExam):
            cByte = encHeader[i]
            ch = cByte >> 4
            cl = cByte & 15

            pByte = matchBytes[i]
            ph = pByte >> 4
            pl = pByte & 15

            k = getKeyFromPlainAndCipher(mapping, ph, pl, ch, cl)
            keylst.append(k)

        sys.stdout.write("{0}: ".format(fileType))
        first = True
        for byte in keylst:
            if first:
                sys.stdout.write("[{0}".format(format(byte, '02x')))
                first = False
            else:
                sys.stdout.write(", {0}".format(format(byte, '02x')))
        sys.stdout.write("]\n")
        KEY_TABLE[fileType] = (bytesToExam, keylst)

    print("All signatures checked!")

def decrypt():
    """
    This method decrypts the given ciphertext file using the hardcoded key.
    """
    print("Starting decryption with hardcoded key...")

    cipherfn = sys.argv[1]
    plainfn = sys.argv[2]

    pfile = open(plainfn, "wb")

    with open(cipherfn, "rb") as cipherfile:
        i = 0
        while True:
            byte = cipherfile.read(1)
            if not byte:
                break

            int_byte = ord(byte)
            ch = int_byte >> 4
            cl = int_byte & 15

            k = KEY_BYTES[i]
            kh = k >> 4
            kl = k & 15
            p = plaintextByte(mapping, ch, cl, kh, kl)

            pfile.write(bytes([p]))
            i += 1

            if i == KEY_LENGTH:
                i = 0

    pfile.close()
    print("Decryption finished!")

    return

def main():
    if len(sys.argv) == 1:
        print("No cipherfile input added")
        sys.exit(2)
    if len(sys.argv) == 2:
        print("No output file added")
        sys.exit(2)

    checkFileHeader()

    decrypt()

    return

if __name__ == "__main__":
    main()
