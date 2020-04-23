# writing to an empty file

filename = 'textFiles/programming.txt'

# writing Multiple line in a new or existing file from the begining
with open(filename, 'w') as fileObject:
    fileObject.write("I love programming.\n")
    fileObject.write("I love creating new games\n")

# adding content to a file instead of writing over existing content
with open(filename, 'a') as fileObject:
    fileObject.write("I also love finding meaning in large datasets.\n")
    fileObject.write("I love creating apps that can run in a browser.\n")
