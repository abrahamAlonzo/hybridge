message ='Cual es tu cancion favorita?'
authorQuestionMessage = 'a que autor pertenece?'

print(message)
song=input()
print(authorQuestionMessage)
author=input()

print('Mi canción favorita es "{song}" de {author}.'.format(song=song,author=author))