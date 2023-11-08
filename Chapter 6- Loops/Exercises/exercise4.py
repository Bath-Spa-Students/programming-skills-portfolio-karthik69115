# The 'sandwich_orders' list contains orders for different types of sandwiches, and the 'finished_sandwiches' list is initially empty.
# It uses a 'while' loop to process sandwich orders until the 'sandwich_orders' list is empty.
# Within the loop, it pops the most recent sandwich order, prepares it, appends it to the 'finished_sandwiches' list, and prints a message indicating that the sandwich is being prepared.
# After all orders are processed, it uses another 'for' loop to print a message for each finished sandwich.
sandwich_orders =['smashed potato', 'layered cheese', 'chicken breast', 'tomato']
finished_sandwiches=[]
while sandwich_orders:
    recent_sandwich=sandwich_orders.pop()
    print("I am preparing your " + recent_sandwich + " sandwich.")
    finished_sandwiches.append(recent_sandwich)
    print("\n")
for sandwich in finished_sandwiches:
    print("I have made a " + sandwich + " sandwich.")
