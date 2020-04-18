# Filling a Dictionary with user input

responses = {}

# Set a flag to indicate that polling is active.
pollingActive = True

while pollingActive:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Whitch mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anuone else is going to take the poll.
    repeat  = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        pollingActive = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(str(name.title()) + " would like to climb " + str(response.title()) + ".")