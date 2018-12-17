"""A set of classes used to represent all users of a website."""

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

class Privileges():
    """Models the privileges assigned to an admin."""
    
    def __init__(self):
        """Initialize attributes."""
        self.privileges = ['can accept users', 'can ban users', 
                           'can shut down discussion boards']
    
    def show_privileges(self):
        """List the privileges of an admin."""
        print("\nThose who are admin have the following privileges:")
        for privilege in self.privileges:
            print(" -" + privilege)

class Admin(User):
    """Represents aspects of a user, specific to admin."""
    
    def __init__(self, first_name, last_name, username, age):
        """
        Initialize attributes from parent class.
        Then initialize attributes specific to admin.
        """
        super().__init__(first_name, last_name, username, age)
        self.privileges = Privileges()