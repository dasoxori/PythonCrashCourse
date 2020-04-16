# checking for special items

requestedToppins = ['mushrooms', 'green peppers', 'extra cheese']

for requestedToppin in requestedToppins:
    if requestedToppin == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requestedToppin + ".")

print("\nFinished making your pizza")

# cheching that a list is NOT empty
print("\nChecking if the list was empty first")
requestedToppins = []

if requestedToppins:
    for requestedToppin in requestedToppins:
        print("Adding " + requestedToppin + ".")
    print("\nFinished making your pizza")
else:
    print("Are you sure you want a plain pizza?")

#using multiple lists
print("\nIn this example we are using multiple lists")

availableToppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requestedToppins = ['mushrooms', 'fresh fries', 'extra cheese']

for requestedTopping in requestedToppins:
    if requestedTopping in availableToppings:
        print("Adding " + requestedTopping + ".")
    else:
        print("Sorry, we don't have " + requestedTopping + ".")

print("\nFinished making your pizza!")
        
