# Exercise 4: Large Shirts

def make_shirt(size='large', message='Haters gonna hate'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Nobody can drag me down')