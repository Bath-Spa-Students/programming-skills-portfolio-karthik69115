#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
sandwich_orders = [
    'pastrami', 'cabbage', 'layered cheese', 'pastrami',
    'chicken breast', 'tomato', 'pastrami']
finished_sandwiches = []
print("we're so sorry for the inconvience, pastrami is out of stock today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\n")
while sandwich_orders:
    recent_sandwich = sandwich_orders.pop()
    print("I am preparing your " + recent_sandwich + " sandwich.")
    finished_sandwiches.append(recent_sandwich)
    print("\n")
for sandwich in finished_sandwiches:
    print("I have made a " + sandwich + " sandwich.")