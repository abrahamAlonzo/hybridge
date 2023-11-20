message ='Ingresa tu nombre: '
message2 ='Ingresa tu edad: '

print(message)
firstName=input()
print(message2)
age=input()

print('{firstName} tiene {age} años.'.format(firstName=firstName,age=age))
