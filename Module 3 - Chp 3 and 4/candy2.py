#list
candy = ["candy corn", "twix", "m&ms", "skittles", "twizzlers"]

#print list
print("So, it's Halloween, and I've got candy on the brain:")
print(candy)

#append
candy.append("snickers")
candy.append("reese's peanut butter cups")
print("\nOops, I almost forgot my favorites...snickers and reese's! One more time:")
print(candy)

#sorted
print("\nNow, librarians need to sort things alphabetically:")
print(sorted(candy))
print("\nOr reverse alphabetically:")
print(sorted(candy,reverse=True))