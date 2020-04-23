# Check if my birthday contained in Pi

filename = 'textFiles/piMillionDigits.txt'

# open file and read it by line
with open(filename) as fileObject:
    lines = fileObject.readlines()

# remove the blank spaces
piString = ''
for line in lines:
    piString += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in piString:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")