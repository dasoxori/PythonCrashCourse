# working with multiple files
# using function

def countWords(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as fileObject:
            contents = fileObject.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        # we can use 'pass' in the except if we want to pass the error in silent.
    else:
        # count approximate number of words in the file.
        words = contents.split()
        numWords = len(words)
        print("The file " + filename + " has about " + str(numWords) + " words.")




filenames = ['textFiles/siddhartha.txt', 'textFiles/alice.txt', 
             'textFiles/mobyDick.txt', 'textFiles/littleWomen.txt']

for filename in filenames:
    countWords(filename)