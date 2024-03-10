# Clase DimmerSwitch
class DimmerSwitch():
  def __init__(self):
    self.switchIsOn = False    # Indica si el interruptor está encendido o apagado
    self.brightness = 0        # Nivel de brillo actual

  def turnOn(self):
    self.switchIsOn = True     # Enciende el interruptor

  def turnOff(self):
    self.switchIsOn = False    # Apaga el interruptor

  def raiseLevel(self):
    if self.brightness < 10:
      self.brightness = self.brightness + 1    # Aumenta el nivel de brillo en 1

  def lowerLevel(self):
    if self.brightness > 0:
      self.brightness = self.brightness - 1    # Reduce el nivel de brillo en 1

  # Método adicional para depuración (debugging)
  def show(self):
    print('¿El interruptor está encendido?', self.switchIsOn)    # Muestra el estado del interruptor
    print('El nivel de brillo es:', self.brightness)    # Muestra el nivel de brillo actual


# Código principal
objeto_dimmer = DimmerSwitch()

# Enciende el interruptor y aumenta el nivel 5 veces
objeto_dimmer.turnOn()
objeto_dimmer.raiseLevel()
objeto_dimmer.raiseLevel()
objeto_dimmer.raiseLevel()
objeto_dimmer.raiseLevel()
objeto_dimmer.raiseLevel()
objeto_dimmer.show()

# Reduce el nivel 2 veces y apaga el interruptor
objeto_dimmer.lowerLevel()
objeto_dimmer.lowerLevel()
objeto_dimmer.turnOff()
objeto_dimmer.show()

# Enciende el interruptor y aumenta el nivel 3 veces
objeto_dimmer.turnOn()
objeto_dimmer.raiseLevel()
objeto_dimmer.raiseLevel()
objeto_dimmer.raiseLevel()
objeto_dimmer.show()