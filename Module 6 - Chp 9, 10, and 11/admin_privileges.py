"""A set of classes used to represent admin users of a website."""

from users import User

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