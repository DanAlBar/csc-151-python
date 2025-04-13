while True: 
  try:
      num1 = input("Enter the first number: ")
      num2 = input("Enter the second number: ")

      #Convert inputs to integers
      number1 = int(num1)
      number2 = int(num2)

      # Add and print the result
      result = number1 + number2
  except ValueError:
      print("Oops! You need to enter valid numbers only.")
  else:
      print(f"The sum is: {result}")

  retry = input("Would you like to try again? (y/n): ")
  if retry.lower() != 'y':
      print("Goodbye!")
      break
