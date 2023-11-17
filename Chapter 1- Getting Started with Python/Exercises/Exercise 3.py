# Exercise 3: Date and Time

from datetime import date
today = date.today()

Date = today.strftime("%B %d, %Y")
print("Date =", Date)
