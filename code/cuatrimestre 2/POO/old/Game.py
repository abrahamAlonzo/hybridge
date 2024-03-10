# Clase Player
class Player():
  def __init__(self, name):
    self.name = name
    self.points = 0
    self.health = 100
    self.isDeath = False
    self.isInvincible = False

  def receiveDamage(self, damage):
    self.health = self.health - damage

  def receivePoints(self, points):
    self.points = self.points + points
    if(self.points < 1):
      self.isDeath = True # el jugador ha muerto

  def showInfo(self):
    print('Estado del Player:')
    print('    Nombre:', self.name)
    print('    Puntos:', self.points)
    print('    Salud:', self.health)
    if self.isDeath:
      print('    El jugador ha muerto')
    else:
      print('    El jugador sigue vivo')
  

# Código principal
objeto_player = Player('Abraham')  # crear un objeto Player
objeto_player.showInfo()
objeto_player.receiveDamage(50)
objeto_player.showInfo()
objeto_player.receivePoints(-100)
objeto_player.showInfo()
