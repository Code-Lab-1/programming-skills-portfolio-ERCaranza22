# Exercise 1: Names

name = ["Evan", "Tyler", "David", "Brian", "Marcel", "Scott"]
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# Exercise 2: Greetings

name = ["Paige", "Andrew", "Damian", "Kimberly", "Knox", "Ryder"]

greet = f"Hello {name[0].title()}! How are you?"
print(greet)

greet = f"Hello {name[1].title()}! How are you?"
print(greet)

greet = f"Hello {name[2].title()}! How are you?"
print(greet)

greet = f"Hello {name[3].title()}! How are you?"
print(greet)

greet = f"Hello {name[4].title()}! How are you?"
print(greet)

greet = f"Hello {name[5].title()}! How are you?"
print(greet)

# Exercise 3: Your Own List

car = ["Toyota", "Nissan", "Honda", "Jaguar", "BMW"]
print(car)

fav_car = f"I want to buy the {car[0].title()} car."
print(fav_car)

fav_car = f"I want to buy the {car[1].title()} car."
print(fav_car)

fav_car = f"I want to buy the {car[2].title()} car."
print(fav_car)

fav_car = f"I want to buy the {car[3].title()} car."
print(fav_car)

fav_car = f"I want to buy the {car[4].title()} car"
print(fav_car)

# Exercise 4: Guest List

guest = ["Mika","Violet","Gavin"]
name = guest[0].title()
print(f"{name}, please come to dinner tonight at 7pm.")

name = guest[1].title()
print(f"{name}, please come to dinner tonight at 7pm.")

name = guest[2].title()
print(f"{name}, please come to dinner tonight at 7pm.")

# Exercise 5: Change Guest List

guest = ["Mika","Violet","Gavin"]
name = guest[0].title()
print(f"\nSorry, {name} can't make it tonight.")

del(guest[0])
guest.insert(0, 'Logan')
name = guest[0].title()
print(f"\n{name}, please come to dinner tonight at 7pm.")

name = guest[1].title()
print(f"{name}, please come to dinner tonight at 7pm.")

name = guest[2].title()
print(f"{name}, please come to dinner tonight at 7pm.")

# Exercise 6: Shrinking Guest List

guest = ["Logan","Violet","Gavin"]
guest.pop(2)
print(f"Sorry, {name.title()} there's no room at the table.")

name = guest[0].title()
print(f"{name}, please come to dinner tonight at 7pm.")

name = guest[1].title()
print(f"{name}, please come to dinner tonight at 7pm.")

# Exercise 7: Seeing the world

country = ['Japan', 'South Korea', 'United Kingdom', 'Canada', 'Hong Kong']

print("Original order:")
print(country)

print("\nAlphabetical:")
print(sorted(country))

print("\nOriginal order:")
print(country)

print("\nReverse alphabetical:")
print(sorted(country, reverse=True))

print("\nOriginal order:")
print(country)

print("\nReversed:")
country.reverse()
print(country)

print("\nOriginal order:")
country.reverse()
print(country)

print("\nAlphabetical")
country.sort()
print(country)

print("\nReverse alphabetical")
country.sort(reverse=True)
print(country)