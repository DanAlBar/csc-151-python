import random

# Create a list of 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly choose 4 numbers
numbers = random.sample([item for item in lottery_pool if isinstance(item, int)], 4)

# Randomly choose 1 letter
letter = random.choice([item for item in lottery_pool if isinstance(item, str)])

# Combine into a lottery ticket
lottery_ticket = numbers + [letter]

# Sort both for easier comparison (optional)
lottery_ticket_sorted = sorted(lottery_ticket, key=str)

# Get user input for their ticket
print("\nEnter your lottery ticket:")
user_numbers = []

# Get 4 number inputs from the user
for i in range(1, 5):
    number = int(input(f"Enter number {i}: "))
    user_numbers.append(number)

# Get 1 letter input from the user
user_letter = input("Enter one letter: ").upper()

# Combine and sort user's ticket
user_ticket = user_numbers + [user_letter]
user_ticket_sorted = sorted(user_ticket, key=str)

# Print both tickets
print("\nLottery winning ticket:", lottery_ticket_sorted)
print("Your ticket:", user_ticket_sorted)

# Compare tickets
if user_ticket_sorted == lottery_ticket_sorted:
    print("🎉 Congratulations! You won the lottery!")
else:
    print("Sorry, you didn't win this time. Better luck next time!")
