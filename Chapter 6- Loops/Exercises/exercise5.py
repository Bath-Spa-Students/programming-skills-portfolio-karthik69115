#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
# Define a list of 'sandwich_orders' that contains various sandwich types, including 'pastrami'.
sandwich_orders = [
    'pastrami', 'cabbage', 'layered cheese', 'pastrami',
    'chicken breast', 'tomato', 'pastrami']
    # Create an empty list to store finished sandwiches.
finished_sandwiches = []
# Notify customers that "pastrami" is temporarily out of stock.
print("We're sorry for the inconvenience, pastrami is out of stock today.")
# Use a 'while' loop to remove all instances of 'pastrami' from 'sandwich_orders'.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
# Print a newline to separate the notification from the preparation process.
print("\n")
# Process the remaining sandwich orders using a 'while' loop.
while sandwich_orders:
    recent_sandwich = sandwich_orders.pop()
    print("I am preparing your " + recent_sandwich + " sandwich.")
    finished_sandwiches.append(recent_sandwich)
    print("\n")
# Print messages for each completed sandwich.
for sandwich in finished_sandwiches:
    print("I have made a " + sandwich + " sandwich.")
