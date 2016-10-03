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
#    "doc": (8, bytes([0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1])),
    # Zip File Format - zip, docx, xlsx, pptx
#    "docx": (8, bytes([0x50, 0x4B, 0x03, 0x04, 0x14, 0x00, 0x06, 0x00])),
    # PDF Document - pdf
#    "pdf": (4, bytes([0x25, 0x50, 0x44, 0x46])),
    # PostScript Document - ps
#    "ps": (8, bytes([0x25, 0x21, 0x50, 0x53, 0x2D, 0x41, 0x64, 0x6F])),
#    "png": (8, bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])),
#    "jpg": (4, bytes([0xFF, 0xD8, 0xFF, 0xDB])),
#    "E0": (4, bytes([0xFF, 0xD8, 0xFF, 0xE0])),
#    "E1": (4, bytes([0xFF, 0xD8, 0xFF, 0xE1])),
#    "E2": (4, bytes([0xFF, 0xD8, 0xFF, 0xE2])),
#    "E3": (4, bytes([0xFF, 0xD8, 0xFF, 0xE3])),
#    "E8": (4, bytes([0xFF, 0xD8, 0xFF, 0xE8])),
    "jpg": (11, bytes([0xFF, 0xD8, 0xFF, 0xE1, 0x00, 0x00, 0x45, 0x78, 0x69, 0x66, 0x00]))
}

KEY_TABLE = {}

# Key so far, bytes 4 and 5 aren't known yet.
#KEY_BYTES = bytes([0x35, 0x33, 0x2E, 0x35, 0x, 0x, 0x35, 0x36, 0x33, 0x4E, 0x2C])

# Largest amount of bytes to read based on the given signatures
MAX_BYTES_TO_READ = 11

# Key is any combination of printable and non-printable characters 0x00 to 0x7F
# Key Length is 7
#
# Key higher bit value must be 0,1,2,3,4,5,6 or 7
#
# Plaintext characters from ASCII hex values range from 0x20 to 0x7F
#
# Plaintext higher bit value must be 2,3,4,5,6 or 7
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

def findInDoubleMatrix(lst, val):
    """
    This method will find all occurences of val in a given lst provided that
    lst is a double matrix.
    We can use this method to find values from the mapping given above.
    """
    result = []
    temp = []
    for i, x in enumerate(lst):
        for j, y in enumerate(x):
            if y == val:
                temp = [i, j]
                result.append(temp)
    return result

def cleanArrayForPlaintext(lst):
    """
    This method will clean out so that only the ph will contain 0,1,2,3,4,5,6,7
    """
    array = []
    temp = []
    for i, x in enumerate(lst):
        if i == 0:
            temp = [i, x[1]]
            array.append(temp)
        elif i == 1:
            temp = [i, x[1]]
            array.append(temp)
        elif i == 2:
            temp = [i, x[1]]
            array.append(temp)
        elif i == 3:
            temp = [i, x[1]]
            array.append(temp)
        elif i == 4:
            temp = [i, x[1]]
            array.append(temp)
        elif i == 5:
            temp = [i, x[1]]
            array.append(temp)
        elif i == 6:
            temp = [i, x[1]]
            array.append(temp)
        elif i == 7:
            temp = [i, x[1]]
            array.append(temp)
    return array

def cleanArrayForKey(lst):
    """
    This method will clean out so that only the kh will contain 2,3,4,5,6,7
    """
    array = []
    temp = []
    for i, x in enumerate(lst):
        if x[1] == 2:
            temp = [i, x[1]]
            array.append(temp)
        elif x[1] == 3:
            temp = [i, x[1]]
            array.append(temp)
        elif x[1] == 4:
            temp = [i, x[1]]
            array.append(temp)
        elif x[1] == 5:
            temp = [i, x[1]]
            array.append(temp)
        elif x[1] == 6:
            temp = [i, x[1]]
            array.append(temp)
        elif x[1] == 7:
            temp = [i, x[1]]
            array.append(temp)
    return array

def possibleKeys(cllst, chlst):
    """
    This method checks the possible keys from the byte read using the mapping of cl and ch.
    cllst will contain the tuples of [pl][kh]
    chlst will contain the tuples of [ph][kl]
    """
    keys = []
    keybyte = 0
    for i, x in enumerate(cllst):
        for j, y in enumerate(chlst):
          if (x[0] != 10) and (y[0] == 0):
              continue
          else:
              keybyte = (x[1] << 4) + y[1]
              keys.append(keybyte)
    return keys

def checkKeysPerLetter(prevKeyslst, checkKeyslst):
    """
    This method will keep the keys that exist in both lists
    """
    keys = list(set(prevKeyslst).intersection(checkKeyslst))

    return keys

def plaintextByte(mapping, ch, cl, kh, kl):
    """
    This method converts a given ch and cl, into a ph and pl with using a kh and kl
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
    Given a known plaintext and known ciphertext bytes, find the key byte.
    """
    for i, x in enumerate(mapping):
        for j, y in enumerate(x):
            if (i == ph) and (mapping[ph][j] == ch):
                kl = j
            if (i == pl) and (mapping[pl][j] == cl):
                kh = j

    return ((kh << 4) + kl)

def checkFileHeader(cipherfile):
    """
    This method will check to see if it is possible to decrypt the start of the
    file into a known file header. Key is assumed to be at least as long as
    possible headers.
    """
    # Get the header of the file
    cFile = open(cipherfile, "rb")
    encHeader = cFile.read(MAX_BYTES_TO_READ)
    cFile.close()


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
            format(k, '02x')
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

    return keylst

def decrypt(fileType):
    """
    This method decrypts the second argument file using the keylst
    """
    print("Starting decryption...")
    frstByte = True
    maxPossKeys = []
    newPossKeys = []

    cipherfn = sys.argv[1]
    plainfn = sys.argv[2]

    keyLength, keyBytes = KEY_TABLE[fileType]

    pfile = open(plainfn, "w")

    with open(cipherfn, "rb") as cipherfile:
        i = 0
        while True:
            byte = cipherfile.read(1)
            if not byte:
                break

            pchar = "0"
            if i < keyLength:
                inbyte = ord(byte)
                ch = inbyte >> 4
                cl = inbyte & 15

                k = keyBytes[i]
                kh = k >> 4
                kl = k & 15
                pchar = str(chr(plaintextByte(mapping, ch, cl, kh, kl)))

            pfile.write(pchar)
            i += 1

            if i == 23:
                i = 0

    pfile.close()
    print("Decryption finished")

    return

def main():
    if len(sys.argv) == 1:
        print("No cipherfile input added")
        sys.exit(2)
    if len(sys.argv) == 2:
        print("No output file added")
        sys.exit(2)

    keylst = checkFileHeader(sys.argv[1])

    decrypt("jpg")
#    noKey = False
#    for i in range(keylength):
#        if not keylst[i]:
#            noKey = True
#    if not noKey:
#        print("Key found")
#        print("Key (int format)= ", keylst)
#        decrypt(keylst)
#    else:
#        print("Key not found")

    return

if __name__ == "__main__":
    main()
