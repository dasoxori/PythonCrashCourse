# Returning a simple value

# I give the middleName argument an empty default value in order
# to make it optional. So if the user pass a middleName is going to
# store it, if not then the function is going to pass the space
# without crashing.
def getFormattedName(firstName, lastName, middleName = ""):
    """Return a full name, neatly formateed"""
    if middleName:
        fullName = firstName + ' ' + middleName + ' ' + lastName
    else:
        fullName = firstName + ' ' + lastName
    return fullName.title()

musician = getFormattedName("jimi", "hendrix") 
print(musician)

musician = getFormattedName("john", "hooker", "lee") 
print(musician)