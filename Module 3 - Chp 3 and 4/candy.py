#list
candy = ["candy corn", "starburst", "twix", "m&ms", "skittles", "twizzlers"]
print("So, it's Halloween, and I've got candy on the brain:")
print(candy)

#append
candy.append("snickers")
candy.append("reese's peanut butter cups")
print("\nOops, I almost forgot my favorites...Snickers and Reese's! One more time:")
print(candy)

#sorted, reverse, and sort
print("\nNow, librarians need to sort things alphabetically:")
print(sorted(candy))
print("\nOr reverse alphabetically:")
candy.reverse()
print(candy)
print("\n...Nah, I like it alphabetical. Let's make it permanent!")
candy.sort()
print(candy)

#insert and len
candy.insert(0, "almond joys")
print("\nI know not everyone is a fan of coconut, but I just have to include Almond Joys...")
print(candy)
number = len(candy)
print("\nThere are " + str(number) + " types of candy on this list. Call me a sweet tooth!")

#pop, remove, and del
print("\nUgh, the guilt is real. Gotta remove some of these...")
nah = candy.pop(4)
print("\n" + nah.title() + ", I don't love you THAT much.")
nah = candy.pop(7)
print(nah.title() + ", you neither.")
candy.remove("candy corn")
del candy[4]
print("Starburst and Candy Corn are out as well!")

#conclusion
print("\nOkay, okay, okay...here's my final list:")
print(candy)
print("\nIn the end, I guess I'm just a chocoholic!")

