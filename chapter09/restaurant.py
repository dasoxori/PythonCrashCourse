class Restaurant():
    def __init__(self, name, cuisineType):
        self.name = name
        self.type = cuisineType

    def describeRestaurant(self):
        print("\nThe name of the restaurant is: " + str(self.name.title()) + ".")
        print("The cuisine type of the restaurant is " + str(self.type.title() + "."))

    def openRestaurant(self):
        print("The restaurant is open")


goodys = Restaurant("Goody's", "Fast Food")

tavern = Restaurant("Mpampi's", "Local Cousine")

glamour = Restaurant("Cosi", "Master Chef")

goodys.describeRestaurant()
goodys.openRestaurant()

tavern.describeRestaurant()
glamour.describeRestaurant()