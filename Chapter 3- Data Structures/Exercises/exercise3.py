#Q.3 Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
# Define a list called 'names' containing two elements, 'cars' and 'bikes'.
names = ['cars', 'bikes']
# Print the entire list 'names'.
print(names)
# Define a message 'msg' that mentions your favorite modes of transportation and prints it.
msg = "my favorite mode of transportation is cars and bikes"
print(msg)
# Access and print each element of the 'names' list individually.
print(names[0])
print(names[1])
# Reassign the list 'names' with the same values 'cars' and 'bikes'.
names = ['cars', 'bikes']
# Create a message 'msg' that mentions the preference for cars as a mode of transportation and prints it.
msg = "cars, it is the best mode of transportation as I love driving, " + names[0].title() + "!"
print(msg)
# Create a message 'msg' that mentions the preference for bikes as a mode of transportation and prints it.
msg = "bikes, it is the best mode of transportation as I love riding, " + names[1].title() + "!"
print(msg)
