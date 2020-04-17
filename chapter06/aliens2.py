# Nesting Dictionaries
# Creating Dictionaries and List them

alien00 ={'color': 'green', 'points': 5}
alien01 ={'color': 'yellow', 'points': 10}
alien02 ={'color': 'red', 'points': 15}

aliens = [alien00, alien01, alien02]

for alien in aliens:
    print(alien)

# Lets make it more realistic and create code which automatically
# generates and creates 30 aliens through range()

# first we create an empty list for storing aliens.
aliens = []
print("\nMake 30 green aliens, modifing the first three of them" +
    ", showing the first five and printing the total number")
# Make 30 green aliens.
for alienNumber in range(30):
    newAlien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(newAlien)

# Change the color from the first three aliens.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
