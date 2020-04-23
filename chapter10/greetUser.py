# Reading Users generated data

import json

def getStoredUsername():
    """Get stored username if available"""
    filename = 'textFiles/username.json'
    try:
        with open(filename) as fileObject:
            username = json.load(fileObject)
    except FileNotFoundError:
            return None
    else:
            return username

def getNewUsername():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = 'textFiles/username.json'
    with open(filename, 'w') as fileObject:
        json.dump(username, fileObject)
    return username

def greetUser():
    """Greet the user by name"""
    username = getStoredUsername()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = getNewUsername()
        print("We'll remember you when you come back, " + username + "!")


greetUser()