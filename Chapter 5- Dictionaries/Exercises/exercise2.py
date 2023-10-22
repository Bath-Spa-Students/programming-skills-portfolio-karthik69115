#Q.2 A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
glossery={
    'dictionary': "it is a large collection of keyvalues in pairs.",
    'comment': 'it is the note in the program which the Python interpreter does not look after.',
    'string': 'it is a large series of characters variables.',
    'loop': 'it Works through a collection of items, one at a single time.',
    'list': 'it is a collection of items in a distinct order.',
    }
word = 'dictionary'
print("\n"+word.title() + ": " + glossery[word])

word = 'comment'
print("\n"+word.title() + ": " + glossery[word])

word = 'string'
print("\n"+word.title() + ": " + glossery[word])

word = 'loop'
print("\n"+word.title() + ": " + glossery[word])

word = 'list'
print("\n"+word.title() + ": " + glossery[word])