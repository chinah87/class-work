places = ['thailand', 'rwanda', 'greece', 'spain', 'italy']

print("Here is the original list:")
print(places)

print("\nHere is the list in alphabetical order:")
print(sorted(places))

print("\nHere is the list in its original order:")
print(places)

print("\nHere is the list in reverse alphabetical order:")
print(sorted(places,reverse=True))

print("\nOne more time, in the original order again:")
print(places)

places.reverse()
print("\nHere is the list in reverse order:")
print(places)

places.reverse()
print("\nAnd I've reversed it back again:")
print(places)

places.sort()
print("\nDoing some permanent damage now...here is the list stored in alphabetical order:")
print(places)

places.sort(reverse=True)
print("\nChanging things up today! Decided to store the list in reverse alphabetical order:")
print(places)
