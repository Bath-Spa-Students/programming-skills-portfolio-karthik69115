#Q.2 Start with the list you used in Exercise 1, but instead of just
#printing each person’s name, print a message to them. The text of each message should be the same, but each message should be 
#personalized with the person’s name.
names = ['adil', 'alan', 'joy', 'shaan']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
names = ['adil', 'alan', 'joy', 'shaan']

msg = "hello adil,invitation for dinner at my home on 20 0ct, " + names[0].title() + "!"
print(msg)

msg = "hello alan,invitation for dinner at my home on 20 0ct, " + names[1].title() + "!"
print(msg)

msg = "hello joy,invitation for dinner at my home on 20 0ct, " + names[2].title() + "!"
print(msg)

msg = "hello shaan,invitation for dinner at my home on 20 0ct, " + names[3].title() + "!"
print(msg)