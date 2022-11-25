# Choose a Character

prompt = "\nWho do you want in your team?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  {topping} is now added to your team.")
    else:
        break