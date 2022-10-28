# Exercise 5: Change Guest List

guest = ["Mika","Violet","Gavin"]
name = guest[0]
print(f"\nSorry, {name} can't make it tonight.")

del(guest[0])
guest.insert(0, 'Logan')
name = guest[0]
print(f"\n{name}, please come to dinner tonight at 7pm.")

name = guest[1]
print(f"{name}, please come to dinner tonight at 7pm.")

name = guest[2]
print(f"{name}, please come to dinner tonight at 7pm.")