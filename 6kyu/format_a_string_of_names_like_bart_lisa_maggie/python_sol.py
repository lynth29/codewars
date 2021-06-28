"""
Given: an array containing hashes of names
Ex: [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]

Return: a string formatted as a list of names separated by commas
except for the last two names, which should be separated by an ampersand.

"""


def namelist(names):
    # for loop to return name from dictionary to a list
    namelist = [name['name'] for name in names]
    result = ' '
    # If there is only one name
    if len(namelist) <= 1:
        return result.join(namelist)
    else:
        # The last two names are separated by &
        lastTwo = ' & '.join(namelist[-2:])
        # Other names are separated by commas
        normal = [i + ',' for i in namelist[:-2]]
        normal.append(lastTwo)
        return result.join(normal)
