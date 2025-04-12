#Desafio 30

#Crie uma função lambda que aceite dois número e retorne a multiplicação desses números.

multi = lambda x, y: x * y

user_x = int(input('Insira um número:'))
user_y = int(input('Insira um outro número:'))

print (f'A multiplicação entre  {user_x} e {user_y} é igual a {multi(user_x, user_y)}.')