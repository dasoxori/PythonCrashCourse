# Passing an unknow number of arguments in a function

# Mixing Positiona and Arbitraty Arguments

# The asterisk in the parametere name *toppings tells Python
# to make an empty tuple called toppings and pack whatever
# value it receives into this tuple.

def makePizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


makePizza(16, "pepperoni")
makePizza(12, "mushrooms", "green peppers", "extra cheese")