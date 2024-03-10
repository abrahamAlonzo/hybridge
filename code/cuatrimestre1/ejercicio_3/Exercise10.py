message ='¿Prefieres el verano o el invierno?'
defaultErrorMessage = 'Respuesta invalida'

print(message)
answer=input()
answerOptions = {
  'verano': True,
  'invierno': False,
}
print('{boolean}'.format(boolean=answerOptions.get(answer.lower(), defaultErrorMessage)))