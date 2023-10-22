pets = []
pet={
    'animaltype': 'black snapper',
    'name': 'dragon',
    'owner': 'raj',
    'weight': 46,
    'eats': 'bees',
}
pets.append(pet)

pet={
    'animal type': 'quwails',
    'name': 'clara',
    'owner': 'shaan',
    'weight': 1,
    'eats': 'seeds',
}
pets.append(pet)
pet={
    'animal type': 'dog',
    'name': 'rocky',
    'owner': 'eyan',
    'weight': 37,
    'eats': 'sausages',
}
pets.append(pet)
for pet in pets:
    print("\nThis is what I know all about" + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))