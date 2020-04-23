# using json.dump() & json.load()
# The JSON format was originally developed for javascript.
# However, it has since become a common format used by many languages.

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'textFiles/numbers.json'
with open(filename, 'w') as fileObject:
    json.dump(numbers, fileObject)