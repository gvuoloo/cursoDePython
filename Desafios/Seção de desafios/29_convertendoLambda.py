#Desafio 29

#Crie uma função lambda que aceite um número e retorne o cubo desse número.

cubo = lambda x: x ** 3

user_x = int(input('Insira um número:'))

print (f'O cubo de {user_x} é igual a {cubo(user_x)}.')