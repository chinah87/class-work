#print a list of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#replace a value with a different one
motorcycles[0] = 'ducati'
print(motorcycles)

#add a value to the end of the list
motorcycles.append('kawasaki')
print(motorcycles)

#start with a blank list and add values into it
cars = []
cars.append('ford')
cars.append('toyota')
cars.append('hyundai')
print(cars)

#insert a value into the existing list
cars.insert(1, 'BMW')
print(cars)

#delete a value from the list
del cars[3]
print(cars)

#delete (pop) a value from anywhere in the list, but save it in the system for use elsewhere
first_car = cars.pop(0)
print(cars)
print(first_car)
print('The first car I owned was a ' + first_car.title() + '.')

#delete a (pop) value from the end of the list, but save it in the system for use elsewhere
last_car = cars.pop()
print('The last car I owned was a ' + last_car.title() + '.')
print(cars)

#remove a value from the list, and use it elsewhere
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki', 'kawasaki']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')