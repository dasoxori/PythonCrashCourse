# tuples
# A tuple looks just like a list except you use parentheses instead of square breckets
# The value in a tuple cannot change. It's an immutable list

dimensions = (200, 50)
#dimensions[0] = 250 # This line proceed an error
print(dimensions[0])
print(dimensions[1])

# Looping through ALL values in a tuple
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
# Although we can't modify a tuple, we can assign a new value to a variable that holds a tuple.
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)