def describe_city(city, country="Iceland"):
    """Prints a message stating which country the city is in."""
    print(f"{city} is in {country}.")

# Calling the function with the default country
describe_city("Reykjavik")

# Calling the function with specified countries
describe_city("Paris", "France")
describe_city("Tokyo", "Japan")
