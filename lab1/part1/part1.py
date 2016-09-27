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
        elif i == 0:
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

def plaintext(mapping, ch, cl, kh, kl):
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

    txt = str(chr((ph << 4) + pl))
    return txt

def readFileForKey(keylength, cipherfile):
    """
    This method will find the key of a given encrypted file
    """
    keylst = []
    firstByte = True

    # opens the file or reading in binary mode
    cFile = open(cipherfile, "rb")

    i = 0
    byte = cFile.read(1)
    while byte:
        i += 1
        intbyte = ord(byte)

        ch = intbyte >> 4
        cl = intbyte & 15

        pPoss = findInDoubleMatrix(mapping, ch)
        kPoss = findInDoubleMatrix(mapping, cl)

        pClean = cleanArrayForPlaintext(pPoss)
        kClean = cleanArrayForKey(kPoss)

        possKeys = sorted(possibleKeys(kClean, pClean))

        if firstByte == True:
            keylst.append(possKeys)
        else:
            keylst[i-1] = checkKeysPerLetter(keylst[i-1], possKeys)

        #if not keylst[i-1]:
        #    print("No comparable keys in set")
        #    cFile.close()
        #    return keylst

        #reset key bins for finding key
        if (i == keylength):
            if (firstByte == True):
                firstByte = False
            i = 0

        byte = cFile.read(1)

    cFile.close()

    return keylst

def decrypt(keylst):
    """
    This method decrypts the second argument file using the keylst
    """
    print("Starting decryption...")
    frstByte = True
    maxPossKeys = []
    newPossKeys = []

    cipherfn = sys.argv[1]
    plainfn = sys.argv[2]

    pfile = open(plainfn, "w")

    with open(cipherfn, "rb") as cipherfile:
        i = 0
        while True:
            byte = cipherfile.read(1)
            if not byte:
                break
            i += 1

            intbyte = ord(byte)

            ch = intbyte >> 4
            cl = intbyte & 15

            k = keylst[i-1][0]
            kh = k >> 4
            kl = k & 15
            pchar = plaintext(mapping, ch, cl, kh, kl)

            pfile.write(pchar)
            if i == 7:
                i = 0

    pfile.close()
    print("Decryption finished")

    return

def main():
    if len(sys.argv) == 1:
        print("No cipherfile input added")
        sys.exit(2)
    elif len(sys.argv) == 2:
        print("No output file added")
        sys.exit(2)

    keylength = input("Please enter the Key Length: ")
    keylength = int(keylength)
    print("Finding Keys...")
    keylst = readFileForKey(keylength, sys.argv[1])

    noKey = False
    for i in range(keylength):
        if not keylst[i]:
            noKey = True
    if not noKey:
        print("Key found")
        print("Key (int format)= ", keylst)
        decrypt(keylst)
    else:
        print("Key not found")

    return

if __name__ == "__main__":
    main()
