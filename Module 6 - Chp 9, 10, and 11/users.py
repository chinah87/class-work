"""A class used to represent general users of a website."""

class User():
    """A model of a user."""
    
    def __init__(self, first_name, last_name, username, age):
        """Initalize attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        """Print a summary of the user."""
        print("\n" + self.first_name + " " + self.last_name)
        print("- Username: " + self.username)
        print("- Age: " + str(self.age))
        
    def greet_user(self):
        """Print a personalized greeting."""
        print("\nWelcome back, " + self.username + "!")
    
    def increment_login_attempts(self):
        """Add login attempts by increments of 1."""
        self.login_attempts += 1
        print("You have logged in " + str(self.login_attempts) 
              + " times.")
    
    def reset_login_attempts(self):
        """Reset the login attempts back to 0."""
        self.login_attempts = 0
        print("Your login attempts have been reset back to " 
              + str(self.login_attempts) + ".")