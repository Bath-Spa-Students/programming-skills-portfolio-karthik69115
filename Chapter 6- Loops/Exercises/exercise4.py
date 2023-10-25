sandwich_orders =['smashed potato', 'layered cheese', 'chicken breast', 'tomato']
finished_sandwiches=[]
while sandwich_orders:
    recent_sandwich=sandwich_orders.pop()
    print("I am preparing your " + recent_sandwich + " sandwich.")
    finished_sandwiches.append(recent_sandwich)
    print("\n")
for sandwich in finished_sandwiches:
    print("I have made a " + sandwich + " sandwich.")