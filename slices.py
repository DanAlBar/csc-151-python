# Chapter 03 MoreGuests_Sorted
guests = ['albert einstein', 'isaac newton', 'neil armstrong']

guests.insert(0, 'miura kentaro')
guests.insert(2, 'junji ito')
guests.append('vincent van gogh')
guests.sort()

# Chapter 04 Slices
slices = guests[:]

print("The first three items in this list are:")
for slice in slices[:3]:
  print(f"{slice.title()}")

print("\nThree items from the middle of the list are:")
for slice in slices[1:4]:
  print(slice.title())

print("\nThe last three items in the list are:")
for slice in slices[-3:]:
  print(slice.title())

