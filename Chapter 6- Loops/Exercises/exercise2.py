#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free
# If the user enters an age, it converts the input to an integer and checks the age to determine the ticket cost.
# - If the age is less than 3, it prints that the person is allowed to enter for free.
# - If the age is between 3 and 12 (inclusive), it prints that the ticket will cost $10.
# - For all other ages, it prints that the ticket will cost $15.
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
