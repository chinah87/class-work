cereals = ['cinnamon toast crunch', 'honeycomb', 'apple jacks', 
'honey nut cheerios']

print("If Amanda opened a cereal bar, she should include:")
for cereal in cereals:
    print(">> " + cereal.title())

print("\n")

suggestion = input("Suggest a cereal: ")
cereals.append(suggestion)

print("\n")

suggestion2 = input("Suggest another: ")
cereals.append(suggestion2)

print("\nAfter feedback, she will now include:")
for cereal in cereals:
    print(">> " + cereal.title())
