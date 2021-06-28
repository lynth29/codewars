"""
ATM machines allow 4 or 6 digit PIN codes
and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""


import re

def validate_pin(pin):
    # bool() is to return True or False
    # regex's fullmatch to search for validate string
    # \d is to search for integer only
    # {4} or {6} is the length of string
    # | equals to OR
    return bool(re.fullmatch("\d{4}|\d{6}",pin))
