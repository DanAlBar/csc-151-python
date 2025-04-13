# Define the User class
class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0  # New attribute to track login attempts

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")
        print(f"Occupation: {self.occupation.title()}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()}! Welcome back!")

    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0

# Create a user instance
user1 = User('sara', 'lee', 28, 'new york', 'graphic designer')

# Simulate login attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print current login attempts
print(f"\nLogin attempts: {user1.login_attempts}")

# Reset login attempts
user1.reset_login_attempts()

# Print login attempts after reset
print(f"Login attempts after reset: {user1.login_attempts}")
