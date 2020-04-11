# create a list and add elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change element in the list
motorcycles[0] = 'ducati'
print(motorcycles)

# insert new element in the end of the list
motorcycles.append('triumph')
print(motorcycles)

# insert new element at any position in the list
motorcycles.insert(0, 'BMW')
print(motorcycles)

# removing element from a specifi position in the list
del motorcycles[0]
print(motorcycles)

# removing the last element from the list and use it after it by put it in a variable
poppedMotorcycle = motorcycles.pop()
print(motorcycles)
print(poppedMotorcycle)

# removing (Poping) items from anywhere in the list.
firstOwned = motorcycles.pop(0)
print ("The first motorcycle I owned was a " + firstOwned.title() + ".")

# removing an item by Value
motorcycles.remove('yamaha')
print(motorcycles)