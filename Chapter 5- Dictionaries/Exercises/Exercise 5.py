# Exercise 5: Pets
pets = []

pet = {'Animal type': 'Cat',
    'Name': 'Chauncey',
    'Owner': 'Cody',
    'Weight': 5,
    'Eats': 'Fish',}
pets.append(pet)

pet = {'Animal type': 'Rabbit',
    'Name': 'Tewi',
    'Owner': 'Fargo',
    'Weight': 7,
    'Eats': 'Carrot',}
pets.append(pet)

pet = {'Animal type': 'Dog',
    'Name': 'Yuri',
    'Owner': 'Jean',
    'Weight': 32,
    'Eats': 'Steak',}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['Name']}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")