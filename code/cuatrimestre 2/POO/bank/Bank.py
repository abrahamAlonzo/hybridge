# Banco que administra un diccionario de objetos Cuenta (Account)
from Account import *

class Banco():
  def __init__(self, horas, dirección, telefono):
    self.cuentasDict = {}
    self.siguienteNumeroCuenta = 0
    self.horas = horas
    self.dirección = dirección
    self.teléfono = telefono
  

  def pedirNúmeroDeCuentaVálido(self):
    númeroDeCuenta = input('¿Cuál es su número de cuenta? ')
    try:
      númeroDeCuenta = int(númeroDeCuenta)
    except ValueError:
      raise AbortTransaction('El número de cuenta debe ser un número entero')
    
    if númeroDeCuenta not in self.cuentasDict:
      raise AbortTransaction('No existe la cuenta ' + str(númeroDeCuenta))
    
    return númeroDeCuenta

  def obtenerCuentaDeUsuario(self):
    numeroDeCuenta = self.pedirNúmeroDeCuentaVálido()
    objeto_Cuenta = self.cuentasDict[numeroDeCuenta]
    self.pedirContraseñaVálida(objeto_Cuenta)
    return objeto_Cuenta

  def crearCuenta(self, elNombre, elSaldoInicial, elPassword):
    objeto_Cuenta = Cuenta(elNombre, elSaldoInicial, elPassword)
    nuevoNumeroCuenta = self.siguienteNumeroCuenta
    self.cuentasDict[nuevoNumeroCuenta] = objeto_Cuenta
    # Incrementar para prepararse para la próxima cuenta a crear
    self.siguienteNumeroCuenta = self.siguienteNumeroCuenta + 1
    return nuevoNumeroCuenta

# --- Se omitieron métodos (Te toca agregarlos por tu cuenta) ---

  def depositar(self):
    print('*** Depósito ***')
    objeto_Cuenta = self.obtenerCuentaDeUsuario()
    cantidadDeDeposito = input('Por favor ingrese la cantidad a depositar: ')
    elSaldo = objeto_Cuenta.deposit(cantidadDeDeposito)
    print('Depositado:', cantidadDeDepósito)
    print('Su nuevo saldo es:', elSaldo)

  def mostrar(self):
    print('*** Mostrar ***')
    print('(Normalmente esto requeriría una contraseña de administrador)')
    for numeroDeCuentaDeUsuario in self.cuentasDict:
      objeto_Cuenta = self.cuentasDict[númeroDeCuentaDeUsuario]
      print('Cuenta:', numeroDeCuentaDeUsuario)
      objeto_Cuenta.show()
      print()

  def retirar(self):
    print('*** Retiro ***')
    objeto_Cuenta = self.obtenerCuentaDeUsuario()
    cantidadDelUsuario = input('Por favor ingrese la cantidad a retirar: ')
    elSaldo = objeto_Cuenta.withdraw(cantidadDelUsuario)
    print('Retirado:', cantidadDelUsuario)
    print('Su nuevo saldo es:', elSaldo)
        
  def obtenerInformacion(self):
    print('Horas:', self.horas)
    print('Dirección:', self.dirección)
    print('Teléfono:', self.teléfono)
    print('Actualmente tenemos', len(self.cuentasDict), 'cuenta(s) abierta(s).')