# Programa de prueba usando cuentas
# Versión 2, utilizando una lista de cuentas
# Importar todo el código de la clase Cuenta desde el archivo Account.py
from Account import *

# Comenzar con una lista vacía de cuentas
listaDeCuentas = []

# Crear dos cuentas
objeto_Account = Cuenta('Joe', 100, 'ContraseñaDeJoe')
listaDeCuentas.append(objeto_Account)
print("El número de cuenta de Joe es 0")

objeto_Account = Cuenta('Mary', 12345, 'ContraseñaDeMary')
listaDeCuentas.append(objeto_Account)
print("El número de cuenta de Mary es 1")

listaDeCuentas[0].show()
listaDeCuentas[1].show()
print()

# Llamar a algunos métodos de las cuentas diferentes
print('Llamando a métodos de las dos cuentas...')
listaDeCuentas[0].deposit(50, 'ContraseñaDeJoe')
listaDeCuentas[1].withdraw(345, 'ContraseñaDeMary')
listaDeCuentas[1].deposit(100, 'ContraseñaDeMary')

# Mostrar las cuentas
listaDeCuentas[0].show()
listaDeCuentas[1].show()

# Crear otra cuenta con información proporcionada por el usuario
print()
nombreUsuario = input('¿Cuál es el nombre para la nueva cuenta de usuario? ')
saldoUsuario = int(input('¿Cuál es el saldo inicial para esta cuenta? '))
passUsuario = input('¿Cuál es la contraseña que deseas utilizar para esta cuenta? ')
objeto_Account = Cuenta(nombreUsuario, saldoUsuario, passUsuario)
listaDeCuentas.append(objeto_Account)  # agregar a la lista de cuentas

# Mostrar la nueva cuenta de usuario creada
print('Se ha creado una nueva cuenta, el número de cuenta es 2')
listaDeCuentas[2].show()

# Realicemos un depósito de 100 en la nueva cuenta
listaDeCuentas[2].deposit(100, passUsuario)
saldoUsuario = listaDeCuentas[2].getBalance(passUsuario)
print()
print('Después de depositar 100, el saldo del usuario es:', saldoUsuario)

# Mostrar la nueva cuenta de usuario
listaDeCuentas[2].show()


while True:
    print()
    print('Presiona b para obtener el saldo')
    print('Presiona d para hacer un depósito')
    print('Presiona o para abrir una nueva cuenta')
    print('Presiona w para hacer un retiro')
    print('Presiona s para mostrar todas las cuentas')
    print('Presiona q para salir')
    print()
    accion = input('¿Qué deseas hacer? ')
    accion = accion.lower()
    print()

    if accion == 'b':
        print('*** Obtener Saldo ***')
        numeroCuentaUsuario = int(input('Por favor, ingresa el número de tu cuenta: '))
        passCuentaUsuario = input('Por favor, ingresa la contraseña: ')
        objeto_Cuenta = diccionario_cuentas[numeroCuentaUsuario]
        saldoActual = objeto_Cuenta.getBalance(passCuentaUsuario)
        if saldoActual is not None:
            print('Tu saldo es:', saldoActual)

    elif accion == 'd':
        print('*** Depósito ***')
        numeroCuentaUsuario = int(input('Por favor, ingresa el número de cuenta: '))
        montoDepositoUsuario = int(input('Por favor, ingresa la cantidad a depositar: '))
        passUsuario = input('Por favor, ingresa la contraseña: ')
        objeto_Cuenta = diccionario_cuentas[numeroCuentaUsuario]
        saldoActualizado = objeto_Cuenta.deposit(montoDepositoUsuario, passUsuario)
        if saldoActualizado is not None:
            print('Tu nuevo saldo es:', saldoActualizado)

    elif accion == 'o':
        print('*** Abrir Cuenta ***')
        nombreUsuario = input('¿Cuál es el nombre para la nueva cuenta de usuario? ')
        saldoInicialUsuario = int(input('¿Cuál es el saldo inicial para esta cuenta? '))
        passUsuario = input('¿Cuál es la contraseña que deseas utilizar para esta cuenta? ')
        objeto_Cuenta = Cuenta(nombreUsuario, saldoInicialUsuario, passUsuario)
        diccionario_cuentas[nextAccountNumber] = objeto_Cuenta
        print('Tu nuevo número de cuenta es:', nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()

    elif accion == 's':
        print('Mostrar:')
        for numeroCuentaUsuario in diccionario_cuentas:
            objeto_Cuenta = diccionario_cuentas[numeroCuentaUsuario]
            print('    Número de cuenta:', numeroCuentaUsuario)
            objeto_Cuenta.show()

    elif accion == 'q':
        break

    elif accion == 'w':
        print('*** Retiro ***')
        numeroCuentaUsuario = int(input('Por favor, ingresa el número de tu cuenta: '))
        montoRetiroUsuario = int(input('Por favor, ingresa la cantidad a retirar: '))
        passUsuario = input('Por favor, ingresa la contraseña: ')
        objeto_Cuenta = diccionario_cuentas[numeroCuentaUsuario]
        saldoActualizado = objeto_Cuenta.withdraw(montoRetiroUsuario, passUsuario)
        if saldoActualizado is not None:
            print('Retiraste:', montoRetiroUsuario)
            print('Tu nuevo saldo es:', saldoActualizado)

    else:
        print('Lo siento, esa no es una acción válida. Por favor, intenta nuevamente.')

print('Hecho')