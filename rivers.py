rivers = {
    'nile': 'egypt',
    'rio grande': 'mexico',
    'shinano-gawa': 'japan',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.\n")

for river in rivers:
    print(river.title() + "\n")

for country in rivers.values():
    print(country.title() + "\n")
