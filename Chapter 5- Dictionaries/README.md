# Exercise 1: Person

person = {
    'first_name': 'Errol',
    'last_name': 'Caranza',
    'age': 19,
    'city': 'Dubai',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# Exercise 2: Glossary

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")

# Exercise 3: Glossary 2

glossary = {'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.','conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.','boolean expression': 'An expression that evaluates to True or False.',}

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")

# Exercise 4: Rivers

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")

# Exercise 5: Pets
pets = []

pet = {
    'Animal type': 'Cat',
    'Name': 'Chauncey',
    'Owner': 'Cody',
    'Weight': 36,
    'Eats': 'Fish',
}
pets.append(pet)

pet = {
    'Animal type': 'Rabbit',
    'Name': 'Tewi',
    'Owner': 'Fargo',
    'Weight': 28,
    'Eats': 'Carrot',
}
pets.append(pet)

pet = {
    'Animal type': 'Dog',
    'Name': 'Yuri',
    'Owner': 'Jean',
    'Weight': 37,
    'Eats': 'Steak',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")