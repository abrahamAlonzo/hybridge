# Non-OOP
# Bank 3
# Two accounts
nombre_cuenta_0 = ''
saldo_cuenta_0 = 0
contrasenia_cuenta_0 = ''
nombre_cuenta_1 = ''
saldo_cuenta_1 = 0
contrasenia_cuenta_1 = ''
nCuentas = 0

def nueva_cuenta(numero_de_cuenta, nombre, saldo, contrasenia):
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0 
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1
  if numero_de_cuenta == 0:
    nombre_cuenta_0 = nombre
    saldo_cuenta_0 = saldo
    contrasenia_cuenta_0 = contrasenia
  if numero_de_cuenta == 1:
    nombre_cuenta_1 = nombre
    saldo_cuenta_1 = saldo
    contrasenia_cuenta_1 = contrasenia
def show():
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1 
  if nombre_cuenta_0 != '':
    print('Cuenta 0')
    print('       nombre', nombre_cuenta_0)
    print('       saldo:', saldo_cuenta_0)
    print('       contraseña:', contrasenia_cuenta_0)
    print()
  if nombre_cuenta_1 != '':
      print('Cuenta 1')
      print('       nombre', nombre_cuenta_1)
      print('       saldo:', saldo_cuenta_1)
      print('       contraseña:', contrasenia_cuenta_1)
      print()

def getsaldo(numero_de_cuenta, contrasenia):
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0 
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1
  if numero_de_cuenta == 0:
      if contrasenia != contrasenia_cuenta_0:
          print('Contraseña incorrecta')
          return None
      return saldo_cuenta_0
  if numero_de_cuenta == 1:
      if contrasenia != contrasenia_cuenta_1:
          print('Contraseña incorrecta')
          return None
      return saldo_cuenta_1
  

def deposito(numero_de_cuenta, cantidad, contrasenia):
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0 
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1
  if numero_de_cuenta == 0:
    if contrasenia != contrasenia_cuenta_0:
      print('Contraseña incorrecta')
      return
    saldo_cuenta_0 = saldo_cuenta_0 + cantidad
  if numero_de_cuenta == 1:
    if contrasenia != contrasenia_cuenta_1:
      print('Contraseña incorrecta')
      return
    saldo_cuenta_1 = saldo_cuenta_1 + cantidad

def retiro(numero_de_cuenta, cantidad, contrasenia):
  global nombre_cuenta_0, saldo_cuenta_0, contrasenia_cuenta_0 
  global nombre_cuenta_1, saldo_cuenta_1, contrasenia_cuenta_1
  if numero_de_cuenta == 0:
    if contrasenia != contrasenia_cuenta_0:
      print('Contraseña incorrecta')
      return
    if cantidad > saldo_cuenta_0:
      print('El saldo de tu cuenta no es suficiente')
      return
    saldo_cuenta_0 = saldo_cuenta_0 - cantidad
  if numero_de_cuenta == 1:
    if contrasenia != contrasenia_cuenta_1:
      print('Contraseña incorrecta')
      return
    if cantidad > saldo_cuenta_1:
      print('El saldo de tu cuenta no es suficiente')
      return
    saldo_cuenta_1 = saldo_cuenta_1 - cantidad
  

#  --- Recortamos las funciones adicionales deposito() y retiro() ---
#  --- Tambien el código principal que las llama ---

print('Bye')