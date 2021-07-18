"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""
# First solution
def rot13(message):
    # Define dictionary
    ## Alphabet dict
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    cipher = ''
    for letter in message:
        if letter in alphabet.lower():
            num = (alphabet.lower().find(letter) + 13) % 26
            cipher += alphabet[num].lower()
        elif letter in alphabet:
            num = (alphabet.find(letter) + 13) % 26
            cipher += alphabet[num]
        else:
            cipher += letter
    return cipher

# Second solution
import string
def rot13(message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    cipher = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    result = message.translate(str.maketrans(alphabet, cipher))
    return result


# time consumed: 40 minutes
