def make_shirt(shirtsize='large', textmessage='I love Python!'):
    print("\nI'm making a "+shirtsize+" t-shirt.")
    print('It will display, "'+textmessage+'"')
make_shirt()
make_shirt(shirtsize='extra large')
make_shirt('large', 'I love cars.')