# Clase TV
class TV():
  def __init__(self):
    self.isOn = False
    self.isMuted = False
    # Algunos canales predeterminados
    self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
    self.nChannels = len(self.channelList)
    self.channelIndex = 0
    self.VOLUME_MINIMUM = 0    # constante
    self.VOLUME_MAXIMUM = 10   # constante
    self.volume = self.VOLUME_MAXIMUM // 2

  def power(self):
    self.isOn = not self.isOn   # toggle

  def volumeUp(self):
    if not self.isOn:
      return
    if self.isMuted:
      self.isMuted = False     # cambiar el volumen mientras está silenciado reactiva el sonido
    if self.volume < self.VOLUME_MAXIMUM:
      self.volume = self.volume + 1

  def volumeDown(self):
    if not self.isOn:
      return
    if self.isMuted:
      self.isMuted = False     # cambiar el volumen mientras está silenciado reactiva el sonido
    if self.volume > self.VOLUME_MINIMUM:
      self.volume = self.volume - 1

  def channelUp(self):
    if not self.isOn:
      return
    self.channelIndex = self.channelIndex + 1
    if self.channelIndex >= self.nChannels:   # si el índice del canal excede el número de canales
      self.channelIndex = 0   # volver al primer canal

  def channelDown(self):
    if not self.isOn:
      return
    self.channelIndex = self.channelIndex - 1
    if self.channelIndex < 0:    # si el índice del canal es menor que cero
      self.channelIndex = self.nChannels - 1    # volver al último canal

  def mute(self):
    if not self.isOn:
      return
    self.isMuted = not self.isMuted

  def setChannel(self, newChannel):
    if newChannel in self.channelList:
      self.channelIndex = self.channelList.index(newChannel)
    # si el nuevo canal no está en nuestra lista de canales, no hace nada

  def showInfo(self):
    print('Estado del TV:')
    if self.isOn:
      print('    La TV está: Encendida')
      print('    El canal es:', self.channelList[self.channelIndex])
      if self.isMuted:
        print('    El volumen es:', self.volume, '(el sonido está silenciado)')
      else:
        print('    El volumen es:', self.volume)
    else:
      print('    TV está: Apagado')

# Código principal
objeto_tv1 = TV()  # crear un objeto TV
objeto_tv2 = TV()  # crear otro objeto TV

# Encender ambos televisores
objeto_tv1.power()
objeto_tv2.power()

# Aumentar el volumen de TV1
objeto_tv1.volumeUp()
objeto_tv1.volumeUp()

# Aumentar el volumen de TV2
objeto_tv2.volumeUp()
objeto_tv2.volumeUp()
objeto_tv2.volumeUp()
objeto_tv2.volumeUp()
objeto_tv2.volumeUp()

# Cambiar el canal de TV2, luego silenciarlo
objeto_tv2.setChannel(44)
objeto_tv2.mute()

# Mostrar la información de ambos televisores
objeto_tv1.showInfo()
objeto_tv2.showInfo()