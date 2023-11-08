#if-elif-else
# If 'age' is less than 2, the person is categorized as a baby.
# If 'age' is between 2 and 4, the person is categorized as a toddler.
# If 'age' is between 4 and 13, the person is categorized as a kid.
# If 'age' is between 13 and 20, the person is categorized as a teenager.
# If 'age' is between 20 and 65, the person is categorized as an adult.
# For any other age, the person is categorized as an elderly person.
age=18
if age<2:
    print("You are a baby!")
elif age<4:
    print("You are a toddler!")
elif age<13:
    print("You are a kid!")
elif age<20:
    print("You are a teenager!")
elif age<65:
    print("You are a adult!")
else:
    print("You are a elderly person!")
