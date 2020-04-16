# A simple dictionary

alien0 = {'color': 'green', 'points': 5}

print(alien0['color'])
print(alien0['points'])

newPoints = alien0['points']
print("You just earned " + str(newPoints) + " points!")

# Adding new key-value pairs
alien0['xPosition'] = 0
alien0['yPosition'] = 25
print("\n" + str(alien0))

# Starting with an Empty Dictionary
alien0 = {}

alien0['color'] = 'blue'
alien0['points'] = 10
print("\n" + str(alien0))

# Modifying Values in a Dictionary

alien0 = {'color': 'grey'}
print("The alien is " + alien0['color'] + ".")

alien0['color'] = 'yellow'
print("The alien is now " + alien0['color'] + ".")

# Tracking aliens position
print("\nLet's track aliens position")
alien0 = {'xPosition': 0, 'yPosition': 25, 'speed': 'fast'}
print("Original x-position: " + str(alien0['xPosition']))

# Let's move the alien to the right
# Determine how far to move the alien based on its current speed
if alien0['speed'] == 'slow':
    xIncrement = 1
elif alien0['speed'] == 'medium':
    xIncrement = 2
else:
    xIncrement = 3 # ok this alien is super fast

alien0['xPosition'] += xIncrement
print("New x-position " + str(alien0['xPosition']))

# removing Key-Value Pairs
print("\n")
alien0 = {'colore': 'green', 'points': 5}
print(alien0)

del alien0['points']
print(alien0)