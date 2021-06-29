"""
A string is considered to be in title case if each word in the string is either
(a) capitalised (that is, only the first letter of the word is in upper case) or
(b) considered to be an exception and put entirely into lower case unless it is
the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional
list of exceptions (minor words). The list of minor words will be given as
a string with each word separated by a space. Your function should ignore
the case of the minor words string -- it should behave in the same way even
if the case of the minor word string is changed.
"""

def title_case(title, minor_words=''):
    title = title.title().split(' ')
    new = []
    new.append(title[0])
    for word in title[1:]:
        print(word, word.lower())
        if word.lower() not in minor_words.lower().split(' '):
            new.append(word)
        else:
            new.append(word.lower())
    return ' '.join(new)

# second solution
def title_case_second(title, minor_words=''):
    return ' '.join([word if word in minor_words.lower().split() else word.capitalize() for word in title.capitalize().split()])
