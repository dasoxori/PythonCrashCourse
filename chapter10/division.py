# Using Exceptions to Prevent Crashes

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    firstNumber = input("\nFirst Number: ")
    if firstNumber == 'q':
        break
    secondNumber = input("Second Number: ")
    try:
        answer = int(firstNumber) / int(secondNumber)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)
