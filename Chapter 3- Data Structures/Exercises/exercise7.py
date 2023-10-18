#Q.7 Think of at least five places in the world you’d like to visit.
#•	 Store the locations in a list. Make sure the list is not in alphabetical order.
locations = ['denmark', 'newyork', 'iceland', 'netherland', 'punjab']

print("original order:")
print(locations)

print("\nalphabetical:")
print(sorted(locations))

print("\noriginal order:")
print(locations)

print("\nreverse alphabetical:")
print(sorted(locations, reverse=True))

print("\noriginal order:")
print(locations)

print("\nreversed:")
locations.reverse()
print(locations)

print("\noriginal order:")
locations.reverse()
print(locations)

print("\nalphabetical")
locations.sort()
print(locations)

print("\nreverse alphabetical")
locations.sort(reverse=True)
print(locations)