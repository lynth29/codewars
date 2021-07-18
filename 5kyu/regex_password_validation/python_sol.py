"""
You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.

"""

regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"

# ^ matches the beginning of the string
# (?=.*[a-z]) matches at least one lowercase letter
# (?=.*[A-Z]) matches at least one uppercase letter
# (?=.*\d) matches at least one numeric letter
# [^\W_] not matches any non-word character or _
# {6,} match 6 or more
# $ end line
# time consumed: ~20 minutes
