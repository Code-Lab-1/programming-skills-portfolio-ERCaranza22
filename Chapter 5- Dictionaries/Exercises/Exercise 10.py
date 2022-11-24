

pet = {'Animal type': 'Rabbit',
    'Name': 'Tewi',
    'Owner': 'Fargo',
    'Weight': 7,
    'Eats': 'Carrot',}
pet.append(pet)

pet = {'Animal type': 'Dog',
    'Name': 'Yuri',
    'Owner': 'Jean',
    'Weight': 32,
    'Eats': 'Steak',}
pet.append(pet)

for pet in pet:
    print(f"\nHere's what I know about {pet['Name']}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")