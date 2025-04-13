favorite_places = {
    'danny': ['california', 'new york', 'mexico'],
    'anna': ['atlanta', 'dc'],
    'chris': ['south caroline', 'florida'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        if place == 'dc':
            print(f"\t{place.upper()}")
        else:
            print(f"\t{place.title()}")
