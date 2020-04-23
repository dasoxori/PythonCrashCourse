# Reading an Entire File

# the with opens and close file when it's necesery
filePath = 'textFiles/piDigits.txt'
with open(filePath) as fileObject:
    contents = fileObject.read()
print(contents.rstrip()) #remove the new line

# Reading line by line
print("\nReading file line by line")
with open(filePath) as fileObject:
    for line in fileObject:
        print(line.rstrip())


# Making a list of Lines from a File
print("\nMaking a list of Lines from a file in order to use it" +
        " outside the with block.")
with open(filePath) as fileObject:
    lines = fileObject.readlines()

for line in lines:
    print(line.rstrip())
    