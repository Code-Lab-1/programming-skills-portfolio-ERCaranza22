# Exercise 1: Print String

song = "Twinkle, twinkle, little star. How I wonder what you are! Up above the world so high. Like a diamond in the sky. Twinkle, twinkle, little star. How I wonder what you are"
print(song)

# Exercise 2: Python Version

import sys
print (sys.version)

# Exercise 3: Date and Time

from datetime import date
today = date.today()

Date1 = today.strftime("%B %d, %Y")
print("Date1 =", Date1)

Date2 = today.strftime("%d/%m/%Y")
print("Date2 =", Date2)

Date3 = today.strftime("%b-%d-%Y")
print("Date3 =", Date3)

# Exercise 4: String Concatination

x = "Friendship "
y = "Is "
z = "Magic"

print(x + y + z)

# Exercise 5: Area of the Circle

PI = 3.14
r = float(input("Enter the radius of a circle:"))

area = PI * r * r
print("Area of a circle = %.2f" %area)