print(f"\nHello! Welcome to The Carolina.")
prompt = "\nTell me your age so I can figure out your ticket price: "
prompt += "\n(Enter 'quit' to end the program)"

total_price = 0

while True:
  age_input = input(prompt)

  if age_input.lower() == 'quit':
    break

  age = int(age_input)

  if age > 12:
    price = 15
  elif age >= 3:
    price = 10
  else:
    price = 0

  total_price += price
  print(f"You are {age} years old and your movie ticket will be ${price}")
  print(f"Current total ticket cost: ${total_price}\n")

print(f"Your total for all the tickets is: ${total_price}")  
