# working with a file contents

filePath = 'textFiles/piDigits.txt'

with open(filePath) as fileObject:
    lines = fileObject.readlines()

piString = ''
for line in lines:
    piString +=line.strip() # strip removes the blank spaces

print(piString)
print(len(piString))

# Large Files: One thousand Digits
filePath = 'textFiles/piMillionDigits.txt'

with open(filePath) as fileObject:
    lines = fileObject.readlines()

piString = ''
for line in lines:
    piString += line.strip()

print(piString[:52] + "...")
print(len(piString))
