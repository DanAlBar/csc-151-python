guests = ['albert einstein', 'isaac newton', 'neil armstrong']

for guest in guests:
  message = f"Dear {guest.title()}, I would be honored if you would join me for dinner. Your company and insights would make for an enlightening and unforgettable evening of conversation."
  print(message)
 
print("I have actually found a table that will accommodate a few more guests for this evening!")

guests.insert(0, 'miura kentaro')
guests.insert(2, 'junji ito')
guests.append('vincent van gogh')
guests.sort()

for guest in guests:
  message = f"Dear {guest.title()}, I would be honored if you would join me for dinner. Your company and insights would make for an enlightening and unforgettable evening of conversation."
  print(message)





