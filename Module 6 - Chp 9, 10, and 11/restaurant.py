"""A class that can be used to represent a restaurant."""

class Restaurant():
    """A simple model of a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine attributes."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Prints information about the restaurant."""
        print(self.name + " is a lovely restaurant that serves " +
             self.cuisine_type + ".")
    
    def open_restaurant(self):
        """Simulate opening a restaurant."""
        print(self.name + " is now open!")
    
    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number
    
    def increment_number_served(self, amount):
        """Add the given amount to the number of customers."""
        self.number_served += amount