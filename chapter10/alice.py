filename = 'textFiles/alice.txt'

try:
    with open(filename) as fileObject:
        contents = fileObject.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # count the approximate number of words in the file
    words = contents.split()
    numWords = len(words)
    print("The file " + filename + " has about " + str(numWords) + " words")