#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.
# The code provides a simple way to collect and acknowledge the user's choice of pizza toppings.
prompt="\nWhat kind topping do you wish to have on your pizza?"
prompt+="\nEnter 'quit' when you wish to stop:"
while True:
    besttopping=input(prompt)
    if besttopping!='quit':
        print("I will add" + besttopping + "to your pizza.")
    else:
        break
