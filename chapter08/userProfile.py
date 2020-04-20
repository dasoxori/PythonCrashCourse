# Using Arbitrary Keyword Arguments

def buildProfile(first, last, **userInfo):
    """Build a dictionary containing everything we know about user."""
    profile = {} # empty dictionary
    profile['firstName'] = first
    profile['lastName'] = last
    for key, value in userInfo.items():
        profile[key] = value
    return profile

userProfile = buildProfile("albert", "einstein",
                            location='princeton',
                            field='phisics')

print(userProfile)