# This program says hello and asks for my name

print('Hallo!')
print('Wie heißt du?')
myName = input()
print('Schön, dich zu sehen, ' + myName)
print('Dein Name hat so viele Buchstaben: ')
print(len(myName))
print('Wie alt bist du?')
myAge = input()
print('Nächstes Jahr bist du ' + str(int(myAge)+1) + ' Jahre alt.')