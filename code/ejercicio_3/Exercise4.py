


message ='¿Te gusta el chocolate? (sí/no)'
defaultErrorMessage = 'Respuesta invalida'

print(message)
answer=input()
answerOptions = {
  'si': True,
  'no': False,
}
print('{boolean}'.format(boolean=answerOptions.get(answer.lower(), defaultErrorMessage)))