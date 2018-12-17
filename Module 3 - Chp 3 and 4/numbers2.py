#counting to twenty
for value in range(1,21):
    print(value)
print("\n")

#one hundred
numbers = list(range(1,101))
for number in numbers:
    print(number)
print("\n")

#summing a hundred
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("\n")

#odd numbers
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)
print("\n")

#threes
threes = list(range(3,31,3))
for number in threes:
    print(number)
print("\n")

#cubes
cubes = []
for number in range(1,11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)
print("\n")

#cube comprehension
cubes = [cube**3 for cube in range(1,11)]
print(cubes)