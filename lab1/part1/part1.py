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
              keys.append(format(keybyte, "#04x"))
    return keys

def possiblePlaintext(chlst, cllst):
    """
    """
    plaintext = []
    plaintextbyte = 0
    plaintextval = "a"
    for i, x in enumerate(chlst):
        for j, y in enumerate(cllst):
          plaintextbyte = (x[0] << 4) + y[0]
          plaintextval = chr(plaintextbyte)
          plaintext.append(plaintextval)
    return plaintext

def checkKeysPerLetter(prevKeyslst, checkKeyslst):
    """
    This method will keep the keys that exist in both lists
    """
    keys = list(set(prevKeyslst).intersection(checkKeyslst))

    return keys

def plaintext(mapping, ch, cl, kh, kl):
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

def test():
    frstByte = True
    maxPossKeys = []
    newPossKeys = []

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
        i = 0
        while True:
            byte = cipherfile.read(1)
            if not byte:
                break
            i += 1

            intbyte = ord(byte)

            ch = intbyte >> 4
            cl = intbyte & 15

            if i == 1:
                pchar = plaintext(mapping, ch, cl, 0x5, 0x0)
            elif i == 2:
                pchar = plaintext(mapping, ch, cl, 0x2, 0xf)  
            elif i == 3:
                pchar = plaintext(mapping, ch, cl, 0x0, 0x8)
            elif i == 4:
                pchar = plaintext(mapping, ch, cl, 0x7, 0xc)
            elif i == 5:
                pchar = plaintext(mapping, ch, cl, 0x5, 0xf)
            elif i == 6:
                pchar = plaintext(mapping, ch, cl, 0x3, 0x0)
            elif i == 7:
                pchar = plaintext(mapping, ch, cl, 0x0, 0x0)
                i = 0

            pfile.write(pchar)

    pfile.close()

    return

# add separation of key lengths  ( 7 different arrays )
def main():

    frstByte = True
    maxPossKeys = []
    newPossKeys = []

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
        #i = 1;
        while True:
        #while i == 1:
            #read first byte
            #print()
            if frstByte == True:
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)

            #read every 7th byte afterwards
            else:
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                byte = cipherfile.read(1)
                i = 0

            intbyte = ord(byte)

            ch = intbyte >> 4
            cl = intbyte & 15

            keys = findKeys(ch, cl)

            # cut out unneccesary ph values
            pPoss = findInDoubleMatrix(mapping, ch)
            kPoss = findInDoubleMatrix(mapping, cl)

            ##print()
            ##print(pPoss)
            ##print(kPoss)

            pClean = cleanArrayForPlaintext(pPoss)
            kClean = cleanArrayForKey(kPoss)

            ##print()
            ##print(pClean)
            ##print(kClean)

            possKeys = sorted(possibleKeys(kClean, pClean))
            possPlaintext = sorted(possiblePlaintext(pClean, kClean))

            #print("possKeys: ", possKeys)
            #print("possPlaintext: ", possPlaintext)
            #print(format(intbyte, '#04x'))

            if frstByte == True:
                maxPossKeys = possKeys
                frstByte = False
                print("poss keys: ", maxPossKeys)
            else:

                maxPossKeys = checkKeysPerLetter(maxPossKeys, possKeys)
      
                # possible keys for this byte
                print("poss keys: ", sorted(maxPossKeys))
                print("len: ", len(maxPossKeys))

                #print("ch =", format(ch, "#03x"))
                #print("cl =", format(cl, "#03x"))
                print(format(intbyte, '#04x')) #use this to print as 0x## where the ##
                # are any digit from 0-f

    pfile.close()

    return

if __name__ == "__main__":
    test()
