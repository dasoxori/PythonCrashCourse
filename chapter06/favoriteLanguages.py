# A dictionary of similar Objects

favoriteLanguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
    favoriteLanguages['sarah'].title() +
    ".\n")

# looping through all key-value pairs.
for name, language in favoriteLanguages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print()
# Looping only through all the keys in a Dictionary
# .keys() method returns only the keys from a dictionary
for name in favoriteLanguages.keys():
    print(name.title())


#Compare dictionarie with list.
print()
friends = ['phil', 'sarah']
for name in favoriteLanguages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
            ", I see your favorite language is " +
            favoriteLanguages[name].title() + "!")


# .keys() method isn't just for looping,
# it actually returns a list of all the keys.

if 'erin' not in favoriteLanguages.keys():
    print("Erin, please take our poll!")

# Looping Through a Dictionary's Keys in Order
print("\nLooping Through a Dictionary's Keys in Order")
for name in sorted(favoriteLanguages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping Through All values in a Dictionary
# .values() method returns only the values from a dictionary
# .set take care that duplicate items shows only once.
print("\nLooping Through All values in a Dictionary")
print("The follow languages have been mentioned")
for language in set(favoriteLanguages.values()):
    print(language.title())