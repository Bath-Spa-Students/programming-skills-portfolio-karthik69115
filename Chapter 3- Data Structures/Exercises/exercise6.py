#Q.6 You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
guests = ['raj', 'rahul', 'rohit']

name = guests[0].title()
print(name + ", humble request to join dinner at my home.")

name = guests[1].title()
print(name + ", humble request to join dinner at my home.")

name = guests[2].title()
print(name + ", humble request to join dinner at my home.")

name = guests[2].title()
print("\nSorry, " + name + " won't be available for dinner.")

del(guests[2])
guests.insert(2, 'shaan')

name = guests[0].title()
print("\n" + name + ", humble request to join dinner at my home.")

name = guests[1].title()
print(name + ", humble request to join dinner at my home.")

name = guests[2].title()
print(name + ", humble request to join dinner at my home.")

print("\ni appolagise for the inconvience,as we can only invite just two people for the specified dinner.")

name = guests.pop()
print("i appolagise for the inconvience, " + name.title() + " at current situation there's no space to accomidate everyone at the table.")

name = guests.pop()
print("i appolagise for the inconvience, " + name.title() + " at current situation there's no space to accomidate everyone at the table.")

name = guests.pop()
print("i appolagise for the inconvience, " + name.title() + " at current situation there's no space to accomidate everyone at the table.")

name = guests.pop()
print("i appolagise for the inconvience, " + name.title() + " at current situation there's no space to accomidate everyone at the table.")

name = guests[0].title()
print(name + ", humble request to join dinner at my home.")
name = guests[1].title()
print(name + ", humble request to join dinner at my home.")

del(guests[0])
del(guests[1])

print(guests)
