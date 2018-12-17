#for loop to print individual names on the list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print("\n")

#doing multiple things in a loop
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")