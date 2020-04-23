# saving and Reading User-Generated Data

import json
username = input("What is your name? ")
filename = 'textFiles/username.json'
with open(filename, 'w') as fObj:
    json.dump(username, fObj)
    print("We'll remember you when you come back, " + username + "!")