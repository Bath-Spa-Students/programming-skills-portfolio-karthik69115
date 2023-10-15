#Q.5 You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
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