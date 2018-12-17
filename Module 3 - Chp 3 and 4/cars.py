#sorting...but you can't revert back to the original order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print("Here is the list permanently sorted alphabetically:")
print(cars)

#reverse alphabetical order...again you can't revert back to original order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print("\nHere is the list permanently sorted in reverse alphabetical order")
print(cars)

#use the sorted function to display the list in a certain order, but not change the original order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the reverse sorted list:")
print(sorted(cars,reverse=True))
print("\nHere is the original list again:")
print(cars)

#use the reverse function to reverse order. It changes the list permanently, but you can reverse it again.
cars.reverse()
print("\nHere is the list in reverse order:")
print(cars)
cars.reverse()
print("\nHere is the list re-reversed:")
print(cars)
