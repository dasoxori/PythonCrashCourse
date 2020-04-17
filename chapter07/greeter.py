# writing clear prompts

name = input("Please enter your name: ")
print("Hello, " + name.title() + "!\n")


# Longer prompt stored in a variable and then pass it to the input
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt +="\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name.title() + ".")