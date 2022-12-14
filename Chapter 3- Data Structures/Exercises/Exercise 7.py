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
