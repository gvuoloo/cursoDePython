#Desafio 31

#Crie uma função lambda que aceite um número e retorne "Par" se o número for par e "Ímpar" se o número for ímpar.

impar_par = lambda x: 'par' if x % 2 == 0 else 'ímpar'

user_x = int(input('Insira um número: '))

print(f'O número {user_x} é um número {impar_par(user_x)}.')