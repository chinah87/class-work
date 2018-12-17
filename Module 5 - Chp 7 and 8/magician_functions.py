def show_magicians(magicians):
    """Print a list of magicians."""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Modify magician names to add 'the Great'."""
    great_magicians = []
    
    while magicians:
        great_magician = "The Great " + magicians.pop()
        great_magicians.append(great_magician)
    
    for great_magician in great_magicians:
        magicians.append(great_magician)
    
    return magicians