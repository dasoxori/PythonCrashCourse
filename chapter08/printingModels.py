# Modifying a List in a Function

def printModels(unprintedDesigns, completedModels):
    """
    Simulate printing each design, until none are left.
    Move each design to completedModels after printing.
    """
    while unprintedDesigns:
        currentDesign = unprintedDesigns.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model " + currentDesign)
        completedModels.append(currentDesign)

def showCompletedModels(completedModels):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completedModel in completedModels:
        print(completedModel)

unprintedDesigns = ['iphone case', 'robot pendant', 'dodecahedron']
completedModels = []

# with the slice [:] we pass a copy of the list and not the original.
printModels(unprintedDesigns[:], completedModels)
showCompletedModels(completedModels)