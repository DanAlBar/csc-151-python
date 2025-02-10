# dimensions.py
dimensions = (
    200, 50
    )
print(dimensions[0])
print(dimensions[1])

print("\nOriginal dimension:")
for dimension in dimensions:
    print(dimension)

dimensions = (
    400, 100
    )
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# magicians.py
magicians = [
    'alice', 'david', 'carolina'
    ]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

# animals.py
marsupials = [
    'kangaroo', 'koala', 'opossum'
    ]
for marsupial in marsupials:
    print(f"The {marsupial.title()}, is a mammal and a marsupial.")
print("All three of theses animals have pouches to carry their young!")

