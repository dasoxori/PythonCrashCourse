# using json.load()
# The JSON format was originally developed for javascript.
# However, it has since become a common format used by many languages.

import json

filename = 'textFiles/numbers.json'
with open(filename) as fObj:
    numbers = json.load(fObj)

print(numbers)