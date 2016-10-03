#!/usr/bin/env python3

"""
File type detector for part 2 of lab 1.
"""

# ------------------------------- MODULE INFO ---------------------------------
__all__ = []
# ------------------------------- MODULE INFO ---------------------------------

# --------------------------------- MODULES -----------------------------------
import argparse
# --------------------------------- MODULES -----------------------------------

# ---------------------------- GLOBAL CONSTANTS -------------------------------
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
    "ps": (4, bytes([0x25, 0x21, 0x50, 0x53]))
}
# ---------------------------- GLOBAL CONSTANTS -------------------------------

# -------------------------------- FUNCTIONS ----------------------------------
def examineSignature(fileName: str) -> str or None:
    """
    Examines the header of 'fileName' and returns a corresponding
    file type 'str' based on the signature if the file type can be
    determined; otherwise returns 'None'.
    """
    resultFileType = None
    # No need to close the input file as it is closed
    # automatically at the end of the "with" block -- RAII in python.
    with open(fileName, "rb") as inputFile:
        for fileType, infoTuple in SIGNATURE_TABLE.items():
            bytesToExam, matchBytes = infoTuple
            header = inputFile.read(bytesToExam)
            if header == matchBytes:
                resultFileType = fileType
                break
            inputFile.seek(0)

    return resultFileType


def main():
    """
    Main command-line driver.
    """
    cliDescription = "Shows the File Extension Based on Signature"
    parser = argparse.ArgumentParser(description=cliDescription)

    parser.add_argument("files",
                        type=str,
                        nargs="+",
                        help="file(s) to be examined")
    args = parser.parse_args()

    if args.files:
        for fileToExam in args.files:
            result = examineSignature(fileToExam)
            formatDict = {
                "name": fileToExam,
                "type": result if result else "not known"
            }
            print("The file type of '{name}' is {type}".format(**formatDict))


if __name__ == "__main__":
    main()
# -------------------------------- FUNCTIONS ----------------------------------
