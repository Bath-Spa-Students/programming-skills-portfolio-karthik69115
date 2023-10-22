#Q.3 Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
glossery={
    'dictionary': "it is a large collection of keyvalues in pairs.",
    'comment': 'it is the note in the program which the Python interpreter does not look after.',
    'string': 'it is a large series of characters variables.',
    'loop': 'it Works through a collection of items, one at a single time.',
    'list': 'it is a collection of items in a distinct order.',
    'key': 'it is termed as The first item in a keyvalues pair in a dictionary.',
    'value': 'it is a item associated with the key in an dictionary.',
    'conditional test': 'A conditional test is the comparison between two values.',
    'float': 'it is termed as a numerical value with an decimal component.',
    'boolean expression': 'it is an expression which evaluates weather the statement is True or False.',
    }
for word,definition in glossery.items():
    print("\n"+word.title() + ": " + definition)