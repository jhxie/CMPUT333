#!/usr/bin/env python3

"""
NOTE: This module is mostly based on 'freqAnalysis' module.
"""

# ------------------------------- MODULE INFO ---------------------------------
__all__ = ["letter_frequency_get", "frequency_order_get", "match_score_find"]
# ------------------------------- MODULE INFO ---------------------------------

# --------------------------------- MODULES -----------------------------------
from collections import OrderedDict
from string import ascii_uppercase
# --------------------------------- MODULES -----------------------------------

# ---------------------------- GLOBAL CONSTANTS -------------------------------
# Unused -- for reference only.
# The frequency is denoted in percentage and rounded up.
LETTER_FREQUENCY = (
    ("E", 12.70),
    ("T", 9.06),
    ("A", 8.17),
    ("O", 7.51),
    ("I", 6.97),
    ("N", 6.75),
    ("S", 6.33),
    ("H", 6.09),
    ("R", 5.99),
    ("D", 4.25),
    ("L", 4.03),
    ("C", 2.78),
    ("U", 2.76),
    ("M", 2.41),
    ("W", 2.36),
    ("F", 2.23),
    ("G", 2.02),
    ("Y", 1.97),
    ("P", 1.93),
    ("B", 1.49),
    ("V", 0.98),
    ("K", 0.77),
    ("J", 0.15),
    ("X", 0.15),
    ("Q", 0.10),
    ("Z", 0.07)
)
FREQUENCY_TABLE = OrderedDict(LETTER_FREQUENCY)
ETAOIN = "".join(FREQUENCY_TABLE.keys())
LETTERS = ascii_uppercase
# ---------------------------- GLOBAL CONSTANTS -------------------------------


# -------------------------------- FUNCTIONS ----------------------------------
def letter_frequency_get(message: str) -> dict:
    """
    Returns a dictionary with keys of single letters and values of the count
    of how many times they appear in the message parameter.
    """
    letter_frequency = dict.fromkeys(ascii_uppercase, 0)

    for letter in message:
        if letter.upper() in LETTERS:
            letter_frequency[letter.upper()] += 1

    return letter_frequency


def frequency_order_get(message: str) -> str:
    """
    Returns a string of the alphabet letters arranged in order of most
    frequently occurring in the message parameter.
    """
    # 1. Get a dictionary of each letter and its frequency count
    # {'E': 40, 'M': 0, 'Z': 0}
    letter_to_frequency = letter_frequency_get(message)

    # 2. Make a dictionary of each frequency count to each letters
    # with that frequency
    # {0: ['Z', 'M'], 40: ['E']}
    frequency_to_letter = {}
    for letter in LETTERS:
        if letter_to_frequency[letter] not in frequency_to_letter:
            frequency_to_letter[letter_to_frequency[letter]] = [letter]
        else:
            frequency_to_letter[letter_to_frequency[letter]].append(letter)

    # 3. Put each list of letters in reverse "ETAOIN" order,
    # and then convert it to a string
    for frequency in frequency_to_letter:
        frequency_to_letter[frequency].sort(key=ETAOIN.find, reverse=True)
        frequency_to_letter[frequency] = "".join(frequency_to_letter[frequency])

    # 4. Convert the 'frequency_to_letter' dictionary to a list of
    # tuple pairs (key, value), then sort them
    frequency_pairs = list(frequency_to_letter.items())
    frequency_pairs.sort(key=lambda x: x[0], reverse=True)

    # 5. Extract all the letters for the final string
    frequency_order = [pair[1] for pair in frequency_pairs]

    return "".join(frequency_order)


def match_score_find(message: str) -> int:
    """
    Returns the number of matches that the string in the message parameter
    has when its letter frequency is compared to English letter frequency.

    A "match" is how many of its 6 most frequent and 6 least frequent letters
    is among the 6 most frequent and 6 least frequent letters for English.
    """
    frequency_order = frequency_order_get(message)
    match_score = 0

    # Find how many matches for the 6 most common letters there are
    for common_letter in ETAOIN[:6]:
        if common_letter in frequency_order[:6]:
            match_score += 1

    # Find how many matches for the 6 least common letters there are
    for uncommon_letter in ETAOIN[-6:]:
        if uncommon_letter in frequency_order[-6:]:
            match_score += 1

    return match_score


if __name__ == "__main__":
    pass
# -------------------------------- FUNCTIONS ----------------------------------
