#numbers in a range
for value in range(1,5):
    print(value) 
print("\n")
for value in range(1,6):
    print(value)
print("\n")
    
#list function and skipping numbers
numbers = list(range(1,6))
print(numbers)
print("\n")

even_numbers = list(range(2,11,2))
print(even_numbers)
print("\n")

by_threes = list(range(0,15,3))
print(by_threes)
print("\n")

#square numbers with exponents
#use this first method to show your thinking...useful for when you're drafting
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
print("\n")

#written more efficiently
#after trying the first method, you can write your code more cleanly
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print("\n")

#minimum, maximum, and sum
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
print("\n")

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
print("\n")

