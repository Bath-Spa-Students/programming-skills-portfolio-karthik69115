# Define a function called 'make_shirt' with two optional parameters, 'shirtsize' and 'textmessage'.
# The function's default values are set to 'large' for the shirt size and 'I love Python!' for the text message.
def make_shirt(shirtsize='large', textmessage='I love Python!'):
    print("\nI'm making a "+shirtsize+" t-shirt.")
    print('It will display, "'+textmessage+'"')
make_shirt()
make_shirt(shirtsize='extra large')
make_shirt('large', 'I love cars.')
