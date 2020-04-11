# using the range function
for value in range(1, 6):
    print(value)

# using range to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

# skiping numbers in a given range "range(2, 11, 2)". We give the range from 2 to 11 and adds 2 in every step
evenNumbers = list(range(2, 11, 2))
print(evenNumbers)


# make a list of the square of each integer from 1 to 10
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# list comprehencions "The following example builds the same list of square numbers"

newSquares = [value**2 for value in range(1, 11)]
print(newSquares)