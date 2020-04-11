class Car():
    def __init__(self, make, model, year):
        # Initialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0
        self.gasTank = 50

    def getDescripteveName(self):
        # return a neatly formatted descriptive name.
        longName = str(self.year) + " " + self.make + " " + self.model
        return longName.title()

    def readOdometer(self):
        # print a statement shownig the car's mileage.
        print("This car has " + str(self.odometerReading) + " miles on it.")

    def updateOdometer(self, mileage):
        # set odometer reading to the given value.
        # reject the change if it attempts to roll the odometer back.
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        # add the given amount to the odometer reading.
        self.odometerReading += miles

    def  fillGasTank(self):
        print (self.gasTank())
        

class ElectricCar(Car):
    # Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year): # initialize attributes of the parent class.
        super().__init__(make, model, year) # the super() make connection between parent and child class
        self.battery = Battery()

    def describeBattery(self):
        # print a statement describing the battery size.
        print("This car has a " + str(self.batterySize) + "-KWh battery.")

    # when I use the same name in the father and child class, then the child overrides the Method
    def fillGasTank(self): 
        print ("This car doesn't need a gas tank!")

class Battery():
    def __init__(self, batterySize=70):
        self.batterySize = batterySize

    def describeBattery(self):
        print("This car has a " + str(self.batterySize) + "-KWh battery.")

    def getRange(self):
        # print a statement about the range this battery provides.
        if self.batterySize == 70:
            range = 240
        elif self.batterySize == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

myTesla = ElectricCar("Tesla", "Model s", 2016)
print(myTesla.getDescripteveName())
myTesla.battery.describeBattery()
myTesla.battery.getRange()