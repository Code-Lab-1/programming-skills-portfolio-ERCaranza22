# Exercise 1: Message

def display_message():
    """Display a message about what I'm learning."""
    msg = "I'm learning to store code in functions."
    print(msg)

display_message()

# Exercise 2: Favorite Book

def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(f"{title} is one of my favorite manga.")

favorite_book('The Abstract Wild')

# Exercise 3: T-Shirt

def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt('large', 'Silver Lining')
make_shirt(message="This is All For You", size='medium')

# Exercise 4: Large Shirts

def make_shirt(size='large', message='Haters gonna hate'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Nobody can drag me down')

# Exercise 5: Cities

def describe_city(city, country='Ireland'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Dublin')
describe_city('Reykjavik', 'Iceland')
describe_city('Mullingar')
