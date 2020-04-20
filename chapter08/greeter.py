# defining a function

def greetUser(username):
    """Display a simple greeting.""" # docstring, descripes what the function does.
    print("Hello, " + username.title() + "!")

greetUser('jesse')



# Using a Function with a while loop
print("Using a Function with a while loop and break statement")

def getFormattedName(firstName, lastName):
    """Return a full name, neatly formatted."""
    fullName = firstName + " " + lastName
    return fullName.title()

# While loop with break statement
while True:
    print("\nPlease tell me your name:\n(enter 'q' at any time to quit)\n")
    firstName = input("First name: ")
    if firstName == 'q':
        break
    
    lastName = input("Last name: ")
    if lastName == 'q':
        break

    formattedName = getFormattedName(firstName, lastName)
    print("\nHello, " + formattedName)