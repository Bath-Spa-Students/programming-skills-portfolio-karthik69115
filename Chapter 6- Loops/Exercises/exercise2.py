#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free
prompt="what is your age?"
prompt+="\nEnter 'quit' when you wish to stop."
while True:
    age=input(prompt)
    if age=='quit':
        break
    age=int(age)
    if age < 3:
        print("  You are allowed to enter for free!")
    elif age < 13:
        print("  Your ticket will coat $10.")
    else:
        print("  Your ticket will cost $15.")