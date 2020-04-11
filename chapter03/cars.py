cars = ['bmw', 'audi', 'toyota', 'subaru', 'honda']

# sort list permanently
cars.sort()
print(cars)

# sort list permanently in reverse
cars.sort(reverse=True)
print(cars)

# sort list Temporarily
car = ['bmw', 'audi', 'toyota', 'subaru', 'honda']
print("\nHere is the original list:")
print(car)

print("\nHere is the sorted list:")
print(sorted(car))

print("\nHere is the original list again:")
print(car)

# printing a list in reverse order.
car.reverse()
print(car)

# finding the length of a list
print(len(car))