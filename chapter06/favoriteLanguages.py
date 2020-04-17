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