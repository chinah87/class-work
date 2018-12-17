#use a tuple to make sure the dimensions of this square doesn't change
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#print as a loop
for dimension in dimensions:
    print(dimension)
    
#you can write over a tuple by overwriting the variable
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#if you try to alter a dimension, you will receive a type error
dimensions[0] = 250