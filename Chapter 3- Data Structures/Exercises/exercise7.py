#Q.7 Think of at least five places in the world you’d like to visit.
#•	 Store the locations in a list. Make sure the list is not in alphabetical order.
# Define a list 'locations' with several place names.
locations = ['denmark', 'newyork', 'iceland', 'netherland', 'punjab']
# Print the original order of the list.
print("original order:")
print(locations)
# Print the list in alphabetical order without modifying the original list.
print("\nalphabetical:")
print(sorted(locations))
# Print the original order to confirm that the original list remains unchanged.
print("\noriginal order:")
print(locations)
# Print the list in reverse alphabetical order without modifying the original list.
print("\nreverse alphabetical:")
print(sorted(locations, reverse=True))
# Print the original order again to confirm that the original list remains unchanged.
print("\noriginal order:")
print(locations)
# Reverse the order of elements in the 'locations' list in-place and print the result.
print("\nreversed:")
locations.reverse()
print(locations)
# Print the original order again.
locations.reverse()
print("\noriginal order:")
print(locations)
# Sort the 'locations' list in alphabetical order in-place and print the result.
print("\nalphabetical:")
locations.sort()
print(locations)
# Sort the 'locations' list in reverse alphabetical order in-place and print the result.
print("\nreverse alphabetical:")
locations.sort(reverse=True)
print(locations)
