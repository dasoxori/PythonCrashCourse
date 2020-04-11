from collections import OrderedDict

favoriteLanguages = OrderedDict()

favoriteLanguages['jen'] = 'python'
favoriteLanguages['sarah'] = 'c'
favoriteLanguages['edward'] = 'ruby'
favoriteLanguages['phil'] = 'python'

for name, language in favoriteLanguages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")