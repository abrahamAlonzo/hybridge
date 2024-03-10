message ='Ingresa un número:'

print(message)
number=input()

if int(number) % 2:
  print('El número {number} es impar.'.format(number=number))
else:
  print('El número {number} es par.'.format(number=number))