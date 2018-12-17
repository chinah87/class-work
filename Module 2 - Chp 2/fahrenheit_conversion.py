fahrenheit_temp = input('Enter the temperatures in degrees Fahrenheit? ')
celcius_temp = round((float(fahrenheit_temp)-32)*5/9,2)
print('The temperature ' + str(fahrenheit_temp) + ' degrees Fahrenheit is ' + str(celcius_temp) + ' degrees Celsius.')