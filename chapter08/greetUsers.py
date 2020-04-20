# Passing a list to function

def greetUsers(names):
    """Print a simple greeting to each user in the list."""
    for name in names: # we define greetUsers() so it expects a list of names
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margo']
greetUsers(usernames)