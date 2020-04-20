from car import Car

myNewCar = Car('audi', 'a4', 2016)
print(myNewCar.getDescriptiveName())

myNewCar.odometerReading = 23
myNewCar.readOdometer()