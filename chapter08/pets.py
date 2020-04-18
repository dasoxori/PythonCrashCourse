# Positional Arguments

def describePet( petName, animalType='dog'): #we can set default value and the func use it if we don't pass one
    """Display information about a pet"""
    print("\nI have a " + animalType + ".")
    print("My " + animalType + "'s name is " + petName.title() + ".")

describePet(animalType = "hamster", petName = "harry") # we can connect the parameter with variables
describePet("willie")
describePet("fifi", "cat")