#pizza list
pizzas = ['sausage', 'hawaiian', 'extra cheese', 'garlic', 'barbeque chicken']

#for loop
for pizza in pizzas:
    print("I love " + pizza.title() + " pizza way too much.\n")

#concluding remark
print("Basically, I just love pizza.")

#create slices
print("\nThe first three items in the list are:")
print(pizzas[:3])

print("\nThree items from the middle of the list are:")
print(pizzas[1:4])

print("\nThe last three items in the list are:")
print(pizzas[-3:])

#friend pizzas
friend_pizzas = pizzas[:]
pizzas.append('tuna mayo')
friend_pizzas.append('spicy sausage')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)