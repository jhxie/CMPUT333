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
    This method will clean out so that only the ph will contain 2,3,4,5,6,7
    """
    array = []
    temp = []
    for i, x in enumerate(lst):
        if i == 2:
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
    This method will clean out so that only the kh will contain 0,1,2,3,4,5,6,7
    """
    array = []
    temp = []
    for i, x in enumerate(lst):
        if x[1] == 0:
            temp = [i, x[1]]
            array.append(temp)
        elif x[1] == 1:
            temp = [i, x[1]]
            array.append(temp)
        elif x[1] == 2:
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
          keybyte = (x[1] << 4) + y[1]
          keys.append(keybyte)
    return keys

def main():

    cipherfn = ''
    plainfn = ''

    if len(sys.argv) == 1:
        print("No cipherfile input added")
        sys.exit(2)
    elif len(sys.argv) == 2:
        print("No output file added")
        sys.exit(2)
    else:
        cipherfn = sys.argv[1]
        plainfn = sys.argv[2]

    pfile = open(plainfn, "w")

    with open(cipherfn, "rb") as cipherfile:
        byte = cipherfile.read(1)

        intbyte = ord(byte)

        ch = intbyte >> 4
        cl = intbyte & 15

        # cut out unneccesary ph values
        pPoss = findInDoubleMatrix(mapping, ch)
        kPoss = findInDoubleMatrix(mapping, cl)
        pClean = cleanArrayForPlaintext(pPoss)
        kClean = cleanArrayForKey(kPoss)

        # possible keys for this byte
        print("poss keys: ", possibleKeys(kClean, pClean))
        print("len: ", len(possibleKeys(kClean, pClean)))

        print("ch =", format(ch, "#03x"))
        print("cl =", format(cl, "#03x"))
        # print(format(intbyte, '#04x')) use this to print as 0x## where the ##
        # are any digit from 0-f

    pfile.close()

    return

if __name__ == "__main__":
    main()
